import streamlit as st
import numpy as np
import pickle

# Judul Aplikasi
st.title("Prediksi Kelulusan Mahasiswa — Classification Model")

# Load model (jika sudah ada model tersimpan)
# try:
#     with open('model.pkl', 'rb') as f:
#         model = pickle.load(f)
# except FileNotFoundError:
#     model = None

# Input user
st.header("Input Data Mahasiswa")
absensi = st.number_input("Persentase Kehadiran (%)", min_value=0, max_value=100, step=1)
nilai_tugas = st.number_input("Nilai Tugas", min_value=0, max_value=100, step=1)
nilai_ujian = st.number_input("Nilai Ujian", min_value=0, max_value=100, step=1)

# Prediksi (dummy sebelum model dibuat)
def dummy_predict(absen, tugas, ujian):
    skor = (absen * 0.3) + (tugas * 0.3) + (ujian * 0.4)
    return "LULUS" if skor >= 60 else "TIDAK LULUS"

if st.button("Prediksi Kelulusan"):
    # jika model asli ada, gunakan: model.predict([[absensi, nilai_tugas, nilai_ujian]])
    hasil = dummy_predict(absensi, nilai_tugas, nilai_ujian)
    st.subheader(f"Hasil Prediksi: {hasil}")
