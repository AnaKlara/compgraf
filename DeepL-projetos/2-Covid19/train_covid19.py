# USO
# No terminal, digite:
# python train.py --dataset dataset

# importando pacotes necessários
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
import os

# analisador de argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path para o dataset de input")
ap.add_argument("-p", "--plot", type=str, default="plot.png",
	help="path para o plot loss/accuracy ")
ap.add_argument("-m", "--model", type=str, default="covid19.model",
	help="path para o output do plot de loss/accuracy")
args = vars(ap.parse_args())


# Inicializando variáveis:
INIT_LR = 1e-3 # initial learning rate
EPOCHS = 25 # number of epochs to train for
BS = 8 # batch size

# inicializa uma lista contendo imagens que estão dentro do diretório
# ta lista com os dados (ex.: images) e uma com as classes das imagens
print("[INFO] carregando imagens...")
imagePaths = list(paths.list_images(args["dataset"]))
data = []
labels = []

# loop pelos paths para as imagens
for imagePath in imagePaths:
	# extraindo a classificação do nome da imagem
	label = imagePath.split(os.path.sep)[-2]

	# carregando a imagem
    # trocando canais de cores 
    # redimensionando para o tamanho fixo de 224x224 pixels
	# ignora aspect ratio
	image = cv2.imread(imagePath)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	image = cv2.resize(image, (224, 224))

	# atualiza a lista de dados e categorias
	data.append(image)
	labels.append(label)

"""
convete os dados e as classificações para Numpy arrays enquanto
escala a intensidade dos pixels para o intervalo [0, 255]
"""
data = np.array(data) / 255.0
labels = np.array(labels)

# executar codificação one-hot nas classes
lb = LabelBinarizer()
labels = lb.fit_transform(labels)
labels = to_categorical(labels)

# Divide os dados em dois pedaços: dados de treinamento e de teste 
# usando 80% dos dados para treinamento e os
# 20% restantes para teste
(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.20, stratify=labels, random_state=42)

# inicializando objeto responsável pelo Aumento de dados de Imagem
'''
O aumento de dados de imagem é uma técnica que pode ser usada para expandir 
artificialmente o tamanho de um conjunto de dados de treinamento 
criando versões modificadas de imagens no conjunto de dados.
Ver https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/
'''
trainAug = ImageDataGenerator(
	rotation_range=15,
	fill_mode="nearest")

# carrega a rede VGG16 
# garantindo que os conjuntos de camadas FC principais sejam deixados de fora
baseModel = VGG16(weights="imagenet", include_top=False,
	input_tensor=Input(shape=(224, 224, 3)))

# construindo a cabeça do modelo que será colocado em cima do modelo base
headModel = baseModel.output
headModel = AveragePooling2D(pool_size=(4, 4))(headModel)
headModel = Flatten(name="flatten")(headModel)
headModel = Dense(64, activation="relu")(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(2, activation="softmax")(headModel)

# coloca o modelo FC principal sobre o modelo base (isso se tornará
# o modelo real que treinaremos)
model = Model(inputs=baseModel.input, outputs=headModel)

# passa por todas as camadas no modelo base e as congela para que elas
# não seja atualizadas durante o primeiro processo de treinamento
for layer in baseModel.layers:
	layer.trainable = False

# compila modelo
print("[INFO] compilando modelo...")
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="binary_crossentropy", optimizer=opt,
	metrics=["accuracy"])

# treinando o head da rede
print("[INFO] treinando o head...")
H = model.fit_generator(
	trainAug.flow(trainX, trainY, batch_size=BS),
	steps_per_epoch=len(trainX) // BS,
	validation_data=(testX, testY),
	validation_steps=len(testX) // BS,
	epochs=EPOCHS)

# fazendo predições nos dados de teste
print("[INFO] evaluating network...")
predIdxs = model.predict(testX, batch_size=BS)

"""
para cada imagem no conjunto de testes, precisamos encontrar o índice do
etiqueta com a maior probabilidade prevista correspondente
"""
predIdxs = np.argmax(predIdxs, axis=1)

# mostra um relatório de classificação bem formatado
print(classification_report(testY.argmax(axis=1), predIdxs,
	target_names=lb.classes_))

# calcula a matriz de confusão e a usa para derivar a
# precisão, sensibilidade e especificidade
cm = confusion_matrix(testY.argmax(axis=1), predIdxs)
total = sum(sum(cm))
acc = (cm[0, 0] + cm[1, 1]) / total
sensitivity = cm[0, 0] / (cm[0, 0] + cm[0, 1])
specificity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

# mostra a matriz de confusão, precisão, sensibilidade e especificidade
print(cm)
print("acc: {:.4f}".format(acc))
print("sensitivity: {:.4f}".format(sensitivity))
print("specificity: {:.4f}".format(specificity))

# plota a perda e a acurácia do treinamento
N = EPOCHS
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), H.history["accuracy"], label="train_acc")
plt.plot(np.arange(0, N), H.history["val_accuracy"], label="val_acc")
plt.title("Perda e a acurácia do treinamento nos dados da COVID-19")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="lower left")
plt.savefig(args["plot"])

# salvando modelo em disco
print("[INFO] salvando modelo de detecção COVID-19...")
model.save(args["model"], save_format="h5")