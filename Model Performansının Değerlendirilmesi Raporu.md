## **Model Performansının Değerlendirilmesi Raporu** 

**Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI) 

## **1. Değerlendirme Amacı** 

Bu raporun amacı, hiperparametre optimizasyonu tamamlanmış ve nihai (production) model olarak seçilmiş olan **Rastgele Orman (Random Forest)** algoritmasının, daha önce hiç görmediği test veri seti üzerindeki matematiksel performansını standart makine öğrenimi metrikleri kullanılarak ölçmek ve belgelendirmektir. 

## **2. Karmaşıklık Matrisi (Confusion Matrix) Analizi** 

Model, 56.962 işlemden oluşan test seti (98'i dolandırıcılık, 56.864'ü normal işlem) üzerinde test edilmiş ve aşağıdaki matris elde edilmiştir: 

- **Gerçek Negatif (True Negative - TN):** 56.849 (Normal işlemler doğru bilindi) 

- **Yanlış Pozitif (False Positive - FP):** 15 (Normal işlemler yanlışlıkla dolandırıcı sanıldı - Tip 1 Hata) 

- **Yanlış Negatif (False Negative - FN):** 19 (Dolandırıcılık işlemleri gözden kaçtı - Tip 2 Hata) 

- **Gerçek Pozitif (True Positive - TP):** 79 (Dolandırıcılık işlemleri başarıyla yakalandı) 

## **3. Temel Sınıflandırma Metrikleri** 

Karmaşıklık matrisinden elde edilen değerler kullanılarak modelin performansı aşağıdaki metriklerle ölçülmüştür: 

- **Doğruluk (Accuracy): %99.94** _(Veri setindeki aşırı dengesizlik nedeniyle bu metrik tek başına referans alınmamıştır, ancak modelin genel kararlılığını gösterir.)_ 

- **Kesinlik (Precision): %84.04** _Hesaplama:_ `TP / (TP + FP) -> 79 / (79 + 15)` _Yorum:_ Modelin "Dolandırıcı" uyarısı verdiği her 100 işlemin yaklaşık 84'ü gerçekten dolandırıcılıktır. Yanlış alarmlar çok düşük seviyededir. 

- **Duyarlılık / Yakalama Oranı (Recall): %80.61** _Hesaplama:_ `TP / (TP + FN) -> 79 / (79 + 19)` _Yorum:_ Sistem, gerçekleşen tüm dolandırıcılık vakalarının %80.6'sını başarıyla tespit edip engellemiştir. 

- **F1-Skoru (F1-Score): %82.29** _Yorum:_ Kesinlik ve Duyarlılık metriklerinin harmonik ortalaması olan F1-Skoru, modelin hem yanlış alarmları önlemede hem de dolandırıcıları yakalamada ne kadar dengeli çalıştığını kanıtlamaktadır. 

## **4. AUC-ROC Performansı** 

Sınıflandırma modelimizin başarı oranını eşik değerlerinden (threshold) bağımsız olarak ölçmek için ROC (Alıcı İşletim Karakteristiği) eğrisi çizdirilmiştir. Eğri Altındaki Alan **(AUC - Area Under Curve) değeri 0.96** olarak hesaplanmıştır. Bu değerin 1.0'a çok yakın olması, modelin "Normal" ve "Dolandırıcı" sınıflarını birbirinden ayırt etme (discrimination) kapasitesinin mükemmel seviyede olduğunu göstermektedir. 

## _]_ 

## **5. Değerlendirme Sonucu** 

Elde edilen metrikler (Özellikle %84 Precision ve %80 Recall dengesi), Random Forest modelinin kredi kartı dolandırıcılığı tespiti gibi yüksek riskli ve dengesiz (imbalanced) bir problemde canlıya alınabilecek (production-ready) güvenilirlikte olduğunu matematiksel olarak kanıtlamıştır. 

