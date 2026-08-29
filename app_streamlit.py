import streamlit as st
import tempfile
import os
import pandas as pd
from PIL import Image
from datetime import datetime
import json

st.set_page_config(page_title="Face Recognition")
st.title("Sistem Pengenalan Wajah")

# ==================== DESKRIPSI PROYEK ====================
with st.expander("Tentang Projek Ini", expanded=True):
    st.markdown("""
    •  Apa itu Face Recognition?
    Aplikasi ini adalah sistem pengenalan wajah yang membandingkan foto yang diupload dengan satu foto referensi.
    
    •  Informasi untuk projek ini
    Sementara UI/UX seperti ini dan Fitur juga dua mode untuk mendeteksi foto setelah diupload, karena lebih fokus pada 
    perbaikan pada Sistem proses mendeteksi Foto dan baris Kode yang sedang diuji coba.

### Pengembang:
Feri Ferdianto 
Kelas XI PPLG 3 - Tugas Akhir Jurusan
""")
# ==========================================================

# --- SIDEBAR: Pilih Mode ---
mode = st.sidebar.radio("Pilih Mode:", ["Single Upload", "Batch Upload & Export"])

# Foto referensi
REFERENCE_IMAGE = "foto_dari_hp/contoh1.jpg"

# --- FUNGSI DETEKSI ---
def detect_face(image_path, reference_path=REFERENCE_IMAGE):
    try:
        from deepface import DeepFace
        result = DeepFace.verify(
            img1_path=reference_path,
            img2_path=image_path,
            model_name="Facenet",
            enforce_detection=False
        )
        return result['verified'], result['distance']
    except Exception as e:
        return None, None

# --- MODE 1: SINGLE UPLOAD ---
if mode == "Single Upload":
    st.subheader("Upload satu foto untuk deteksi")
    
    uploaded_file = st.file_uploader("Pilih foto wajah dengan format: JPG, JPEG, PNG", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        
        image = Image.open(uploaded_file)
        st.image(image, caption="Foto yang diupload", width=300)
        
        with st.spinner("Memproses wajah..."):
            verified, distance = detect_face(tmp_path)
            
            if verified is None:
                st.error("❌ Gagal memproses foto. Pastikan ada wajah yang terdeteksi.")
            elif verified:
                st.success(f"✅ WAJAH DIKENAL! (Jarak cosine: {distance:.4f})")
            else:
                st.error(f"❌ WAJAH TIDAK DIKENAL (Jarak cosine: {distance:.4f})")
        
        os.unlink(tmp_path)

# --- MODE 2: BATCH UPLOAD + EXPORT EXCEL ---
else:
    st.subheader("Upload banyak foto sekaligus")
    st.info("Pilih beberapa foto, lalu klik tombol 'Proses Semua'")
    
    uploaded_files = st.file_uploader(
        "Pilih beberapa format foto JPG, JPEG, PNG", 
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )
    
    if uploaded_files:
        st.write(f"{len(uploaded_files)} foto siap diproses")
        
        if st.button("Proses Semua Foto"):
            results = []
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, file in enumerate(uploaded_files):
                status_text.text(f"Memproses {file.name}... ({i+1}/{len(uploaded_files)})")
                
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                    tmp_file.write(file.read())
                    tmp_path = tmp_file.name
                
                verified, distance = detect_face(tmp_path)
                
                if verified is None:
                    status_deteksi = "ERROR"
                    jarak = None
                elif verified:
                    status_deteksi = "DIKENAL"
                    jarak = distance
                else:
                    status_deteksi = "TIDAK DIKENAL"
                    jarak = distance
                
                results.append({
                    "File": file.name,
                    "Status": status_deteksi,
                    "Jarak Cosine": jarak,
                    "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                
                os.unlink(tmp_path)
                progress_bar.progress((i + 1) / len(uploaded_files))
            
            status_text.text("✅ Selesai!")
            
            # Tampilkan hasil dalam tabel
            df = pd.DataFrame(results)
            st.subheader("Hasil Deteksi")
            st.dataframe(df, use_container_width=True)
            
            # Tombol download Excel
            excel_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
            df.to_excel(excel_file.name, index=False)
            
            with open(excel_file.name, "rb") as f:
                st.download_button(
                    label="Download Hasil (Excel)",
                    data=f,
                    file_name="hasil_deteksi.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            
            os.unlink(excel_file.name)
            
            # Tampilkan ringkasan
            st.success(f"✅ {len(results)} foto diproses. {df[df['Status']=='DIKENAL'].shape[0]} dikenali, {df[df['Status']=='TIDAK DIKENAL'].shape[0]} tidak dikenali.")