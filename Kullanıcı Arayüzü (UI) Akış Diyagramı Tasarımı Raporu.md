## **Kullanıcı Arayüzü (UI) Akış Diyagramı Tasarımı Raporu** 

**Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI) 

## **1. Tasarımın Amacı** 

Bu belgenin amacı, "Fraud Shield AI" web arayüzünü kullanacak olan banka analistlerinin veya güvenlik uzmanlarının sistem içindeki yolculuğunu (User Flow) adım adım tasarlamaktır. Tasarım; sezgisel bir kullanım sunmayı, tıklama sayısını (click-depth) en aza indirmeyi ve karmaşık yapay zeka sonuçlarını hızlı kararlara dönüştürmeyi hedeflemektedir. 

## **2. Kullanıcı Akış Adımları (User Flow)** 

Kullanıcının sisteme girişinden rapor oluşturmasına kadar geçen süreç aşağıdaki 5 temel adımdan oluşmaktadır: 

## **Adım 1: Sisteme Giriş ve Ana Gösterge Paneli (Dashboard)** 

- **Eylem:** Kullanıcı web tarayıcısı üzerinden sisteme giriş yapar. 

- **Arayüz Elemanları:** Üst gezinme çubuğu (Navbar), iki ana işlem sekmesi ("Tekli İşlem" ve "Toplu İşlem"), ve son analiz edilen işlemleri gösteren özet bir tablo (Recent Transactions). 

- **Geçiş:** Kullanıcı, sayfa yüklendiğinde doğrudan "Tekli İşlem" formunun bulunduğu varsayılan ana ekrana yönlendirilir. 

## **Adım 2: İşlem Verilerini Girme (Manuel Kontrol)** 

- **Eylem:** Kullanıcı, şüpheli bulduğu spesifik bir kredi kartı işlemini kontrol etmek ister. 

- **Arayüz Elemanları:** * Girdi Formları (Input Fields): İşlem Tutarı, Lokasyon (Ülke), Zaman ve Cihaz Tipi bilgileri için metin kutuları ve açılır menüler (Dropdowns). 

   - **"Yapay Zeka Analizini Başlat"** butonu (Harekete Geçirici Mesaj - CTA). 

- **Geçiş:** Butona tıklandığında ekran kararmadan bir "Yükleniyor (Loading Bar)" animasyonu tetiklenir. 

## **Adım 3: İşlem Detaylarını ve Model Sonucunu Görüntüleme** 

- **Eylem:** Sistem tahmini saniyeler içinde ekrana yansıtır. 

- **Arayüz Elemanları:** 

   - **Risk Skoru Çubuğu (Progress Bar):** %0 ile %100 arasında dinamik dolan bir çubuk. 

   - **Durum Rozetleri (Badges):** İşlem durumunu belirten "Güvenli İşlem (Yeşil)" veya "Yüksek Riskli Fraud (Kırmızı)" etiketleri. 

- **Detay Kartları (Cards):** Modelin bu kararı neden verdiğini açıklayan alt kartlar (Örn: "Yüksek Tutar", "Riskli Saat"). 

## **Adım 4: Şüpheli İşlemleri İşaretleme ve Aksiyon Alma** 

- **Eylem:** Analist, yapay zeka sonucuna göre işlem hakkında nihai bir karar verir. 

- **Arayüz Elemanları:** 

   - **"İşlemi Onayla"** Butonu (Yeşil renkli, birincil buton). 

   - **"Kartı Bloke Et / Şüpheli İşaretle"** Butonu (Kırmızı renkli, dikkat çekici buton). 

- **Geçiş:** Karar verildikten sonra, arayüz ekranın sağ üst köşesinde "İşlem başarıyla kaydedildi" şeklinde küçük bir bildirim (Toast Notification) gösterir ve işlem geçmişi tablosuna eklenir. 

## **Adım 5: Rapor Oluşturma ve Toplu Analiz (CSV)** 

- **Eylem:** Kullanıcı gün sonu raporu almak veya binlerce işlemi aynı anda taramak ister. 

- **Arayüz Elemanları:** 

   - Sürükle-bırak destekli dosya yükleme alanı (Drag & Drop Zone). 

   - **Dinamik Veri Tablosu (Data Table):** Sadece "Fraud" olarak tespit edilen işlemleri filtreleyen, sütun başlıklarına göre sıralanabilen (sortable) bir tablo. 

   - **"CSV Olarak İndir / Raporla"** butonu. 

- **Geçiş:** Tablodaki sonuçlar indirildiğinde süreç tamamlanır ve sistem yeni bir analiz için hazır hale gelir. 

## **3. UX (Kullanıcı Deneyimi) Odaklı Tasarım Prensipleri** 

Sistem akışı tasarlanırken aşağıdaki UX kuralları titizlikle uygulanmıştır: 

- **Görsel Hiyerarşi:** En önemli bilgi olan "Risk Skoru" ekranın tam ortasında ve en büyük puntolarla gösterilmiştir. 

- **Hata Önleme (Error Prevention):** Form alanlarına yanlış veri tipi (örneğin Tutar kısmına harf) girilmesi durumunda buton aktif olmaz ve kırmızı bir uyarı metni belirir. 

- **Geri Bildirim (Feedback):** Kullanıcının yaptığı her tıklama veya sayfa geçişi, anlık animasyonlar veya bildirim mesajları ile kullanıcıya hissettirilir; böylece sistemin donduğu hissiyatı önlenir. 

