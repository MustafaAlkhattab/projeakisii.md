## **Model Seçimi ve Değerlendirme Metrikleri Raporu** 

**Hazırlayan:** Felek (Makine Öğrenimi Geliştiricisi) 

**Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti 

**Tarih:** 2 Mayıs 2026 

## **1. Raporun Amacı** 

Bu rapor, kredi kartı dolandırıcılığı tespiti projesinde kullanılacak makine öğrenimi algoritmalarının seçim gerekçelerini açıklamak ve modellerin performansını doğru bir şekilde ölçmek için kullanılacak değerlendirme metriklerini (Evaluation Metrics) tanımlamak amacıyla hazırlanmıştır. 

## **2. Model Seçimi ve Gerekçeleri** 

Projenin kapsamı ve veri setinin yapısı (Binary Classification - İkili Sınıflandırma) göz önüne alınarak aşağıdaki iki temel makine öğrenimi modeli seçilmiştir: 

## **A. Lojistik Regresyon (Logistic Regression):** 

- **Seçim Gerekçesi:** Lojistik regresyon, ikili sınıflandırma problemleri için endüstri standardı olan temel bir algoritmadır (baseline model). Hesaplama açısından çok hızlıdır ve sonuçları olasılık (probability) olarak ürettiği için yorumlanması oldukça kolaydır. 

- **Kullanım Amacı:** Projede temel referans noktamızı (baseline) oluşturmak ve doğrusal (linear) ilişkileri ne kadar iyi yakalayabildiğimizi görmek için ilk model olarak kullanılacaktır. 

## **B. Karar Ağacı (Decision Tree):** 

- **Seçim Gerekçesi:** Veri setindeki değişkenler (V1-V28, Time, Amount) arasında doğrusal olmayan (non-linear) karmaşık ilişkiler bulunabilir. Karar ağaçları, veriyi belirli koşullara göre dallara ayırarak bu karmaşık ilişkileri ve gizli örüntüleri yakalamakta çok başarılıdır. 

- **Kullanım Amacı:** Lojistik regresyonun yetersiz kalabileceği doğrusal olmayan durumları çözmek ve her iki modelin performansını birbiriyle kıyaslamak (Hafta 3 - Görev 7) için ikinci model olarak kullanılacaktır. 

## **3. Değerlendirme Metrikleri (Evaluation Metrics)** 

Kredi kartı dolandırıcılığı veri setlerinde dolandırıcı işlemler (Class=1), normal işlemlere (Class=0) göre çok azınlıktadır (%0.17 civarı). Bu tür dengesiz veri 

setlerinde (imbalanced data) **Doğruluk (Accuracy) metriği kullanılamaz.** (Çünkü model her işleme "Güvenli" dese bile %99.8 doğruluk oranına ulaşır, ancak dolandırıcılıkları kaçırır). 

Bu yanılgıya düşmemek için model değerlendirmesinde aşağıdaki metrikler temel alınacaktır: 

- **1. Duyarlılık / Hassasiyet (Recall / Sensitivity):** `TP / (TP + FN)` 

   - **Anlamı:** Gerçekte dolandırıcı olan işlemlerin yüzde kaçını doğru yakalayabildik? 

   - **Projedeki Önemi:** Bankacılık sektöründe bir dolandırıcılığı kaçırmanın maliyeti çok yüksektir. Bu nedenle projemizdeki en kritik metrik **Recall** olacaktır. Hedefimiz bu değeri maksimize etmektir. 

- **2. Kesinlik (Precision):** `TP / (TP + FP)` 

   - **Anlamı:** Modelin "Dolandırıcı" dediği işlemlerin yüzde kaçı gerçekten dolandırıcıdır? 

   - **Projedeki Önemi:** Müşterilerin normal işlemlerini sürekli yanlışlıkla iptal etmek (False Positive) müşteri memnuniyetsizliğine yol açar. Bu metrik ile gereksiz alarmları ölçmüş olacağız. 

- **3. F1-Skoru (F1-Score):** 

   - **Anlamı:** Precision ve Recall metriklerinin harmonik ortalamasıdır. 

   - **Projedeki Önemi:** Modelin hem dolandırıcılıkları yakalama yeteneğini hem de gereksiz alarm vermeme yeteneğini tek bir skorla dengelemek için kullanılacaktır. 

- **4. AUC-ROC Eğrisi (Area Under the Receiver Operating Characteristic Curve):** 

   - **Anlamı:** Modelin farklı eşik değerlerinde (thresholds) pozitif ve negatif sınıfları birbirinden ne kadar iyi ayırabildiğini gösteren grafiksel bir metriktir. 

   - **Projedeki Önemi:** Lojistik Regresyon ve Karar Ağacı modellerinin genel başarımlarını birbirleriyle kıyaslarken temel alınacaktır. 

## **4. Sonuç** 

Belirtilen bu teorik altyapı ve metrikler, geliştirme aşamasındaki kodlama görevlerinde (Görev 5 ve Görev 6) modellerin eğitilmesi (training) ve hiperparametre optimizasyonu süreçlerinde doğrudan kullanılacak ve nihai model seçimi bu metriklerin sonuçlarına göre yapılacaktır. 

