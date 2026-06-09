

## Proje Sonuçlarının Konsolidasyonu
## Raporu
Proje: Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI)
## 1. Raporun Amacı
Bu rapor, 6 haftalık proje geliştirme süreci boyunca elde edilen tüm teknik,
operasyonel ve analitik sonuçları tek bir belgede birleştirmeyi (konsolide etmeyi)
amaçlamaktadır. Veri hazırlığından başlayarak, modelin son arayüz entegrasyonuna
kadar elde edilen bulgular nihai proje başarısını kanıtlamak üzere özetlenmiştir.
- Veri Ön İşleme ve Dengeleme Sonuçları
Projenin en kritik zorluklarından biri olan "aşırı sınıf dengesizliği" başarıyla
çözülmüştür.
 Orijinal veri setindeki 284.807 işlemin sadece %0.17'sini oluşturan
dolandırıcılık vakaları, SMOTE algoritması kullanılarak sentetik olarak
artırılmıştır.
 Eğitim veri seti %50 Normal, %50 Dolandırıcılık olacak şekilde (227.451'er
örnek) dengelenmiş ve modelin azınlık sınıfını ezberlemesi engellenmiştir.
- Algoritma Karşılaştırmaları ve Model Seçimi
## Sonuçları
Proje kapsamında eşzamanlı olarak üç farklı algoritma eğitilmiş ve test veri seti
(56.962 işlem) üzerinde karşılaştırılmıştır:
 Lojistik Regresyon: Yüksek yanlış alarm (False Positive) oranı nedeniyle
müşteri deneyimi açısından elenmiştir.
 Karar Ağacı: Yanlış alarmları azaltmış ancak tespit oranında yetersiz
kalmıştır.
 Rastgele Orman (Random Forest): Hem dolandırıcıları yakalama hem de
normal müşteriyi rahatsız etmeme konusunda en optimal dengeyi sağlamıştır.
Nihai (production) model olarak bu algoritma seçilmiştir.
## 4. Nihai Model Performans Skorlarının
## Konsolidasyonu
Seçilen Rastgele Orman modelinin test verisi üzerindeki kesin performans
konsolidasyonu şu şekildedir:
 Kesinlik (Precision): %84.04 (Alarm verilen işlemlerin %84'ü kesinlikle
dolandırıcıdır).

 Duyarlılık (Recall): %80.61 (Gerçek dolandırıcılık vakalarının büyük
çoğunluğu engellenmiştir).
 Yanlış Alarm (False Positive): 56.864 normal işlemin sadece 15'inde hatalı
alarm verilmiştir. Bankacılık sektörü için bu mükemmel bir operasyonel
başarıdır.
 AUC-ROC Skoru: 0.96 (Modelin sınıfları birbirinden ayırt etme gücü
neredeyse kusursuzdur).
- Sistem Entegrasyonu ve Ürünleşme
Sadece teorik metriklerle kalınmamış, proje uçtan uca (end-to-end) bir ürüne
dönüştürülmüştür.
 Eğitilen nihai model, fiziksel bir dosya (.pkl) olarak dışa aktarılmıştır.
 Python (Flask) kullanılarak bir web sunucusu ve kullanıcı arayüzü
geliştirilmiştir.
 Banka analistlerinin sistemi test edebileceği, yeni işlemlerin risk skorunu anlık
olarak hesaplayabilen çalışan bir prototip başarıyla canlıya alınmıştır.
- Genel Sonuç ve Hedeflere Ulaşım
"Fraud Shield AI" projesi, başlangıçta belirlenen "Yüksek tespit oranı ve sıfıra yakın
yanlış alarm" hedeflerine tam anlamıyla ulaşmıştır. Proje, makine öğrenimi teorisinin
pratik bir bankacılık problemine nasıl başarıyla uygulanabileceğini kanıtlayarak
geliştirme sürecini tamamlamıştır.
