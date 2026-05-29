from deepface import DeepFace

try:
    result = DeepFace.verify(
        img1_path="foto_dari_hp/fotoku.jpg",
        img2_path="foto_dari_hp/contoh_wajah.jpg",
        model_name="Facenet",
        enforce_detection=False
    )
    if result['verified']:
        print("WAJAH SAMA")
    else:
        print("WAJAH BERBEDA")
    print(f"Jarak cosine: {result['distance']:.3f} (threshold: {result['threshold']})")
except Exception as e:
    print("Error:", e)
    print("Pastikan kedua file foto ada dan wajah terdeteksi.")