# USO  
# no terminal, digite:
# python train_anomaly_detector.py --dataset floresta --model anomaly_detector.model

# importando os pacotes necessários
from code.features import load_dataset
from sklearn.ensemble import IsolationForest
import argparse
import pickle

# analisador de argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path para o dataset de imagens")
ap.add_argument("-m", "--model", required=True,
	help="path para o output do modelo Detecção de anomalia")
args = vars(ap.parse_args())

# carrega e quantifica o dataset de imagens
print("[INFO] preparando o dataset...")
data = load_dataset(args["dataset"], bins=(3, 3, 3))

# train the anomaly detection model
print("[INFO] construindo o modelo...")
model = IsolationForest(n_estimators=100, contamination=0.01,
	random_state=42)
model.fit(data)

# serializando o modelo de detecção de anomalia em disco
f = open(args["model"], "wb")
f.write(pickle.dumps(model))
f.close()