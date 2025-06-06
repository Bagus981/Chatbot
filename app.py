import streamlit as st
from PIL import Image
from datetime import datetime
import os
import json

# Konfigurasi halaman
st.set_page_config(page_title="Diagnosa Kerusakan Kendaraan", page_icon="💠", layout="centered")

# Path penyimpanan riwayat
data_folder = "riwayat_diagnosa"
os.makedirs(data_folder, exist_ok=True)

# === Kelas Kerusakan ===
class Kerusakan:
    def __init__(self, nama, jenis, gejala, solusi, gambar):
        self.nama = nama
        self.jenis = jenis
        self.gejala = gejala
        self.solusi = solusi
        self.gambar = gambar

    def cocok(self, input_gejala):
        cocok_gejala = sum(1 for g in input_gejala if g in self.gejala)
        return cocok_gejala / len(self.gejala) if cocok_gejala > 0 else 0

# === Data Kerusakan ===
data_kerusakan = [
    Kerusakan("Busi Rusak", "Motor", ["Mesin tidak nyala", "Susah starter", "Suara mesin tersendat"],
              "Ganti busi dan periksa kabel pengapian", "gambar/busi_rusak.jpeg"),
    Kerusakan("Aki Soak", "Motor", ["Starter elektrik mati", "Lampu redup"],
              "Isi ulang aki atau ganti aki baru", "gambar/aki_soak.jpeg"),
    Kerusakan("Karburator Kotor", "Motor", ["Mesin brebet", "Boros bensin"],
              "Bersihkan karburator", "gambar/karburator.jpeg"),
    Kerusakan("Filter Udara Kotor", "Motor", ["Tarikan berat", "Suara mesin ngos-ngosan"],
              "Bersihkan atau ganti filter udara", "gambar/filter_udara.jpeg"),
    Kerusakan("Rantai Kendor", "Motor", ["Suara berisik saat jalan", "Tarikan kasar"],
              "Kencangkan atau ganti rantai motor", "gambar/rantai.jpeg"),
    Kerusakan("Rem Aus", "Mobil", ["Rem kurang pakem", "Suara berdecit saat rem"],
              "Ganti kampas rem dan periksa sistem hidrolik", "gambar/rem_aus.jpeg"),
    Kerusakan("Radiator Bocor", "Mobil", ["Mobil cepat panas", "Air radiator cepat habis"],
              "Tambal atau ganti radiator", "gambar/radiator_bocor.jpeg"),
]

# === UI Utama ===
st.title(":wrench: Diagnosa Kerusakan Kendaraan")
st.markdown("Silakan pilih jenis kendaraan Anda terlebih dahulu.")

jenis_kendaraan = st.selectbox("Pilih kendaraan:", ["Motor", "Mobil"])
metode_input = st.radio("Metode Input Gejala:", ["Upload Audio/Video", "Input Manual"])

input_gejala = []

if metode_input == "Upload Audio/Video":
    uploaded_file = st.file_uploader("Upload file audio/video", type=["mp4", "mp3", "wav", "avi"])
    if uploaded_file:
        if 'video' in uploaded_file.type:
            st.video(uploaded_file)
        else:
            st.audio(uploaded_file)
        st.markdown("**Gejala Terdeteksi Otomatis (simulasi):**")
        if jenis_kendaraan == "Motor":
            input_gejala += ["Suara mesin tersendat", "Suara berisik saat jalan"]
        else:
            input_gejala += ["Rem kurang pakem", "Mobil cepat panas"]
        for g in input_gejala:
            st.write(f"- {g}")

elif metode_input == "Input Manual":
    st.write("### Input Manual Gejala")
    merk = st.text_input("Masukkan merk kendaraan Anda")
    transmisi = st.radio("Tipe transmisi:", ["Manual", "Otomatis"])
    semua_gejala = sorted({g for k in data_kerusakan if k.jenis == jenis_kendaraan for g in k.gejala})
    st.markdown("**Pilih gejala dari daftar berikut:**")
    for gejala in semua_gejala:
        if st.checkbox(gejala):
            input_gejala.append(gejala)
    st.markdown("**Tambahkan gejala lainnya jika tidak ada dalam daftar:**")
    gejala_tambahan = st.text_area("Gejala tambahan (pisahkan dengan koma)")
    if gejala_tambahan:
        input_gejala.extend([g.strip() for g in gejala_tambahan.split(",") if g.strip()])

if st.button(":mag: Diagnosa Sekarang"):
    if not input_gejala:
        st.warning("Silakan isi gejala terlebih dahulu.")
    else:
        hasil = [(k, k.cocok(input_gejala)) for k in data_kerusakan if k.jenis == jenis_kendaraan]
        hasil = sorted([h for h in hasil if h[1] > 0], key=lambda x: x[1], reverse=True)

        if hasil:
            nama_user = st.text_input("Nama Anda untuk menyimpan riwayat:", "User")
            st.markdown("### Hasil Diagnosa")
            for kerusakan, skor in hasil:
                st.subheader(f"Kemungkinan {int(skor * 100)}%: {kerusakan.nama}")
                st.image(kerusakan.gambar, caption=kerusakan.nama, use_column_width=True)
                st.success(f"Solusi: {kerusakan.solusi}")
                st.progress(skor)
                st.markdown("---")
            # Simpan ke riwayat
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            hasil_dict = {
                "nama": nama_user,
                "kendaraan": jenis_kendaraan,
                "gejala": input_gejala,
                "diagnosa": [r[0].nama for r in hasil],
                "waktu": timestamp
            }
            with open(os.path.join(data_folder, f"{nama_user}_{timestamp}.json"), "w") as f:
                json.dump(hasil_dict, f, indent=2)
            st.success(f"Riwayat diagnosa berhasil disimpan!")
        else:
            st.error("Gejala tidak cocok dengan database. Silakan konsultasi ke bengkel.")

# === Riwayat ===
with st.expander(":open_file_folder: Lihat Riwayat Diagnosa"):
    files = sorted([f for f in os.listdir(data_folder) if f.endswith(".json")], reverse=True)
    for file in files:
        with open(os.path.join(data_folder, file)) as f:
            data = json.load(f)
        st.markdown(f"**{data['waktu']} - {data['nama']}**")
        st.write(f"Kendaraan: {data['kendaraan']}")
        st.write(f"Gejala: {', '.join(data['gejala'])}")
        st.write(f"Diagnosa: {', '.join(data['diagnosa'])}")
        st.markdown("---")
