# importa os pacotes necessários
from imutils import paths
import numpy as np
import cv2

def quantify_image(image, bins=(4, 6, 3)):
	# calcula um histograma de cores 3D sobre a imagem
	hist = cv2.calcHist([image], [0, 1, 2], None, bins,
		[0, 180, 0, 256, 0, 256])
	# normaliza o histograma
 	# ver https://pt.wikipedia.org/wiki/Equaliza%C3%A7%C3%A3o_de_histograma
	hist = cv2.normalize(hist, hist).flatten()

	# retorna o histograma
	return hist

def load_dataset(datasetPath, bins):
	# reúne todos os paths para imagens
	# inicializa a lista de imagens
	imagePaths = list(paths.list_images(datasetPath))
	data = []

	# loop pela lista de paths para as imagens
	for imagePath in imagePaths:
		# carrega a imagem e converte para the HSV color space
		image = cv2.imread(imagePath)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		# quantifica a imagem e atualiza a lista
		features = quantify_image(image, bins)
		data.append(features)

	# retorna nossa lista de dados como numpy array 
	return np.array(data)