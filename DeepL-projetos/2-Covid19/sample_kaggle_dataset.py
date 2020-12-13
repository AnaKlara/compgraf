# USO
#
# No terminal, digite:
# python sample_kaggle_dataset.py --kaggle chest_xray --output dataset/normal

# importando os pacotes necessários
from imutils import paths
import argparse
import random
import shutil
import os

# analisador de argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--kaggle", required=True,
	help="path para o diretório para o dataset de imagens raio-x da Kaggle")
ap.add_argument("-o", "--output", required=True,
	help="path para o diretório onde imagens com exemplos de raio-x 'normal' serão armazenadas")
ap.add_argument("-s", "--sample", type=int, default=25,
	help="número de amostras para baixar do Kaggle dataset")
args = vars(ap.parse_args())

# reúne paths para as imagensde raio-x de treinameto a partir do conjunto de dados da Kaggle
basePath = os.path.sep.join([args["kaggle"], "train", "NORMAL"])
imagePaths = list(paths.list_images(args["kaggle"]))

# separando imagens randomicamente
random.seed(42)
random.shuffle(imagePaths)
imagePaths = imagePaths[:args["sample"]]

# loop pelos paths das imagens
for (i, imagePath) in enumerate(imagePaths):
    #extrai o nome do arquivo do path e então constrói o 
    # path para a imagem copiada
	filename = imagePath.split(os.path.sep)[-1]
	outputPath = os.path.sep.join([args["output"], filename])

	# copia a imagem
	shutil.copy2(imagePath, outputPath)