## **Model Seçimi ve Değerlendirme Metrikleri Araştırması Raporu** 

**Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI) 

## **1. Araştırmanın Amacı** 

Bu raporun amacı, kredi kartı dolandırıcılığı (fraud detection) gibi yapısal olarak dengesiz (imbalanced) veri setlerinde yüksek performans gösterebilecek makine öğrenimi algoritmalarını literatür taraması yoluyla araştırmaktır. Ayrıca, sınıflandırma modellerinin performansını ölçmek için kullanılan çeşitli değerlendirme metriklerinin teorik altyapıları incelenmiş ve dolandırıcılık bağlamındaki önemleri vurgulanmıştır. 

## **2. Makine Öğrenimi Modelleri Araştırması** 

Dolandırıcılık tespiti bir "ikili sınıflandırma (binary classification)" problemidir. Bu kapsamda literatürde en çok öne çıkan algoritmalar ve özellikleri aşağıda incelenmiştir: 

## **A. Lojistik Regresyon (Logistic Regression)** 

- **Özellikleri:** İkili sınıflandırma problemleri için temel istatistiksel bir modeldir. Çıktıları 0 ile 1 arasında bir olasılık değeri olarak verir. 

- **Avantajları:** Hesaplama maliyeti çok düşüktür, hızlı eğitilir ve sonuçların yorumlanabilirliği (hangi değişkenin ne kadar etki ettiği) son derece yüksektir. 

- **Dezavantajları:** Değişkenler arasındaki karmaşık ve doğrusal olmayan (nonlinear) ilişkileri yakalamada yetersiz kalır. 

- **Uygun Veri Setleri:** Doğrusal olarak ayrılabilen ve çok karmaşık olmayan veri setlerinde temel (baseline) model olarak idealdir. 

## **B. Karar Ağaçları (Decision Trees)** 

- **Özellikleri:** Veri setini bilgi kazancı (information gain) veya Gini safsızlığı gibi kriterlere göre dallara ayırarak karar kuralları (if-else) oluşturan bir algoritmadır. 

- **Avantajları:** Doğrusal olmayan ilişkileri çok iyi öğrenir. Veri ön işleme (ölçeklendirme vb.) ihtiyacı minimumdur ve karar süreçleri bir ağaç grafiği üzerinden insan tarafından kolayca okunabilir. 

- **Dezavantajları:** Aşırı öğrenmeye (overfitting) çok yatkındır. Verideki küçük bir değişiklik ağacın tüm yapısını bozabilir. 

## **C. Rastgele Ormanlar (Random Forests)** 

- **Özellikleri:** Birden fazla karar ağacının bir araya gelerek (ensemble) ortak bir tahmin ürettiği güçlü bir algoritmadır. 

- **Avantajları:** Aşırı öğrenme (overfitting) riskini ciddi oranda azaltır. Yüksek boyutlu ve çok değişkenli veri setlerinde olağanüstü yüksek doğruluk oranlarına ulaşır. 

- **Dezavantajları:** Modelin boyutu büyüktür, eğitilmesi uzun sürer ve "kara kutu (black-box)" yapısında olduğu için iç karar mekanizmasını yorumlamak zordur. 

## **D. Destek Vektör Makineleri (Support Vector Machines - SVM)** 

- **Özellikleri:** Sınıfları birbirinden ayırmak için n-boyutlu uzayda en uygun hiper-düzlemi (hyperplane) çizen bir algoritmadır. 

- **Avantajları:** Marjin maksimizasyonu sayesinde yüksek boyutlu verilerde çok etkilidir. 

- **Dezavantajları:** Milyonlarca satırlık büyük bankacılık veri setlerinde (Big Data) hesaplama süresi pratik olarak uygulanamayacak kadar uzundur. 

## **E. Yapay Sinir Ağları (Artificial Neural Networks - ANN)** 

- **Özellikleri:** İnsan beynindeki nöronların çalışma prensibini taklit eden derin öğrenme algoritmalarıdır. 

- **Avantajları:** En karmaşık ve gizli örüntüleri (özellikle zaman serisi veya ardışık işlemlerde) yakalayabilen en güçlü yapılardır. 

- **Dezavantajları:** Devasa donanım gücüne (GPU) ve çok büyük miktarda veriye ihtiyaç duyar. Hiperparametre optimizasyonu son derece zahmetlidir. 

## **3. Değerlendirme Metrikleri Araştırması** 

Sınıflandırma modellerinin başarısını ölçmek için kullanılan standart metriklerin formülleri ve teorik anlamları araştırılmıştır: 

- **Kesinlik (Precision):** Modelin "Pozitif (Dolandırıcı)" olarak işaretlediği işlemlerin gerçekten ne kadarının pozitif olduğunu gösterir. `(True Positive / (True Positive + False Positive))` 

- **Duyarlılık / Hassasiyet (Recall / True Positive Rate):** Gerçekte pozitif olan durumların ne kadarının model tarafından doğru tespit edildiğini gösterir. `(True Positive / (True Positive + False Negative))` 

- **F1-Skoru (F1-Score):** Kesinlik ve Duyarlılık metriklerinin harmonik ortalamasıdır. İki metrik arasında bir denge kurar. `(2 * (Precision * Recall) / (Precision + Recall))` 

- **AUC-ROC Eğrisi:** Farklı sınıflandırma eşik değerlerinde (threshold) modelin pozitif ve negatif sınıfları ayırt etme yeteneğini (Eğri Altında Kalan Alan - Area Under Curve) grafiksel olarak ölçer. Alanın 1'e yaklaşması modelin mükemmel olduğunu gösterir. 

## **4. Dengesiz Veri Setlerinde Metriklerin Önemi (Özel Vurgu)** 

Kredi kartı dolandırıcılığı verilerinde, dolandırıcılık vakaları (Class=1) genellikle %1'den daha azdır. Bu "Aşırı Sınıf Dengesizliği (Class Imbalance)" durumu, geleneksel değerlendirme metriklerini yanıltıcı hale getirir. 

**Neden Doğruluk (Accuracy) Kullanılamaz?** Eğer model %99 oranında normal işlem içeren bir veri setinde tüm işlemlere "Normal" cevabı verirse, hiç dolandırıcı yakalamamasına rağmen %99 Doğruluk (Accuracy) oranına ulaşır. Bu durum bankacılık sistemleri için felakettir. 

**Hangi Metriklere Odaklanılmalı?** Dolandırıcılık tespitinde öncelikli metrik **Duyarlılık (Recall)** olmalıdır. Bir dolandırıcılığı gözden kaçırmanın (False Negative) finansal maliyeti, normal bir işlemi yanlışlıkla dolandırıcılık olarak işaretlemekten (False Positive) çok daha yüksektir. Bu nedenle modeller eğitilirken Recall oranını en üst düzeye çıkarmak birincil araştırma hedefi olmalıdır. 

