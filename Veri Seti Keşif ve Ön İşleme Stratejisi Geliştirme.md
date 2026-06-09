## **Veri Seti Keşfi ve Ön İşleme Planı** 

**Hazırlayan:** Ahmed Kannavi (Proje Yöneticisi ve Veri Sorumlusu) **Görev:** Kullanılacak veri setinin incelenmesi, kalitesinin değerlendirilmesi ve ön işleme adımlarının planlanması. 

## **1. Kullanılacak Veri Setinin İncelenmesi** 

Projemizde, makine öğrenimi literatüründe standart haline gelmiş olan Kaggle **"Credit Card Fraud Detection"** veri seti kullanılacaktır. 

- **Veri Yapısı:** Veri setinde yaklaşık 284.807 işlem (satır) ve 31 öznitelik (sütun) bulunmaktadır. 

- **Değişkenler:** Müşteri gizliliğini korumak amacıyla verilerin büyük bir kısmı PCA (Temel Bileşenler Analizi) işleminden geçirilmiş ve V1'den V28'e kadar isimlendirilmiştir. Sadece "Time" (İşlem Zamanı) ve "Amount" (İşlem Tutarı) özellikleri orijinal haliyle bırakılmıştır. 

- **Hedef Değişken (Class):** İşlemin dolandırıcılık olup olmadığını gösterir (0: Normal İşlem, 1: Dolandırıcılık). 

## **2. Eksik Verilerin (Missing Values) Ele Alınması** 

Veri seti projeye dahil edildiğinde ilk olarak eksik değer kontrolü yapılacaktır. Stratejimiz şu şekildedir: 

- Eğer eksik değer oranı çok düşükse (örneğin %1'den az), veri setinin genel yapısını bozmamak adına bu satırlar tamamen silinecektir (Drop). 

- Eğer belirli sütunlarda yoğun eksik veri bulunursa, bu değerler veri dağılımını etkilememesi için sütunun **medyan (ortanca)** değerleri ile doldurulacaktır (Imputation). 

## **3. Veri Setinin Temizlenmesi ve Dönüştürülmesi** 

Modellerin doğru ve verimli çalışabilmesi için şu ön işleme (preprocessing) adımları uygulanacaktır: 

- **Ölçeklendirme (Scaling):** PCA uygulanmış V1-V28 sütunları zaten belirli bir ölçektedir. Ancak "Time" ve "Amount" sütunları çok geniş bir aralığa sahip olduğu için, aykırı değerlere (outliers) karşı dirençli olan **RobustScaler** kullanılarak ölçeklendirilecektir. 

- **Mükerrer Verilerin Silinmesi:** Veri setindeki tekrar eden aynı işlemler (duplicate rows) modelin ezberlemesini (overfitting) önlemek amacıyla tespit edilip temizlenecektir. 

## **4. Veri Kalitesi ve Sınıf Dengesizliğinin (Class Imbalance) Çözümü** 

Veri kalitesi açısından en büyük zorluk sınıf dengesizliğidir. Veri setindeki işlemlerin %99.8'i normal, sadece %0.17'si dolandırıcılık işlemidir. Bu durum, modelin sürekli "0" tahmin ederek yüksek doğruluk (accuracy) yanılgısına düşmesine sebep olabilir. 

- **Çözüm Planı:** Eğitim aşamasına geçilmeden önce, **SMOTE (Synthetic Minority Over-sampling Technique)** yöntemi kullanılarak azınlık sınıfı (dolandırıcılık) sentetik olarak artırılacak ve eğitim verilerinde sınıflar arası denge sağlanacaktır. 

