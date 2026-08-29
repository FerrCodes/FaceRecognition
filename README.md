![Python](https://img.shields.io/badge/Python-3.11-blue)
![DeepFace](https://img.shields.io/badge/DeepFace-FaceNet-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Selesai-brightgreen)

# 📸 Face Recognition System — Smartphone to PC

Sistem pengenalan wajah yang menerima foto dari **smartphone**, memprosesnya di **PC**, dan menghasilkan laporan identifikasi dalam format **JSON** dan **Excel**.

---

## 📌 Tentang Proyek

Proyek ini dibuat sebagai **Tugas Akhir** jurusan **PPLG (Pengembangan Perangkat Lunak dan Gim)**. Tujuannya adalah membangun sistem yang dapat:

- ✅ Menerima foto wajah dari smartphone
- ✅ Memproses banyak foto sekaligus (*batch processing*)
- ✅ Membandingkan wajah dengan foto referensi menggunakan **FaceNet512**
- ✅ Menghasilkan laporan dalam format **JSON** dan **Excel**

---

## 🛠️ Teknologi yang Digunakan

| Teknologi             | Fungsi                                     |
| --------------------- | ------------------------------------------ |
| **Python 3.11**       | Bahasa pemrograman utama                   |
| **DeepFace**          | Library face recognition                   |
| **FaceNet512**        | Model deep learning untuk pengenalan wajah |
| **OpenCV**            | Pemrosesan gambar                          |
| **Pandas & Openpyxl** | Ekspor hasil ke Excel                      |
| **VSCode**            | Editor kode                                |

---

## 📁 Struktur Proyek

```
FaceRecognition-Final/
│
├── foto_dari_hp/           # Folder untuk menyimpan foto dari smartphone
│   ├── contoh1.jpg         # Foto referensi utama (wajah yang dikenal)
│   ├── contoh1_variasi.jpg # Variasi foto wajah yang sama
│   └── contoh2.jpg         # Foto wajah berbeda (tidak dikenal)
│
├── deteksi_dari_hp.py      # Script utama — deteksi & verifikasi wajah
├── to_Excel.py             # Script ekspor hasil JSON ke Excel
├── coba_wajah.py           # Script percobaan awal
├── test.py                 # Script pengujian
├── hasil_deteksi.json      # Output hasil deteksi (format JSON)
└── hasil_deteksi_dengan_foto.xlsx  # Output laporan (format Excel)
```

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

## 🚀 Cara Menjalankan Proyek

### 1. Clone repository ini

```bash
git clone https://github.com/Ferr-Hanni/FaceRecognition-Final.git
cd FaceRecognition-Final
```

### 2. Install dependensi yang dibutuhkan

```bash
pip install deepface opencv-python pandas openpyxl
```

> **Catatan:** DeepFace akan otomatis mengunduh model FaceNet512 saat pertama kali dijalankan. Pastikan koneksi internet tersedia.

### 3. Siapkan foto referensi

Letakkan foto wajah referensi (wajah yang ingin dikenali) di dalam folder `foto_dari_hp/` dengan nama `contoh1.jpg`.

```
foto_dari_hp/
└── contoh1.jpg   ← foto referensi kamu
```

### 4. Masukkan foto dari HP

Pindahkan foto-foto dari smartphone (via USB, Google Drive, WhatsApp, dll.) ke dalam folder `foto_dari_hp/`. Format yang didukung: `.jpg`, `.jpeg`, `.png`.

### 5. Jalankan deteksi wajah

```bash
python deteksi_dari_hp.py
```

Contoh output di terminal:
```
Menemukan 3 foto. Memproses...

contoh1.jpg: DIKENAL (jarak=0.0000)
contoh1_variasi.jpg: DIKENAL (jarak=0.1523)
contoh2.jpg: TIDAK DIKENAL (jarak=0.7234)

✅ Selesai. Hasil disimpan di hasil_deteksi.json
```

### 6. Export hasil ke Excel

```bash
python to_Excel.py
```

File `hasil_deteksi_dengan_foto.xlsx` akan dibuat secara otomatis.

---

## 📊 Hasil Pengujian

| File                  | Status        | Jarak Cosine |
| --------------------- | ------------- | ------------ |
| contoh1.jpg           | DIKENAL       | 0.0000       |
| contoh1\_variasi.jpg  | DIKENAL       | 0.1523       |
| contoh2.jpg           | TIDAK DIKENAL | 0.7234       |

> **Catatan Threshold:**
> - Jarak cosine **< 0.4** → wajah dianggap **sama (DIKENAL)**
> - Jarak cosine **> 0.6** → wajah dianggap **berbeda (TIDAK DIKENAL)**
>
> Foto contoh menggunakan wajah generatif AI dari [ThisPersonDoesNotExist.com](https://thispersondoesnotexist.com) untuk menjaga privasi.

---

## ⚙️ Cara Kerja Deteksi

Script `deteksi_dari_hp.py` bekerja dengan langkah-langkah berikut:

1. **Membaca folder** `foto_dari_hp/` dan mengumpulkan semua file gambar (`.jpg`, `.jpeg`, `.png`).
2. **Menggunakan `DeepFace.verify()`** dengan model `Facenet512` untuk membandingkan setiap foto dengan foto referensi (`contoh1.jpg`).
3. **Menghitung jarak cosine** antara dua embedding wajah. Semakin kecil jaraknya, semakin mirip wajahnya.
4. **Menentukan status** wajah: `DIKENAL` atau `TIDAK DIKENAL` berdasarkan nilai threshold bawaan DeepFace.
5. **Menyimpan seluruh hasil** ke file `hasil_deteksi.json` lengkap dengan timestamp.

---

## 🐛 Troubleshooting

| Masalah | Solusi |
|---|---|
| `ModuleNotFoundError: deepface` | Jalankan `pip install deepface` |
| File referensi tidak ditemukan | Pastikan `contoh1.jpg` ada di folder `foto_dari_hp/` |
| Model FaceNet512 gagal diunduh | Periksa koneksi internet, lalu coba lagi |
| Foto tidak terdeteksi wajah | Pastikan foto cukup terang dan wajah terlihat jelas |
| Error saat export Excel | Jalankan `pip install openpyxl` |

---

## 📝 Lisensi

Proyek ini menggunakan lisensi **MIT** — bebas digunakan dan dimodifikasi untuk keperluan pembelajaran.

---

## 👤 Pembuat

**Feri-Ferdianto**
Tugas Akhir — Jurusan PPLG (Pengembangan Perangkat Lunak dan Gim)

---

> 💡 *Proyek ini dibuat untuk keperluan pendidikan dan demonstrasi teknologi face recognition berbasis deep learning.*
