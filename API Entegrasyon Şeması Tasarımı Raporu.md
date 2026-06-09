## **API Entegrasyon Şeması Tasarımı Raporu** 

**Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI) 

## **1. Tasarımın Amacı** 

Bu belge, eğitilmiş makine öğrenimi modelinin (Random Forest - `.pkl` formatında) son kullanıcıların eriştiği web arayüzü (Front-End) ile nasıl haberleşeceğini gösteren API (Uygulama Programlama Arayüzü) entegrasyon şemasını ve mimarisini detaylandırmaktadır. 

## **2. Mimari ve Veri Akış Süreci** 

Sistem, "İstemci-Sunucu (Client-Server)" mimarisi üzerine inşa edilmiştir. Arayüz ile model arasındaki veri akışı şu adımlarla gerçekleşir: 

1. **İstek (Request):** Kullanıcı web arayüzünde (HTML/JS) form verilerini girer veya bir CSV dosyası yükler. JavaScript, bu verileri paketleyerek HTTP POST isteği ile sunucuya gönderir. 

2. **İşleme (Processing):** Python tabanlı Flask sunucusu isteği karşılar, gelen verileri modelin anlayacağı özellik (feature) vektörlerine (V1-V28, Time, Amount) dönüştürür. 

3. **Tahmin (Prediction):** İşlenen veriler `Nihai_RandomForest_Modeli.pkl` modeline beslenir. Model, %0 ile %100 arasında bir dolandırıcılık olasılığı hesaplar. 

4. **Yanıt (Response):** Flask sunucusu, modelin tahmin sonucunu standart bir JSON formatına çevirerek arayüze geri döndürür. 

## **3. Kullanılan API Endpoint'leri ve Veri Formatları** 

Sistemin verimli çalışabilmesi için iki farklı API uç noktası (endpoint) tasarlanmıştır: 

## **A. Tekli İşlem Kontrolü (Manuel Giriş)** 

- **Endpoint:** `/predict` 

- **Metot:** `POST` 

- **İstek (Request) Formatı:** JSON 

JSON 

```
{
  "amount": 9500.00,
  "time": 1500,
  "country": "RU",
  "device": "mobile",
  "payment": "online"
```

```
}
```

- **Yanıt (Response) Formatı:** JSON 

## JSON 

```
{
  "status": "success",
  "prediction": 1,
  "probability": 85.5
}
```

## **B. Toplu İşlem Kontrolü (Dosya Yükleme)** 

- **Endpoint:** `/predict_csv` 

- **Metot:** `POST` 

- **İstek (Request) Formatı:** `multipart/form-data` (CSV Dosyası) 

- **Yanıt (Response) Formatı:** JSON 

JSON 

```
{
  "status": "success",
  "total_records": 1000,
  "fraud_count": 12,
  "fraud_cases": [{...}, {...}]
}
```

## **4. Güvenlik ve Hata Yönetimi Önlemleri** 

Finansal verilerin işlendiği bu entegrasyonda aşağıdaki güvenlik ve verimlilik önlemleri tasarlanmış ve uygulanmıştır: 

- **CORS (Cross-Origin Resource Sharing):** API'ye sadece yetkilendirilmiş alan adlarının (domain) veya yerel portların (localhost) istek yapabilmesi için Flask-CORS kütüphanesi yapılandırılmıştır. Yabancı kaynaklardan gelen istekler reddedilir. 

- **Veri Doğrulama (Data Validation):** Arayüzden sunucuya eksik veya hatalı veri (örneğin harf içeren bir işlem tutarı) geldiğinde, sunucu çökmemek için `try-catch` (hata yakalama) blokları kullanır ve arayüze HTTP 400 (Bad Request) kodu döndürür. 

- **Gelecekteki Üretim (Production) Güvenliği:** Sistemin canlı ortama (canlı bir banka sunucusuna) taşınması durumunda, iletişim `HTTPS` protokolü ile şifrelenecek ve API'ye erişim `JWT (JSON Web Token)` kimlik doğrulama yöntemi ile sınırlandırılacaktır. 

