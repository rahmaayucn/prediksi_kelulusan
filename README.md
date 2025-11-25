# Sistem Pendukung Keputusan - Prediksi Kelulusan Mahasiswa

Metode: Classification menggunakan Decision Tree

## Input
- absensi
- nilai tugas
- nilai ujian

## Output
- Lulus
- Tidak

## Cara menjalankan

1. Aktifkan virtual environment
2. Install library:
   pip install -r requirements.txt
3. Latih model:
   python src/train.py
4. Jalankan API:
   python app.py