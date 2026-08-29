import streamlit as st
from deepface import DeepFace
import tempfile
import os
from PIL import Image

st.set_page_config(page_title="Face Recognition", page_icon="📸")
st.title("📸 Face Recognition - Upload Foto")

# Foto referensi (pastikan file ini ada di folder foto_dari_hp)
REFERENCE_IMAGE = "foto_dari_hp/contoh1.jpg"

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