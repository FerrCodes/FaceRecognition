import os
import sys
import tempfile
from PIL import Image
import streamlit as st

# Pastikan OpenCV bisa jalan
try:
    import cv2
except ImportError:
    os.system("pip install opencv-python-headless==4.10.0.84")
    import cv2

from deepface import DeepFace

# Konfigurasi halaman
st.set_page_config(page_title="Face Recognition", page_icon="📸")
st.title("📸 Face Recognition - Upload Foto")

# Path referensi
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REFERENCE_IMAGE = os.path.join(BASE_DIR, "foto_dari_hp", "contoh1.jpg")

# Upload foto
uploaded_file = st.file_uploader("Pilih foto wajah (jpg/jpeg/png)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Simpan file sementara
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Tampilkan foto
    image = Image.open(uploaded_file)
    st.image(image, caption="Foto yang diupload", width=300)

    # Proses deteksi
    with st.spinner("Memproses wajah..."):
        try:
            result = DeepFace.verify(
                img1_path=REFERENCE_IMAGE,
                img2_path=tmp_path,
                model_name="Facenet",
                enforce_detection=False
            )

            jarak = result['distance']
            if result['verified']:
                st.success(f"✅ WAJAH DIKENAL! (Jarak cosine: {jarak:.4f})")
            else:
                st.error(f"❌ WAJAH TIDAK DIKENAL (Jarak cosine: {jarak:.4f})")
        except Exception as e:
            st.error(f"Error: {e}")

    # Hapus file sementara
    os.unlink(tmp_path)
else:
    st.info("📤 Upload foto wajah untuk memulai deteksi.")