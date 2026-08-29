![Python](https://img.shields.io/badge/Python-3.11-blue)
![DeepFace](https://img.shields.io/badge/DeepFace-FaceNet-green)
![Status](https://img.shields.io/badge/Status-Selesai-brightgreen)

# Face Recognition System - Smartphone to PC

Sistem pengenalan wajah berbasis web yang menerima foto dari **smartphone**, memprosesnya secara **online**, dan menghasilkan laporan dalam format **Excel**.

---

## Tentang Proyek

Proyek ini adalah sistem **pengenalan wajah** yang membandingkan foto yang diupload dengan satu **foto referensi**. Aplikasi ini memiliki dua mode:

| Mode | Fungsi |
|------|--------|
| **Single Upload** | Upload satu foto → hasil langsung |
| **Batch Upload & Export** | Upload banyak foto → proses semua → download Excel |

---

## Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| **Python 3.11** | Bahasa pemrograman utama |
| **DeepFace** | Library face recognition |
| **FaceNet** | Model deep learning untuk pengenalan wajah |
| **Streamlit** | Framework web untuk antarmuka |
| **Pandas & Openpyxl** | Ekspor hasil ke Excel |
| **OpenCV** | Pemrosesan gambar |

---

## 📱 Alur Sistem

```
📱 Smartphone (ambil foto)
        ↓
💻 Transfer ke PC (USB / Cloud / Email)
        ↓
📁 Masukkan ke folder "foto_dari_hp"
        ↓
🐍 Jalankan: python deteksi_dari_hp.py
        ↓
🤖 DeepFace + FaceNet512
   ├─ Deteksi wajah dalam foto
   ├─ Bandingkan dengan foto referensi (contoh1.jpg)
   └─ Hitung jarak cosine
        ↓
📊 Hasil: DIKENAL / TIDAK DIKENAL
        ↓
💾 Simpan ke hasil_deteksi.json
        ↓
📎 Jalankan: python to_Excel.py
        ↓
📊 Export ke hasil_deteksi.xlsx
        ↓
✅ Selesai
```

---

## Fitur Aplikasi

### 1. Single Upload
- Upload satu foto wajah
- Hasil langsung: DIKENAL atau TIDAK DIKENAL
- Tampilkan jarak cosine

### 2. Batch Upload & Export
- Upload banyak foto sekaligus
- Proses semua foto dengan progress bar
- Tampilkan tabel hasil di web
- **Download hasil dalam format Excel**

---

## Contoh Hasil Pengujian

| File | Status | Jarak Cosine |
|------|--------|---------------|
| contoh1.jpg | DIKENAL | 0.0000 |
| contoh1_variasi.jpg | DIKENAL | 0.1523 |
| contoh2.jpg | TIDAK DIKENAL | 0.7234 |

> **Catatan:** Jarak cosine < 0.4 = wajah sama, > 0.6 = wajah berbeda.  
> Foto contoh menggunakan wajah generatif AI dari [ThisPersonDoesNotExist.com](https://thispersondoesnotexist.com) untuk menjaga privasi.

---

## Struktur Folder
```
FaceRecognition/
├── app_streamlit.py          # Aplikasi web utama
├── deteksi_dari_hp.py        # Script deteksi batch (terminal)
├── to_excel.py               # Export ke Excel
├── requirements.txt          # Daftar library
├── README.md                 # Dokumentasi
├── foto_dari_hp/             # Folder foto contoh
│   ├── contoh1.jpg           # Foto referensi
│   └── contoh2.jpg           # Foto uji coba
├── hasil_deteksi.json        # Hasil deteksi (JSON)
└── hasil_deteksi.xlsx        # Laporan Excel
```
---

## 🎯 Pengembangan ke Depan
- Menambahkan database banyak orang (lebih dari satu referensi)
- Membuat REST API dengan Flask
- Real-time detection menggunakan webcam
- Menambahkan grafik hasil di Excel

---

## Pengembang
- Feri Ferdianto
-Kelas XI PPLG 3 - [SMKN 5 Malang]
- Proyek Tugas Akhir Jurusan - Semester Akhir

Email: [ferdiantoferi1303@gmail.com]
