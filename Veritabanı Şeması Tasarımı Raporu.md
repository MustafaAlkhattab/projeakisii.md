## **Veritabanı Şeması Tasarımı Raporu** 

**Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI) 

## **1. Tasarımın Amacı** 

Bu rapor, kredi kartı dolandırıcılığı tespiti projesinin (Fraud Shield AI) arka planında çalışacak ilişkisel veritabanı (RDBMS) şemasının tasarımını detaylandırmaktadır. Tasarım; veri bütünlüğünü sağlamak, modelin ürettiği analiz sonuçlarını güvenli bir şekilde saklamak ve büyük veri setleri (Big Data) üzerinde performansı optimize etmek amacıyla oluşturulmuştur. 

## **2. Tablo Yapıları, Veri Tipleri ve Anahtarlar** 

Veritabanı temel olarak 3 ana tablodan oluşmaktadır: Kullanıcılar, İşlemler ve Model Sonuçları. 

## **Tablo 1: Users (Kullanıcı Bilgileri)** 

Sistemi kullanacak banka personeli ve analistlerin bilgilerini tutar. 

- **user_id (PK):** `INT` - Otomatik artan (Auto-Increment) benzersiz kimlik. 

- **username:** `VARCHAR(50)` - Kullanıcı adı. 

- **password_hash:** `VARCHAR(255)` - Şifrelenmiş parola (Güvenlik için). 

- **role:** `VARCHAR(20)` - Kullanıcı rolü (Örn: "Analyst", "Admin"). 

- **created_at:** `TIMESTAMP` - Hesabın oluşturulma tarihi. 

## **Tablo 2: Transactions (İşlem Verileri)** 

Kredi kartı ile yapılan ham işlemleri (manuel girilen veya CSV ile yüklenen) tutar. 

- **transaction_id (PK):** `VARCHAR(100)` - İşleme ait benzersiz ID (Örn: UUID). 

- **amount:** `DECIMAL(10, 2)` - İşlem tutarı. 

- **time_seconds:** `INT` - İşlemin gerçekleşme zamanı (Time değişkeni). 

- **country_code:** `VARCHAR(3)` - İşlemin yapıldığı lokasyon/ülke. 

- **is_fraud_actual:** `TINYINT` - İşlemin gerçekte dolandırıcılık olup olmadığı (Eğer banka sonradan teyit ederse güncellenir: 0 veya 1). 

## **Tablo 3: Model_Results (Model Tahmin Sonuçları)** 

Yapay Zeka modelinin (Random Forest) işlemler üzerindeki analiz sonuçlarını ve kullanıcının aldığı aksiyonları tutar. 

- **result_id (PK):** `INT` - Sonuca ait otomatik artan benzersiz ID. 

- **transaction_id (FK):** `VARCHAR(100)` - İşlemi referans alan Yabancı Anahtar (Transactions tablosuna bağlı). 

- **user_id (FK):** `INT` - İşlemi analiz eden/onaylayan kullanıcıyı referans alan Yabancı Anahtar (Users tablosuna bağlı). 

- **risk_score:** `DECIMAL(5, 2)` - Modelin ürettiği risk olasılığı (Örn: %85.50). 

- **prediction:** `TINYINT` - Modelin tahmini (0: Güvenli, 1: Fraud). 

- **action_taken:** `VARCHAR(20)` - Analistin işlemi onaylayıp onaylamadığı ("Approved", "Blocked", "Pending"). 

- **analyzed_at:** `TIMESTAMP` - Analizin yapıldığı tarih ve saat. 

## **3. Veritabanı İlişkileri (Relationships)** 

- **Users -> Model_Results:** 1'den Çoğa (1:N) ilişki. Bir analist birden fazla işlem sonucunu değerlendirebilir. 

- **Transactions -> Model_Results:** Bire Bir (1:1) veya 1'den Çoğa (1:N) ilişki. Bir işlemin birden fazla kez analiz edilme ihtimaline karşı 1:N esnekliği bırakılmıştır. 

## **4. Performans Optimizasyonu ve İndeksleme (Indexing) Planı** 

Milyonlarca satırlık kredi kartı verisinde sorguların (queries) yavaşlamaması için aşağıdaki indeksleme stratejisi tasarlanmıştır: 

1. **Primary Key İndeksleri:** `user_id` , `transaction_id` ve `result_id` sistem tarafından otomatik olarak indekslenir (Clustered Index). 

2. **Filtreleme İndeksleri (Non-Clustered Index):** * Arayüzdeki tabloda sadece şüpheli işlemleri hızlıca göstermek için `Model_Results` tablosundaki **`prediction`** ve **`risk_score`** sütunlarına indeks eklenecektir. 

   - Tarihe göre raporlama yapılabilmesi için `analyzed_at` sütununa indeks uygulanacaktır. 

## **5. Veritabanı Şeması Diyagramı (ER Diagram)** 

Aşağıda veritabanının kavramsal mimarisi görselleştirilmiştir: 

Plaintext `[ USERS ] +-- user_id (PK) |-- username |-- password_hash |-- role +-- created_at | | 1 | | N [ MODEL_RESULTS ]                           [ TRANSACTIONS ] +-- result_id (PK)                          +-- transaction_id (PK) |-- transaction_id (FK) >------------------ | |-- user_id (FK) <------ (Bağlantı)         |-- amount |-- risk_score                              |-- time_seconds |-- prediction                              |-- country_code` 

```
|-- action_taken                            +-- is_fraud_actual
+-- analyzed_at
```

