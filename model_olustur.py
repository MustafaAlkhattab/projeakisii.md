"""
model_olustur.py - Ornek Random Forest Modeli Olusturma Scripti

Bu script, Nihai_RandomForest_Modeli.pkl dosyasini olusturmak icin
sentetik (yapay) bir veri seti uzerinde Random Forest modeli egitir.

Kullanim:
    python model_olustur.py
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Rastgelelik sabit olsun ki her calistirmada ayni model uretilsin
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

N_ORNEK = 10_000    # Kac satir sentetik veri
N_OZELLIK = 30      # V1-V28 + Scaled_Time + Scaled_Amount
TEST_BOYUTU = 0.25

MODEL_PATH = "Nihai_RandomForest_Modeli.pkl"
FEATURE_NAMES = [f"V{i}" for i in range(1, 29)] + ["Scaled_Time", "Scaled_Amount"]

print(f"[INFO] {N_ORNEK} adet sentetik veri olusturuluyor...")

# Sentetik ozellikler (normal dagilim)
X = np.random.randn(N_ORNEK, N_OZELLIK)

# Gercekci etiketler olusturmak icin birkac ozellige dayali bir kural:
# - V1, V5, V10, V20, V25 ozelliklerinin belirli bir kombinasyonu
# - Scaled_Amount (son ozellik) yuksekse risk artar
islem_tutari = np.abs(X[:, -1]) * 100  # Scaled_Amount'dan tutar uret
risk_skoru = (
    0.3 * X[:, 0]    +   # V1
    0.2 * X[:, 4]    +   # V5
    0.15 * X[:, 9]   +   # V10
    0.2 * X[:, 19]   +   # V20
    0.1 * X[:, 24]   +   # V25
    0.05 * (islem_tutari - islem_tutari.mean()) / islem_tutari.std()
)

# Sigmoid benzeri bir olasilik
olasilik = 1 / (1 + np.exp(-risk_skoru))
y = (olasilik > 0.7).astype(int)

# Sinif dengesini kontrol et
fraud_orani = y.mean() * 100
print(f"[INFO] Dolandiricilik orani: %{fraud_orani:.1f} "
      f"({int(y.sum())} fraud / {int((1 - y).sum())} normal)")

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_BOYUTU, random_state=RANDOM_STATE, stratify=y
)

print("[INFO] Random Forest modeli egitiliyor...")
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=RANDOM_STATE,
    n_jobs=-1,
    class_weight="balanced",
    verbose=0
)

# Feature isimleriyle fit et (uyari gormemek icin)
X_train_df = pd.DataFrame(X_train, columns=FEATURE_NAMES)
model.fit(X_train_df, y_train)

# Degerlendirme
dogruluk = model.score(X_test, y_test)
print(f"[INFO] Test dogrulugu: %{dogruluk*100:.2f}")

# Modeli kaydet
joblib.dump(model, MODEL_PATH)
print(f"[OK] Model basariyla kaydedildi: {MODEL_PATH}")

# Feature isimlerini modele ek bilgi olarak sakla
model_metadata = {
    "model": model,
    "feature_names": FEATURE_NAMES,
    "accuracy": round(dogruluk, 4),
}
joblib.dump(model_metadata, MODEL_PATH.replace(".pkl", "_with_meta.pkl"))
print(f"[OK] Metadata'li model de kaydedildi: "
      f"{MODEL_PATH.replace('.pkl', '_with_meta.pkl')}")

print("\n[Hazir] Streamlit uygulamasini baslatabilirsiniz:")
print("    streamlit run app.py")
