import os
import json
from deepface import DeepFace
from datetime import datetime

def deteksi_dari_hp():
    FOLDER_FOTO = "foto_dari_hp"
    HASIL_FILE = "hasil_deteksi.json"
    REFERENCE_FACE = os.path.join(FOLDER_FOTO, "contoh1.jpg")

    # Buat folder jika belum ada
    if not os.path.exists(FOLDER_FOTO):
        os.makedirs(FOLDER_FOTO)
        print(f"Folder '{FOLDER_FOTO}' telah dibuat. Silakan letakkan foto di sini.")
        return

    if not os.path.exists(REFERENCE_FACE):
        print(f"File referensi '{REFERENCE_FACE}' tidak ditemukan. Letakkan 'fotoku.jpg' di folder '{FOLDER_FOTO}'.")
        return

    # Cek file gambar
    extensions = ('.jpg', '.jpeg', '.png')
    files = [f for f in os.listdir(FOLDER_FOTO) if f.lower().endswith(extensions)]

    if not files:
        print(f"Tidak ada file foto di folder '{FOLDER_FOTO}'. Letakkan foto dari HP.")
        return

    print(f"Menemukan {len(files)} foto. Memproses...\n")
    results = []

    for file in files:
        full_path = os.path.join(FOLDER_FOTO, file)
        try:
            result = DeepFace.verify(
                img1_path=REFERENCE_FACE,
                img2_path=full_path,
                model_name="Facenet512",
                enforce_detection=False
            )
            status = "DIKENAL" if result["verified"] else "TIDAK DIKENAL"
            distance = result["distance"]
        except Exception as e:
            status = "ERROR"
            distance = None
            print(f"Error pada {file}: {e}")

        hasil_entry = {
            "file": file,
            "status": status,
            "jarak_cosine": distance,
            "waktu": datetime.now().isoformat()
        }
        results.append(hasil_entry)

        if distance is not None:
            print(f"{file}: {status} (jarak={distance:.4f})")
        else:
            print(f"{file}: {status}")

    # Simpan hasil ke JSON
    with open(HASIL_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print(f"\n✅ Selesai. Hasil disimpan di {HASIL_FILE}")

if __name__ == "__main__":
    deteksi_dari_hp()