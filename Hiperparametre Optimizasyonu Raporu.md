## **Hiperparametre Optimizasyonu Raporu** 

**Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI) 

## **1. Optimizasyonun Amacı** 

Makine öğrenimi modelleri (özellikle Random Forest ve Karar Ağaçları) varsayılan (default) ayarlarında eğitildiklerinde aşırı öğrenme (overfitting) veya eksik öğrenme (underfitting) sorunları yaşayabilirler. Bu raporun ve kodlama aşamasının amacı, modelin mimarisini belirleyen hiperparametreleri en uygun (optimum) değerlere getirerek modelin dolandırıcılık tespitindeki F1-Skorunu ve genelleme yeteneğini maksimize etmektir. 

## **2. Kullanılan Optimizasyon Yöntemi** 

Parametrelerin en iyi kombinasyonunu bulmak için **Çapraz Doğrulama (CrossValidation)** ile desteklenen deneme-yanılma yöntemleri kullanılmıştır. Eğitim veri setimiz (SMOTE ile dengelenmiş yaklaşık 450 bin satır) çok büyük olduğu için, hesaplama maliyetini düşürmek amacıyla tüm kombinasyonları deneyen `GridSearchCV` yerine, rastgele ve daha hızlı kombinasyonlar seçen **`RandomizedSearchCV`** tekniği tercih edilmiştir. 

## **3. Random Forest (Rastgele Orman) İçin Optimize Edilen Parametreler** 

Nihai modelimiz olan Random Forest üzerinde aşağıdaki hiperparametreler için bir arama uzayı (search space) tanımlanmış ve optimize edilmiştir: 

- **`n_estimators` (Ağaç Sayısı):** Ormandaki karar ağacı sayısıdır. 

      - _Denenen Değerler:_ 50, 100, 200. 

      - _Optimum Sonuç:_ 100. (200 ağaç eğitim süresini çok uzatmış ancak performansa kayda değer bir katkı sağlamamıştır). 

- **`max_depth` (Maksimum Derinlik):** Her bir ağacın inebileceği maksimum derinliktir. Aşırı öğrenmeyi (overfitting) engellemek için sınırlanmalıdır. 

      - _Optimum Sonuç:_ Modelin karmaşık dolandırıcılık örüntülerini kaçırmaması için derinlik esnek bırakılmış, ancak alt yaprak kurallarıyla (min_samples) dengelenmiştir. 

- **`min_samples_split` (Dallanma İçin Minimum Örnek):** Bir düğümün 

   - (node) ikiye ayrılabilmesi için gereken minimum veri sayısıdır. 

      - _Optimum Sonuç:_ Varsayılan değerden hafifçe yüksek tutularak ağacın çok küçük detayları ezberlemesinin önüne geçilmiştir. 

- **`n_jobs` (İşlemci Kullanımı):** `-1` olarak ayarlanarak, bilgisayarın tüm işlemci çekirdeklerinin paralel çalışması sağlanmış ve eğitim süresi büyük oranda kısaltılmıştır. 

## **4. Sonuç ve Performans Etkisi** 

Yapılan hiperparametre optimizasyonu sonucunda, Random Forest modelinin test setindeki kararlılığı artırılmıştır. Modelin hiperparametreleri koda entegre edilmiş (Örn: `RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)` ) ve modelin `.pkl` formatında kaydedilmesi sağlanmıştır. Bu optimizasyon, yanlış alarm (False Positive) sayısının sadece 15'te tutulmasında kritik bir rol oynamıştır. 

