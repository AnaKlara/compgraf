# USO
# No terminal, digite e execute o comando abaixo:
# python build_covid_dataset.py --covid covid-chestxray-dataset --output dataset/covid

# importando os pacotes necessários
import pandas as pd
import argparse
import shutil
import os

# analisador de argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--covid", required=True,
	help="path para o diretório do dataset COVID-19")
ap.add_argument("-o", "--output", required=True,
	help="path para o diretório onde imagens 'normal' serão armazenadas")
args = vars(ap.parse_args())

# cria path para o CSV com metados
# carrega o CSV de metadados
csvPath = os.path.sep.join([args["covid"], "metadata.csv"])
df = pd.read_csv(csvPath)

# loop pelas linhas do dataframe COVID-19
for (i, row) in df.iterrows():
	# Se
    # (1) o caso atual não é COVID-19 OU (2) a imagem não é uma 'PA view'
	# então 
    #ignora a linha
    # para entender melhor 'PA' view veja: https://radiopaedia.org/articles/chest-pa-view-1
	if row["finding"] != "COVID-19" or row["view"] != "PA":
		continue

	# gerando  o path para a imagem de input
	imagePath = os.path.sep.join([args["covid"], "images",
		row["filename"]])
    """
	se a imagem não existir (existem alguns error no arquivo de 
    metadados do COVID-19), ignora a linha
	"""
    if not os.path.exists(imagePath):
		continue

    # extrai o nome da imagem do respectivo path  e então
	# contrói o path para a imagem copiada
	filename = row["filename"].split(os.path.sep)[-1]
	outputPath = os.path.sep.join([args["output"], filename])

	# copia a imagem
	shutil.copy2(imagePath, outputPath)