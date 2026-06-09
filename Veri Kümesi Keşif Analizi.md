## **Veri Kümesi Keşif Analizi (EDA) Planı** 

**Hazırlayan:** Ahmed (Proje Yöneticisi ve Veri Sorumlusu) **Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti **Tarih:** 30 Nisan 2026 

## **1. Giriş ve Analizin Amacı** 

Bu belgenin amacı, kredi kartı dolandırıcılığı tespiti projesinde kullanılacak veri setinin derinlemesine anlaşılması için uygulanacak Keşif Veri Analizi (Exploratory Data Analysis - EDA) adımlarını planlamaktır. Analizin temel hedefi; verinin yapısını anlamak, olası veri kalitesi sorunlarını (eksik veya aykırı değerler) tespit etmek ve makine öğrenimi modellemesi öncesinde değişkenler arasındaki gizli ilişkileri ortaya çıkarmaktır. 

## **2. Veri Yapısı ve Temel İnceleme** 

Veri seti projeye dahil edildikten sonra ilk olarak aşağıdaki yapısal incelemeler gerçekleştirilecektir: 

- **Veri Boyutu ve Tipleri:** Veri setindeki satır (gözlem) ve sütun (öznitelik) sayılarının belirlenmesi, değişkenlerin veri tiplerinin (sayısal, kategorik, tarih vb.) kontrol edilmesi. 

- **Eksik Değer (Missing Value) Kontrolü:** Her bir sütundaki eksik veri miktarının tespit edilmesi ve bu eksikliklerin rastgele mi yoksa sistematik bir modele mi sahip olduğunun incelenmesi. 

- **Genel İstatistikler:** Veri setinin genel bir özetini almak için `describe()` fonksiyonu ile minimum, maksimum, çeyreklik (quartile) değerleri gibi temel istatistiksel özetlerin çıkarılması. 

## **3. İstatistiksel Yöntemler ve Analizler** 

Verinin eğilimini ve dağılımını matematiksel olarak ifade etmek için şu istatistiksel yöntemler kullanılacaktır: 

- **Merkezi Eğilim ve Yayılım Ölçüleri:** Özellikle "Amount" (İşlem Tutarı) ve "Time" (Zaman) değişkenleri için ortalama (mean), medyan (median), standart sapma (standard deviation) ve varyans değerlerinin hesaplanması. 

- **Korelasyon Analizi:** Tüm bağımsız değişkenlerin (V1-V28, Time, Amount) birbirleriyle ve özellikle hedef değişken olan "Class" (Dolandırıcı/Güvenli) ile olan ilişkisini ölçmek için **Korelasyon Matrisi (Correlation Matrix)** oluşturulacaktır. Bu sayede, tahmine en çok katkı sağlayacak özellikler veya çoklu doğrusal bağlantı (multicollinearity) sorunları tespit edilecektir. 

## **4. Veri Görselleştirme Stratejisi** 

İstatistiksel bulguları desteklemek ve görsel olarak yorumlanabilir hale getirmek için çeşitli grafik türlerinden yararlanılacaktır: 

- **Sınıf Dağılımı (Bar Plot / Pie Chart):** Hedef değişkenin (Class) dağılımı görselleştirilerek veri setindeki dengesizlik (imbalanced data) oranı net bir şekilde ortaya konacaktır. 

- **Sayısal Değişken Dağılımları (Histogramlar ve Yoğunluk Grafikleri):** "Time" ve "Amount" gibi değişkenlerin dağılım şekillerinin (normal dağılım, çarpıklık) incelenmesi için histogramlar çizilecektir. 

- **Aykırı Değer Tespiti (Kutu Grafikleri - Box Plots):** Normal işlemler ile dolandırıcılık işlemleri arasındaki tutar (Amount) farklılıklarını ve uç değerleri (outliers) gözlemlemek için kutu grafikleri kullanılacaktır. 

- **Değişken İlişkileri (Dağılım Grafikleri - Scatter Plots):** Korelasyonu yüksek çıkan belirli değişken çiftlerinin birbiriyle olan etkileşimini ve kümelerini incelemek amacıyla dağılım grafikleri oluşturulacaktır. 

## **5. Beklenen Çıktılar ve Modellemeye Etkisi** 

Bu EDA planının uygulanması sonucunda; verinin temizlenme stratejisi netleşecek, ölçeklendirme (scaling) ihtiyacı belirlenecek ve veri dengesizliği problemi sayısal kanıtlarla ortaya konularak SMOTE gibi tekniklerin kullanımına bilimsel bir zemin hazırlanacaktır. 

