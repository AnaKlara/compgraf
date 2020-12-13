# USO
# no terminal, digite:
# python test_anomaly-detector.py --model anomaly_detector.model --image exemplos/highway_a836030.jpg

# importando os pacotes necessários
from code.features import quantify_image
import argparse
import pickle
import cv2

# analisador de argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path para o modelo treinado")
ap.add_argument("-i", "--image", required=True,
	help="path para a imagem de input")
args = vars(ap.parse_args())

# carrega o modelo de detecção de anomalia
print("[INFO] carregando o modelo...")
model = pickle.loads(open(args["model"], "rb").read())

# carrega a imagem de input, converte para HSV color space 
# ver https://pt.wikipedia.org/wiki/HSV
# quatifica a image
image = cv2.imread(args["image"])
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
features = quantify_image(hsv, bins=(3, 3, 3))

# usa o modelo e as features extraídas para determinar
# se a imagem de exemplo é uma anomalia ou não
preds = model.predict([features])[0]
label = "anomalia" if preds == -1 else "normal"
color = (0, 0, 255) if preds == -1 else (0, 255, 0)

# desenha o rótulo(resultante do modelo) na imagem original
cv2.putText(image, label, (10,  25), cv2.FONT_HERSHEY_SIMPLEX,
	0.7, color, 2)

# exibe a imagem
cv2.imshow("Output", image)
cv2.waitKey(0)

exit()