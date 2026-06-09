

Sonuçların Analizi ve Raporlanması
Proje: Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI)
## 1. Raporun Amacı
Bu raporun amacı, veri ön işleme aşamalarından geçirilip eğitilen makine öğrenimi
modellerinin (Lojistik Regresyon, Karar Ağacı ve Rastgele Orman) test verisi
üzerindeki performans sonuçlarını analiz etmek, metrikleri (Precision, Recall, F1-
Score) karşılaştırmak ve projenin nihai başarısını iş modeli (bankacılık)
perspektifinden değerlendirmektir.
- Veri Ön İşleme ve Sınıf Dengeleme Analizi
Orijinal veri setimizde yer alan 284.807 işlemin sadece 492'si (%0.17) dolandırıcılık
(Fraud - Sınıf 1) olarak etiketlenmişti. Modelin bu aşırı dengesizliği ezberlemesini
önlemek için uygulanan SMOTE (Sentetik Azınlık Aşırı Örnekleme) tekniği başarılı
olmuş ve eğitim veri seti 227.451 normal, 227.451 dolandırıcılık işlemi olacak şekilde
%50-%50 dengelenmiştir. Analizler, SMOTE işleminin modellerin azınlık sınıfını
(Fraud) öğrenme kapasitesini doğrudan artırdığını göstermiştir.
## 3. Model Performans Sonuçlarının Karşılaştırmalı
## Analizi
Eğitilen modeller, daha önce hiç görmedikleri %20'lik test verisi (56.962 işlem)
üzerinde test edilmiştir. Test setinde tam olarak 98 adet gerçek dolandırıcılık vakası
bulunmaktadır. Modellerin sonuçları aşağıdaki gibi analiz edilmiştir:
A. Lojistik Regresyon (Logistic Regression) Sonuçları
 Dolandırıcılık Yakalama (Recall): %92 (98 vakanın 90'ını yakaladı).
 Yanlış Alarm (False Positive): 1.458 adet normal işlem yanlışlıkla
"Dolandırıcı" olarak işaretlendi.
 Analiz: Model, dolandırıcılıkları yakalamada çok agresif davranmış ancak
kesinlik (Precision) oranı %6'da kalmıştır. Bankacılık sektörü için 1.458
müşterinin kartını haksız yere bloke etmek müşteri memnuniyetsizliği
yaratacağından bu model yetersiz bulunmuştur.
B. Karar Ağacı (Decision Tree) Sonuçları
 Dolandırıcılık Yakalama (Recall): %78 (98 vakanın 76'sını yakaladı).
 Yanlış Alarm (False Positive): 147 adet.
 Analiz: Doğrusal olmayan bir algoritma olduğu için Lojistik Regresyona göre
yanlış alarmları 10 kat oranında azaltmıştır. Ancak dolandırıcılığı yakalama
(Recall) oranında bir miktar kayıp yaşanmıştır.
C. Rastgele Orman (Random Forest - Nihai Model) Sonuçları

 Dolandırıcılık Yakalama (Recall): %81 (98 vakanın 79'unu yakaladı).
 Yanlış Alarm (False Positive): Sadece 15 adet.
 Kesinlik (Precision): %84
 Analiz: Bu model, diğer iki modelin zayıf yönlerini dengelemiştir. Neredeyse
hiç yanlış alarm vermeden (sadece 15 hata) dolandırıcılık işlemlerinin çok
büyük bir kısmını başarıyla tespit etmiştir. F1-Skoru en yüksek olan modeldir.
- İş Etkisi (Business Impact) ve Karar
Teknik sonuçlar iş modeli açısından incelendiğinde; False Positive (Yanlış Alarm)
oranının 1.458'den 15'e düşürülmesi, bankanın operasyonel maliyetlerinde devasa bir
tasarruf anlamına gelmektedir (gereksiz çağrı merkezi trafiği ve müşteri şikayetlerinin
önlenmesi).
Nihai Karar: Test sonuçları analiz edildiğinde, projenin temel hedefi olan "yüksek
doğruluk ve düşük yanlış alarm" hedefine ulaşan Random Forest (Rastgele Orman)
algoritması projenin nihai (production) modeli olarak seçilmiş ve web arayüzü (Flask
API) ile başarılı bir şekilde entegre edilmiştir.
