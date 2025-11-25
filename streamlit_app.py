import streamlit as st
import pickle
import numpy as np

# =========================
# 🎀 Custom Pink CSS
# =========================
pink_css = """
<style>
/* Background color */
body {
    background-color: #ffe6f2 !important;
}

/* Streamlit headers */
h1, h2, h3 {
    color: #d63384;
    text-align: center;
    font-family: 'Poppins', sans-serif;
}

/* Cards */
.block-container {
    padding: 2rem 2rem;
    background-color: #ffffffdd;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(255, 105, 180, 0.2);
}

/* Input style */
.stNumberInput label {
    color: #d63384 !important;
    font-weight: 600;
}

/* Button pink */
.stButton>button {
    background-color: #ff4da6 !important;
    color: white !important;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 18px;
    border: none;
}
.stButton>button:hover {
    background-color: #e60073 !important;
}
</style>
"""
st.markdown(pink_css, unsafe_allow_html=True)

# =========================
# 🎓 Load Model
# =========================
model = pickle.load(open("model.pkl", "rb"))

# =========================
# UI
# =========================
st.title("🎀 Prediksi Kelulusan Mahasiswa 🎓")
st.write("Masukkan data berikut untuk memprediksi apakah mahasiswa *Lulus* atau *Tidak Lulus*.")

absen = st.number_input("📌 Persentase Absensi (%)", 0, 100)
tugas = st.number_input("📘 Nilai Tugas", 0, 100)
ujian = st.number_input("📝 Nilai Ujian", 0, 100)

if st.button("💗 Prediksi Sekarang"):
    # Convert input
    x = np.array([[absen, tugas, ujian]])
    pred = model.predict(x)[0]

    if pred == 1:
        st.success("🎉 **Hasil: LULUS!** Tetap pertahankan prestasimu ya 💖")
    else:
        st.error("❌ **Hasil: TIDAK LULUS** Semangat! Kamu pasti bisa 💪")
