import streamlit as st
from src.predict import prediksi

# ===================== CSS CUSTOM (PINK THEME) =====================
st.markdown("""
<style>
/* Tombol */
div.stButton > button {
    background-color: #ff69b4; /* Pink */
    color: white;
    padding: 10px 25px;
    border-radius: 8px;
    border: none;
    font-size: 16px;
}
div.stButton > button:hover {
    background-color: #ff4da6; /* Pink lebih gelap */
}

/* Card */
.card {
    background-color: #fff0f7; /* Pink pastel */
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #ffcce6;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)


# ===================== HEADER (PINK) =====================
st.markdown("""
    <div style='background-color:#ff69b4;padding:15px;border-radius:10px;margin-bottom:20px'>
        <h1 style='color:white;text-align:center;'>💗 Sistem Prediksi Kelulusan Mahasiswa 💗</h1>
    </div>
""", unsafe_allow_html=True)


# ===================== CARD FORM INPUT =====================
st.markdown("<div class='card'><h3 style='color:#d63384;'>Masukkan Data Mahasiswa 🌸</h3></div>", unsafe_allow_html=True)

absensi = st.number_input("Masukkan nilai Absensi", 0, 100)
tugas = st.number_input("Masukkan nilai Tugas", 0, 100)
ujian = st.number_input("Masukkan nilai Ujian", 0, 100)


# ===================== BUTTON & PREDIKSI =====================
if st.button("🔍 Prediksi Kelulusan"):
    hasil = prediksi(absensi, tugas, ujian)

    if hasil == "Lulus":
        st.success("🎉 Hasil Prediksi: Mahasiswa **LULUS**! 💖")
    else:
        st.error("❌ Hasil Prediksi: Mahasiswa **TIDAK LULUS** 💔")
