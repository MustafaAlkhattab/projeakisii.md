## **Veri Ön İşleme ve Temizleme İşlemleri Planı** 

**Hazırlayan:** Ahmed (Proje Yöneticisi ve Veri Sorumlusu) **Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti **Tarih:** 30 Nisan 2026 

## **1. Planın Amacı** 

Bu belgenin amacı, makine öğrenimi modellerine beslenecek olan kredi kartı işlem verilerinin kalitesini artırmak için uygulanacak veri ön işleme ve temizleme adımlarını standartlaştırmaktır. Temiz ve tutarlı bir veri seti, modelin yanlış örüntüleri öğrenmesini (bias) engelleyerek dolandırıcılık tespitindeki genel doğruluğu artırır. 

## **2. Eksik Değerlerin (Missing Values) Yönetimi** 

Kaggle üzerinden alınan mevcut veri setinin genellikle temiz olduğu bilinse de, gerçek dünya senaryolarına uygun olarak eksik veriler için aşağıdaki strateji izlenecektir: 

- **Tespit:** `pandas` kütüphanesindeki `isnull().sum()` fonksiyonu ile her sütundaki eksik veri sayısı belirlenecektir. 

- **Ele Alma Yöntemi:** 

   - Eksik verilerin veri setine oranı **%1'den az ise** , bu satırlar modelin eğitimini etkilememesi için veri setinden çıkarılacaktır (Drop/Filtreleme). 

   - Oranın daha yüksek olması durumunda, sayısal sütunlar (örneğin "Amount") için ortalama (mean) yerine **medyan (median) ile doldurma** yöntemi kullanılacaktır. Ortalama değer uç değerlerden etkileneceği için finansal verilerde medyan daha güvenli bir yaklaşımdır. Kategorik veriler olsaydı en sık geçen değer (mode) kullanılacaktı. 

## **3. Aykırı Değerlerin (Outliers) Tespiti ve İşlenmesi** 

Dolandırıcılık tespiti projelerinde aykırı değer yönetimi en kritik aşamalardan biridir. 

- **Tespit:** Çeyreklikler Arası Aralık (IQR - Interquartile Range) yöntemi ve Kutu Grafikleri (Box Plots) kullanılarak V1-V28, "Time" ve "Amount" sütunlarındaki aykırı değerler tespit edilecektir. 

- **İşleme (Neden Silmiyoruz?):** Normal şartlarda makine öğreniminde aykırı değerler kırpılır (clipping) veya filtrelenerek silinir. Ancak **dolandırıcılık faaliyetlerinin kendisi yapısal olarak bir aykırı değerdir.** Uç değerleri silmek, modelin dolandırıcılığı öğrenmesini engeller. Bu nedenle verileri silmek yerine, aykırı değerlerin etkisini minimize eden **RobustScaler** kullanılarak dönüştürme (transformation) işlemi uygulanacaktır. 

## **4. Veri Tutarsızlıklarının Giderilmesi** 

Veri setindeki olası mantıksal hataları ve tekrarları önlemek için şu adımlar uygulanacaktır: 

- **Tekrarlanan Verilerin (Duplicates) Silinmesi:** Veri tabanı veya sistem hatalarından kaynaklanan aynı işlemler (satırlar), `drop_duplicates()` fonksiyonu ile tespit edilip silinecektir. Bu, modelin belirli işlemleri ezberlemesini (overfitting) önleyecektir. 

- **Veri Tipi Standardizasyonu:** "Class" (Hedef) değişkeninin tam sayı (integer - 0 ve 1) olduğundan, "Amount" ve "Time" değişkenlerinin ise ondalıklı sayı (float) formatında olduğundan emin olunacaktır. 

## **5. Veri Dengesizliği (Imbalanced Data) İçin Önlem** 

Veri ön işlemenin son ve en önemli adımı olarak, dolandırıcılık işlemlerinin (Class=1) normal işlemlere (Class=0) göre çok azınlıkta kalması problemi çözülecektir. Bu amaçla, sentetik veri üretme algoritması olan **SMOTE (Synthetic Minority Oversampling Technique)** kullanılarak azınlık sınıfı çoğaltılacak ve veri seti model eğitimi için dengeli hale getirilecektir. 

