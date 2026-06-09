

Eksiklerin Giderilmesi ve İyileştirmeler
## Raporu
Proje: Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI)
## 1. Raporun Amacı
Bu rapor, projenin geliştirme, test ve entegrasyon aşamalarında karşılaşılan teknik
sorunları, bu sorunların ekibimiz tarafından nasıl çözüldüğünü ve sistemin
performansını artırmak için yapılan son iyileştirmeleri belgelemektedir.
## 2. Karşılaşılan Temel Sorun: "%0 Dolandırıcılık
Tespit Hatası" ve Çözümü
Sorun (Bug): Model geliştirme aşamasının başlarında, temel bir algoritma eğitilip
test edildiğinde dolandırıcılık vakalarını (Class 1) yakalama oranının (Recall) %0
olduğu gözlemlenmiştir. Yani model, tüm işlemlere istisnasız "Güvenli (Normal)"
etiketi basmaktaydı. Toplam doğruluk (Accuracy) %99.8 görünmesine rağmen, asıl
amacımız olan dolandırıcıları yakalama konusunda model tamamen başarısızdı.
Kök Neden Analizi (Root Cause Analysis): Ekibimiz hatayı analiz ettiğinde sorunun
kodlama mantığından değil, "Aşırı Veri Dengesizliği" (Extreme Class Imbalance)
probleminden kaynaklandığını tespit etmiştir. 284 bin normal işleme karşılık sadece
492 dolandırıcılık işlemi olduğu için, model kolaya kaçarak (çoğunluk sınıfını
ezberleyerek) kendini optimize etmişti.
## Uygulanan Çözüm:
- Veri setine imbalanced-learn kütüphanesinden SMOTE (Sentetik Azınlık
Aşırı Örnekleme) tekniği uygulandı.
- Eğitim veri setindeki dolandırıcılık işlemleri sentetik olarak üretilerek sınıflar
%50-%50 (227.451 / 227.451) oranında eşitlendi.
- Model bu yeni dengeli veri setiyle yeniden eğitildiğinde %0 olan tespit oranı
%80.61 seviyesine başarıyla yükseltildi.
- Web Arayüzü ve Entegrasyon İyileştirmeleri (API
## Fixes)
Sorun: Flask API (web sunucusu) ile arayüz bağlandığında, kullanıcının ekrandan
girdiği manuel değerler model tarafından yanlış yorumlanıyor ve hatalı risk skorları
üretiyordu.
Çözüm: * Canlı arayüzden gelen verilerin, modelin eğitim aşamasında gördüğü veri
formatından farklı olduğu (ölçeklendirilmediği) fark edildi.

 Arka plana (backend) bir ön işleme (pre-processing) katmanı eklendi.
Kullanıcının arayüzden girdiği "Tutar" (Amount) ve "Zaman" (Time) gibi
değerler, tahmin yapılmadan hemen önce StandardScaler kullanılarak arka
planda otomatik olarak ölçeklendirildi. Bu iyileştirme ile API'nin doğru
sonuçlar döndürmesi sağlandı.
## 4. Sonuç
Karşılaşılan kritik hatalar (%0 tespit sorunu ve API ölçeklendirme uyumsuzluğu)
bilimsel yöntemlerle analiz edilip çözülmüş, sistem %100 çalışır ve sunuma hazır hale
getirilmiştir. Projede şu an bilinen herhangi bir majör hata (bug) bulunmamaktadır.
