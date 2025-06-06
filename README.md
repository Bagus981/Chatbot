# Chatbot
# Final Project: Diagnosa Kerusakan Kendaraan

Aplikasi ini adalah sistem diagnosa kerusakan kendaraan (motor & mobil) berbasis Streamlit. User dapat memilih gejala secara manual atau upload audio/video, lalu aplikasi akan menampilkan kemungkinan kerusakan dan solusi.
Banyak pengguna kendaraan tidak memahami gejala kerusakan secara teknis. Aplikasi ini membantu pengguna mendiagnosa gejala umum pada kendaraan secara mandiri.

## Cara Menjalankan Aplikasi

1. **Aktifkan Virtual Environment (Jika Ada)**
   Jika menggunakan virtual environment bernama myenv, jalankan di PowerShell:
   ```
   .\myenv\Scripts\Activate.ps1
   ```

2. **Install Dependensi**
   Pastikan sudah install semua library yang dibutuhkan. Jalankan:
   ```
   pip install streamlit pillow
   ```
   Atau, jika tersedia file `requirements.txt`, cukup jalankan:
   ```
   pip install -r requirements.txt
   ```

3. **Pastikan Folder & File Gambar Tersedia**
   - Pastikan folder `gambar/` berisi file gambar yang dibutuhkan (misal: `busi_rusak.jpeg`, `aki_soak.jpeg`, dll).
   - Pastikan folder `riwayat_diagnosa/` ada (akan otomatis dibuat jika belum ada).

4. **Jalankan Aplikasi**
   Pindah ke folder project:
   ```
   cd "c:\Users\wwwba\Documents\Belajar coding\Bootcamp ai-python\Final_project"
   ```
   Lalu jalankan:
   ```
   streamlit run app.py
   ```

5. **Akses di Browser**
   Setelah perintah dijalankan, buka link yang muncul di terminal (misal: http://localhost:8501) untuk menggunakan aplikasi.

## Fitur
- Diagnosa kerusakan motor & mobil berdasarkan gejala
- Input gejala manual atau upload audio/video (simulasi)
- Solusi dan gambar kerusakan
- Simpan & lihat riwayat diagnosa

## Catatan Penting
- Pastikan koneksi internet aktif untuk download dependensi jika diperlukan
- Jika ada error library, pastikan sudah install semua dependensi di environment yang aktif
- Untuk upload file, parsing PDF belum didukung (hanya info file saja)
- Semua riwayat diagnosa akan tersimpan di folder `riwayat_diagnosa/` dalam format JSON

preview aplikasi ada di folder preview

---

Selamat menggunakan aplikasi diagnosa kerusakan kendaraan!