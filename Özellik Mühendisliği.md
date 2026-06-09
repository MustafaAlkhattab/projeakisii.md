## **Özellik Mühendisliği (Feature Engineering) Stratejisi** 

**Hazırlayan:** Ahmed (Proje Yöneticisi ve Veri Sorumlusu) **Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti **Tarih:** 30 Nisan 2026 

## **1. Stratejinin Amacı** 

Bu strateji belgesinin temel amacı, makine öğrenimi modellerinin (Lojistik Regresyon ve Karar Ağacı) dolandırıcılık tespitindeki doğruluk oranını ve performansını artırmak için mevcut verilerden yeni anlamlı özellikler (features) türetmek ve veriyi modele en uygun hale getirmektir. 

## **2. Mevcut Özelliklerden Yeni Özellikler Türetme (Feature Extraction)** 

Kullanılan veri setinde V1'den V28'e kadar olan değişkenler PCA (Temel Bileşen Analizi) ile gizlenmiş olsa da, "Time" (Zaman) ve "Amount" (Tutar) değişkenleri orijinal haliyle bulunmaktadır. Bu değişkenler üzerinden şu türetmeler planlanmaktadır: 

- **Zaman Serisi Özellikleri (Time-based Features):** Veri setindeki "Time" değişkeni, ilk işlemden itibaren geçen saniyeleri ifade etmektedir. Bu değer matematiksel bir dönüşümle **"Günün Saati" (Hour of Day)** formatına dönüştürülecektir. Dolandırıcılık işlemlerinin genellikle gece geç saatlerde (örneğin 00:00 - 05:00 arası) yoğunlaşma eğilimi olduğu bilindiğinden, bu yeni özellik modelin örüntüleri yakalamasına büyük katkı sağlayacaktır. 

- **İşlem Tutarı Sınıflandırması:** Gerekli görülmesi halinde, "Amount" değişkeni üzerinden belirli bir eşik değerin üzerindeki işlemler için "Yuksek_Tutar" (High_Amount) adında ikili (binary) bir yeni değişken oluşturulabilir. 

## **3. Harici Veri Kaynaklarının Değerlendirilmesi** 

Kapsamlı bir dolandırıcılık tespiti sisteminde modelin performansını artırmak için harici veriler entegre edilebilir: 

- **Coğrafi Konum (Geolocation) ve Demografik Veriler:** Müşterinin işlem yaptığı IP adresi ile kayıtlı ikametgahı arasındaki mesafe veya müşterinin yaş/gelir durumu gibi harici veriler, dolandırıcılık riskini belirlemede kritik bir rol oynar. 

- **Uygulanabilirlik Değerlendirmesi:** Projede kullandığımız Kaggle veri setinde veri gizliliği (privacy) nedeniyle müşteri kimlikleri ve kart bilgileri anonimleştirilmiştir. Bu nedenle harici bir API veya veri tabanı bağlamak _bu spesifik veri seti için_ teknik olarak mümkün değildir. Ancak gerçek dünya senaryolarında bu harici veri kaynaklarının sisteme entegre edilmesi stratejik olarak zorunludur. 

## **4. Dönüştürme ve Ölçeklendirme (Transformation & Scaling)** 

Türetilen ve mevcut olan özelliklerin model tarafından doğru ağırlıklandırılması için aşağıdaki işlemler uygulanacaktır: 

- **Logaritmik Dönüşüm (Log Transformation):** "Amount" değişkeninde çok fazla uç değer (outlier) bulunma ihtimali yüksektir. Verinin dağılımını normalleştirmek için logaritmik dönüşüm uygulanması test edilecektir. 

- **Ölçeklendirme (RobustScaler):** Standart ölçeklendirme (StandardScaler) uç değerlerden (outliers) çok fazla etkilendiği için, "Time" ve "Amount" değişkenlerini ölçeklendirmek amacıyla medyan ve çeyreklikler arası aralığı kullanan **RobustScaler** yöntemi tercih edilecektir. 

## **5. Sonuç** 

Belirtilen özellik mühendisliği adımları, veri ön işleme aşamasında (kodlama kısmında) sırasıyla uygulanacak ve dönüştürülen bu yeni veri seti (DataFrame) yapay zeka modellerine eğitim (training) için sunulacaktır. 

