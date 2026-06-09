## Web Arayüzü Tasarım ve Prototip Geliştirme Planı 

**Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI) 

## **1. Planın Amacı** 

Bu plan, makine öğrenimi modelimizin (Random Forest) tahminlerini son kullanıcılara (banka analistleri ve güvenlik ekipleri) sunacak olan web tabanlı arayüzün tasarım aşamalarını, kullanılacak teknolojileri ve Kullanıcı Arayüzü (UI) / Kullanıcı Deneyimi (UX) prensiplerini detaylandırmak amacıyla hazırlanmıştır. 

## **2. Arayüzün Temel İşlevleri ve Gereksinimler** 

Geliştirilecek arayüzün temel amacı, karmaşık veri bilimi sonuçlarını basit ve eyleme dönüştürülebilir görsel çıktılara çevirmektir. Arayüzün barındırması planlanan temel işlevler şunlardır: 

- **Veri Giriş Modülü:** Kullanıcının şüpheli bir işlemi anında kontrol edebilmesi için işlem tutarı, lokasyon, zaman ve cihaz bilgilerini girebileceği manuel bir form alanı. 

- **Toplu Analiz Modülü (CSV Yükleme):** Binlerce işlemin aynı anda sisteme yüklenip, model tarafından taranmasını sağlayacak dosya yükleme alanı. 

- **Sonuç Görselleştirme:** Modelin ürettiği %0 ile %100 arasındaki dolandırıcılık risk skorunun ilerleme çubukları (progress bars), renk kodları ve rozetler (badges) ile gösterilmesi. 

## **3. Kullanıcı Arayüzü (UI) ve Kullanıcı Deneyimi (UX) Prensipleri** 

Hedef kitlemiz teknik olmayan banka personeli olduğu için tasarımda şu UI/UX prensipleri benimsenecektir: 

- **Minimalizm ve Odaklanma:** Ekranda dikkat dağıtıcı hiçbir gereksiz unsur bulunmayacaktır. Odak noktası tamamen risk skoru ve işlemin durumu (Güvenli/Fraud) olacaktır. 

- **Renk Kodlaması (Color Coding):** İnsan psikolojisindeki evrensel uyarı renkleri kullanılacaktır. Yüksek riskli (Fraud) işlemler için Kırmızı/Bordo tonları, güvenli işlemler için Yeşil tonları, orta riskler için Sarı/Turuncu tonları tercih edilecektir. 

- **Hızlı Geri Bildirim:** Kullanıcı "Analiz Et" butonuna bastığında, sistemin arka planda çalıştığını gösteren dinamik bir "Yükleniyor (Loading)" animasyonu tasarlanacaktır. Bu sayede kullanıcının sistemin donduğunu düşünmesi engellenecektir. 

## **4. Kullanılacak Teknolojiler ve Geliştirme Araçları** 

Prototipin oluşturulması ve web arayüzünün geliştirilmesi için aşağıdaki teknoloji yığını (tech stack) seçilmiştir: 

- **Prototipleme ve Tel Çerçeve (Wireframe):** Arayüzün ilk görsel taslaklarını (mockup) oluşturmak için **Figma** tasarım aracı kullanılacaktır. 

- **Ön Yüz Geliştirme (Front-End):** * Sayfa iskeleti için **HTML5** . 

   - Modern, karanlık tema (Dark Mode) destekli ve kurumsal bir görünüm elde etmek için **CSS3** . 

   - Sayfa yenilenmeden asenkron veri akışını sağlamak ve UI animasyonlarını yönetmek için **Vanilla JavaScript (JS)** . _(Projenin hafif olması ve sunucu tabanlı (Flask) çalışması nedeniyle React veya Angular gibi ağır framework'ler yerine saf JS tercih edilmiştir)._ 

- **Arka Yüz Entegrasyonu (Back-End):** Python tabanlı modelin arayüze bağlanması için **Flask** web framework'ü kullanılacaktır. 

## **5. Erişilebilirlik (Accessibility) ve Sonuç** 

Tasarlanacak arayüz, farklı cihaz çözünürlüklerine (masaüstü ve tablet) uyumlu olacak şekilde duyarlı (responsive) olarak geliştirilecektir. Yazı tipleri okunabilir, kontrast oranları yüksek tutulacaktır. Bu plan doğrultusunda, arayüzün kodlama aşamasına geçilecek ve belirlenen UX prensipleri birebir koda dökülecektir. 

