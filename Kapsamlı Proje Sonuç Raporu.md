

## Kapsamlı Proje Sonuç Raporu
Proje Başlığı: Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI)
- Giriş ve Proje Amacı
Günümüzde dijital ödemelerin artmasıyla birlikte kredi kartı dolandırıcılığı, finansal
kuruluşlar için milyarlarca dolarlık zarara yol açan kritik bir problem haline gelmiştir.
Bu projenin temel amacı, makine öğrenimi (Machine Learning) algoritmalarını
kullanarak kredi kartı işlemlerini saniyeler içinde analiz eden, dolandırıcılık vakalarını
yüksek doğrulukla yakalayan ve aynı zamanda normal müşterileri rahatsız edecek
"yanlış alarmları" (False Positives) en aza indiren akıllı bir sistem geliştirmektir.
- Veri Ön İşleme ve Öznitelik Mühendisliği
Projede kullanılan veri setinde aşırı bir sınıf dengesizliği (Class Imbalance) mevcuttu.
284.807 işlemin sadece 492'si (%0.17) dolandırıcılık işlemiydi. Modelin sağlıklı
eğitilebilmesi için aşağıdaki adımlar uygulanmıştır:
 Ölçeklendirme (Scaling): Veri setindeki "Zaman" (Time) ve "Tutar"
(Amount) değişkenleri StandardScaler kullanılarak diğer özelliklerle aynı
ölçeğe getirilmiştir.
 Veri Bölme (Train-Test Split): Modelin tarafsız bir şekilde test edilebilmesi
için veri %80 Eğitim ve %20 Test olarak ayrılmıştır.
 Sınıf Dengeleme (SMOTE): Eğitim verisi üzerinde Sentetik Azınlık Aşırı
Örnekleme Tekniği (SMOTE) kullanılarak dolandırıcılık verileri sentetik
olarak artırılmış ve sınıflar %50-%50 (227.451'er satır) oranında eşitlenmiştir.
- Kullanılan Algoritmalar ve Model Seçimi
Proje kapsamında üç farklı denetimli öğrenme (Supervised Learning) algoritması test
edilmiştir:
 Lojistik Regresyon (Logistic Regression): Hızlı bir referans modeli olarak
kullanılmış, ancak yüksek yanlış alarm oranı nedeniyle elenmiştir.
 Karar Ağacı (Decision Tree): Yanlış alarmları azaltmada başarılı olmuş
fakat karmaşık örüntüleri yakalamada yetersiz kalmıştır.
 Rastgele Orman (Random Forest): Hiperparametre optimizasyonu
(Grid/Randomized Search) uygulanarak eğitilen bu algoritma, en kararlı ve
tutarlı sonuçları vererek projenin nihai (production) modeli olarak seçilmiştir.
- Model Performansı ve Değerlendirme Metrikleri
Nihai model olan Random Forest, daha önce hiç görmediği 56.962 işlemlik test veri
seti üzerinde test edilmiş ve aşağıdaki mükemmel sonuçları elde etmiştir:
 Doğruluk (Accuracy): %99.94

 Kesinlik (Precision): %84.04 (Sistemin "Dolandırıcı" dediği her 100 işlemin
84'ü kesinlikle dolandırıcıdır).
 Duyarlılık / Yakalama Oranı (Recall): %80.61 (Gerçekleşen
dolandırıcılıkların büyük çoğunluğu başarıyla tespit edilmiştir).
 Yanlış Alarm (False Positive): Test edilen on binlerce normal işlem arasında
sadece 15 adet yanlış alarm verilmiştir. Operasyonel maliyetleri düşürmek
adına bu büyük bir başarıdır.
 AUC-ROC Skoru: 0.96 olarak ölçülmüştür.
- Web Arayüzü ve Sistem Entegrasyonu
Proje sadece teorik bir model olarak bırakılmamış, son kullanıcı (banka analistleri)
için kullanılabilir bir ürüne dönüştürülmüştür.
 Eğitilen Random Forest modeli .pkl formatında kaydedilmiştir.
 Python tabanlı Flask framework'ü kullanılarak bir web sunucusu (API)
oluşturulmuştur.
 Geliştirilen HTML/CSS/JS tabanlı arayüz sayesinde, kullanıcılar sisteme yeni
işlem verileri girebilmekte ve yapay zeka modelinden anlık olarak "Güvenli"
veya "Şüpheli" şeklinde risk raporu alabilmektedir.
- Sonuç ve Gelecek Önerileri
6 haftalık geliştirme sürecinin sonunda "Fraud Shield AI" projesi hedeflerine tam
anlamıyla ulaşmıştır. Geliştirilen sistem, bankacılık sektöründe canlı ortama
(production) alınabilecek standartlardadır. Gelecek geliştirmeler için, dolandırıcıların
sürekli değişen taktiklerine karşı modelin her ay yeni verilerle otomatik olarak
yeniden eğitileceği (Continuous Training) bir yapay zeka boru hattı (AI Pipeline)
kurulması önerilmektedir.
