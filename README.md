![Python](https://img.shields.io/badge/Python-3.11-blue)
![DeepFace](https://img.shields.io/badge/DeepFace-FaceNet-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Selesai-brightgreen)

# 📸 Face Recognition System - Smartphone to PC

Sistem pengenalan wajah yang menerima foto dari **smartphone**, memprosesnya di **PC**, dan menghasilkan laporan identifikasi dalam format **Excel**.

---

## 📌 Tentang Proyek

Proyek ini dibuat sebagai tugas akhir jurusan **PPLG (Pengembangan Perangkat Lunak dan Gim)**. Tujuannya adalah membangun sistem yang dapat:

- ✅ Menerima foto wajah dari smartphone
- ✅ Memproses banyak foto sekaligus (batch processing)
- ✅ Membandingkan wajah dengan foto referensi menggunakan **FaceNet**
- ✅ Menghasilkan laporan dalam format **JSON** dan **Excel**

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| **Python 3.11** | Bahasa pemrograman utama |
| **DeepFace** | Library face recognition |
| **FaceNet** | Model deep learning untuk pengenalan wajah |
| **OpenCV** | Pemrosesan gambar |
| **Pandas & Openpyxl** | Ekspor hasil ke Excel |
| **VSCode** | Editor kode |

---

## 📱 Alur Sistem
📱 Smartphone (ambil foto)
↓
💻 Transfer ke PC (USB/Cloud/Email)
↓
📁 Folder "foto_dari_hp"
↓
🐍 Jalankan deteksi_dari_hp.py
↓
🤖 DeepFace + FaceNet

Deteksi wajah

Bandingkan dengan foto referensi

Hitung jarak cosine
↓
📊 Hasil: DIKENAL / TIDAK DIKENAL
↓
💾 Simpan ke hasil_deteksi.json
↓
📎 Export ke hasil_deteksi.xlsx
↓
✅ Selesai

---

## 📊 Hasil Pengujian

| File | Status | Jarak Cosine |
|------|--------|---------------|
| contoh1.jpg | DIKENAL | 0.0000 |
| contoh1_variasi.jpg | DIKENAL | 0.1523 |
| contoh2.jpg | TIDAK DIKENAL | 0.7234 |

> **Catatan:** Jarak cosine < 0.4 = wajah sama, > 0.6 = wajah berbeda.  
> Foto contoh menggunakan wajah generatif AI dari [ThisPersonDoesNotExist.com](https://thispersondoesnotexist.com) untuk menjaga privasi.

---

## 🚀 Cara Menjalankan Proyek

### 1. Clone repository ini
```bash
git clone https://github.com/[username-anda]/FaceRecognition-Portfolio.git
cd FaceRecognition-Portfolio
