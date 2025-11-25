import joblib
import numpy as np

model = joblib.load('models/model.joblib')

def prediksi(absensi, tugas, ujian):
    data = np.array([[absensi, tugas, ujian]])
    pred = model.predict(data)[0]
    return "Lulus" if pred == 1 else "Tidak Lulus"