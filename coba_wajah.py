from deepface import DeepFace

# 1. Bandingkan dua foto (apakah orang yang sama)?
print("=== Uji 1: Apakah dua foto ini orang yang sama? ===")
try:
    result = DeepFace.verify(
        img1_path="foto_dari_hp/fotoku.jpg",
        img2_path="foto_dari_hp/contoh_wajah.jpg",
        model_name="Facenet",
        enforce_detection=False
    )
    if result['verified']:
        print("✅ HASIL: SAMA (foto adalah orang yang sama)")
    else:
        print("❌ HASIL: BERBEDA (bukan orang yang sama)")
    print(f"Jarak cosine: {result['distance']:.4f}")
except Exception as e:
    print("Error pada Uji 1:", e)

# 2. Bandingkan dengan foto orang lain (jika ada)
print("\n=== Uji 2: Bandingkan dengan foto orang lain ===")
try:
    result2 = DeepFace.verify(
        img1_path="foto_dari_hp/fotoku.jpg",
        img2_path="foto_dari_hp/orang_lain.jpg",
        model_name="Facenet",
        enforce_detection=False
    )
    if result2['verified']:
        print("⚠️ HASIL: SAMA (padahal seharusnya beda) – cek foto orang_lain.jpg")
    else:
        print("✅ HASIL: BERBEDA (sesuai harapan, orang berbeda)")
except Exception as e:
    print("Error pada Uji 2:", e)
    print("(Jika tidak punya foto orang_lain.jpg, abaikan)")

# 3. Analisis wajah (usia, gender, emosi)
print("\n=== Uji 3: Analisis wajah pada fotoku.jpg ===")
try:
    obj = DeepFace.analyze(
        img_path="foto_dari_hp/fotoku.jpg",
        actions=["age", "gender", "emotion"],
        enforce_detection=False
    )
    print(f"Usia perkiraan: {obj[0]['age']} tahun")
    print(f"Gender: {obj[0]['gender']} (tertinggi: {obj[0]['dominant_gender']})")
    print(f"Emosi dominan: {obj[0]['dominant_emotion']}")
except Exception as e:
    print("Error pada Uji 3:", e)