

Detaylı Proje Dokümantasyonu ve
## Kullanım Kılavuzu
Proje: Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI)
## 1. Dokümantasyonun Amacı
Bu belge, projenin teknik altyapısını, kullanılan teknolojileri, dosya mimarisini ve
sistemin yerel (local) bir bilgisayarda nasıl kurulup çalıştırılacağını adım adım
açıklayan teknik bir kılavuzdur.
- Kullanılan Teknolojiler ve Kütüphaneler
Projenin geliştirilmesi ve çalıştırılması için aşağıdaki teknolojiler kullanılmıştır:
##  Programlama Dili: Python 3.8+
 Veri İşleme ve Analiz: pandas, numpy
 Makine Öğrenimi ve Modelleme: scikit-learn (Model eğitimi),
imbalanced-learn (SMOTE ile veri dengeleme)
 Model Kayıt ve Yükleme: joblib veya pickle
 Web Sunucusu ve API: Flask
 Kullanıcı Arayüzü (Frontend): HTML5, CSS3, Bootstrap
- Proje Dosya ve Klasör Mimarisi
Projenin GitHub deposundaki (repository) standart dosya yapısı aşağıdaki gibidir:
## Plaintext
Fraud_Shield_AI/
## │
├── verisetleri/
│   └── creditcard.csv                 # Orijinal Kaggle veri seti
(Boyutu nedeniyle GitHub'a eklenmeyebilir)
## │
├── notebooks/
│   └── Veri_On_Isleme_ve_Model.ipynb  # Veri temizleme, SMOTE ve
model eğitim kodları
## │
├── modeller/
│   └── Nihai_RandomForest_Modeli.pkl  # Eğitilmiş ve dışa aktarılmış
yapay zeka modeli
## │
├── templates/
│   └── index.html                     # Web arayüzünün görsel
kodları
## │
├── app.py                             # Flask web sunucusunu ve
API'yi çalıştıran ana kod
└── requirements.txt                   # Proje için gerekli Python
kütüphanelerinin listesi

- Kurulum ve Çalıştırma Talimatları
Sistemi kendi bilgisayarınızda çalıştırmak için terminal (komut satırı) üzerinden
aşağıdaki adımları izleyiniz:
Adım 1: Gerekli Kütüphanelerin Yüklenmesi Proje dizinine terminal ile gidip
aşağıdaki komutu çalıştırarak tüm bağımlılıkları yükleyin:
## Bash
pip install pandas numpy scikit-learn flask imbalanced-learn
(Eğer requirements.txt dosyası varsa: pip install -r requirements.txt)
Adım 2: Flask Sunucusunun Başlatılması Gerekli kütüphaneler yüklendikten sonra
ana uygulamayı başlatın:
## Bash
python app.py
Adım 3: Arayüze Erişim Terminalde sunucunun başarıyla çalıştığına dair bir mesaj
göreceksiniz. Web tarayıcınızı açıp adres çubuğuna şu adresi girin:
## [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
## 5. Sistemin Kullanım Senaryosu
- Kullanıcı tarayıcı üzerinden sisteme erişir.
- Ekranda yer alan forma, test edilmek istenen kredi kartı işleminin
özniteliklerini (örneğin işlem tutarı ve ilgili V özelliklerini) girer.
- "Analiz Et" butonuna tıklandığında, arka planda çalışan app.py bu verileri
alır, standartlaştırma (scaling) işlemlerinden geçirir ve
Nihai_RandomForest_Modeli.pkl dosyasına gönderir.
- Model saniyeler içinde olasılık hesaplaması yapar ve sonucu arayüze
döndürür: "Güvenli İşlem" (Yeşil) veya "Dolandırıcılık Şüphesi!"
(Kırmızı).
