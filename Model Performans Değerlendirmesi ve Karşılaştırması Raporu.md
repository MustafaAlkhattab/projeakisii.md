## **Model Performans Değerlendirmesi ve Karşılaştırması Raporu** 

## **Hazırlayan:** Felek 

**Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti 

**1. Giriş** Bu raporda, SMOTE yöntemi ile dengelenmiş veri seti üzerinde eğitilen iki temel makine öğrenimi modelinin (Lojistik Regresyon ve Karar Ağacı) performans sonuçları karşılaştırılmıştır. Amaç, hangi modelin dolandırıcılık (fraud) tespitinde daha başarılı olduğunu belirlemektir. 

**2. Sonuçların Analizi ve Karşılaştırma** Modellerin test verisi üzerindeki performansı Confusion Matrix (Karmaşıklık Matrisi) ve Classification Report metriklerine göre incelenmiştir: 

- **Lojistik Regresyon (Logistic Regression):** Model, 98 dolandırıcılık işleminin 90'ını başarılı bir şekilde yakalamıştır (Yüksek Recall). Ancak, doğrusal bir model olduğu için 1458 adet normal işlemi yanlışlıkla "dolandırıcılık" olarak işaretlemiştir (Yüksek False Positive). Bu durum banka müşterileri için rahatsız edici olabilecek gereksiz alarmlara yol açmaktadır. 

- **Karar Ağacı (Decision Tree):** Model, doğrusal olmayan ilişkileri daha iyi öğrenerek 1458 olan yanlış alarm (False Positive) sayısını **147'ye** düşürmüştür. 98 dolandırıcılık işleminin 76'sını yakalamıştır. Lojistik Regresyona kıyasla çok daha dengeli ve güvenilir bir profil çizmiştir. 

**3. Sonuç ve Öneri** İki model karşılaştırıldığında, Karar Ağacı algoritmasının yanlış alarmları (False Positives) ciddi oranda azalttığı ve kredi kartı verilerindeki karmaşık örüntüleri daha iyi öğrendiği görülmüştür. Bu nedenle projenin nihai tesliminde, Karar Ağacının daha gelişmiş bir ensemble (topluluk) versiyonu olan **Random Forest (Rastgele Orman)** algoritmasının kullanılması ve web arayüzüne entegre edilmesi ekibimizce kararlaştırılmıştır. 

