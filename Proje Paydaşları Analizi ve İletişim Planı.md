## **Proje Paydaşları Analizi ve İletişim Planı** 

**Proje:** Yapay Zeka ile Kredi Kartı Dolandırıcılığı Tespiti (Fraud Shield AI) 

## **1. Planın Amacı** 

Bu belgenin amacı, "Kredi Kartı Dolandırıcılığı Tespiti" projesinin başarısı üzerinde doğrudan veya dolaylı etkiye sahip olan tüm kişi ve grupları (paydaşları) tanımlamak, beklentilerini analiz etmek ve proje yaşam döngüsü boyunca bu paydaşlarla kurulacak iletişim stratejisini belirlemektir. 

## **2. Proje Paydaşları Analizi** 

Projedeki paydaşlar, etki ve ilgi düzeylerine göre sınıflandırılmış ve beklentileri aşağıdaki gibi analiz edilmiştir: 

## **A. Birincil Paydaşlar (Yüksek Etki - Yüksek İlgi)** 

- **Proje Danışmanı / Akademik Kurul (Sponsorlar):** 

   - **Rolü:** Projenin akademik standartlara uygunluğunu denetler ve nihai notlandırmayı/onayı yapar. 

   - **Beklentileri:** Projenin zaman çizelgesine uyulması, yenilikçi bir yapay zeka çözümü (Random Forest vb.) sunulması, detaylı dokümantasyon ve sorunsuz çalışan bir canlı sunum (demo). 

- **Proje Yöneticisi (Ahmed):** 

   - **Rolü:** Ekip koordinasyonunu sağlamak, görev dağılımını yapmak ve projenin genel ilerleyişini denetlemek. 

   - **Beklentileri:** Ekip üyelerinin görevlerini zamanında teslim etmesi, iletişim kanallarının aktif kullanılması ve ortaya çıkan krizlerin (teknik veya idari) hızlı çözülmesi. 

- **Geliştirme ve Veri Ekibi (Mustafa, Felek):** 

   - **Rolü:** Veri ön işleme, makine öğrenimi modellerinin eğitilmesi, API entegrasyonu ve Web arayüzünün (Front-End/Back-End) geliştirilmesi. 

   - `o` **Beklentileri:** Net görev tanımları (Requirement belgelendirmesi), kod çakışmalarını önleyecek versiyon kontrol (Git) altyapısı ve uyumlu bir takım çalışması. 

## **B. İkincil Paydaşlar (Yüksek Etki - Orta İlgi)** 

- **Değerlendirme Jürisi:** 

   - **Rolü:** Dönem sonunda projenin teknik derinliğini ve pratik faydasını değerlendirmek. 

   - **Beklentileri:** Sistemin nasıl çalıştığını gösteren hatasız bir arayüz, teknik sorulara (metrikler, algoritma seçimi vb.) tatmin edici cevaplar ve anlaşılır bir sunum. 

## **C. Üçüncül Paydaşlar (Düşük Etki - Yüksek İlgi)** 

- **Son Kullanıcılar (Simüle Edilen Banka Personeli / Müşteriler):** 

   - **Rolü:** Geliştirilen Fraud Shield arayüzünü kullanarak işlemleri denetleyecek kitle. 

   - **Beklentileri:** Hızlı tahmin süreleri, düşük yanlış alarm (False Positive) oranı, kullanıcı dostu ve anlaşılır bir gösterge paneli (Dashboard). 

## **3. İletişim Planı** 

Paydaşların düzenli olarak bilgilendirilmesi ve geri bildirimlerin alınması için aşağıdaki iletişim matrisi kullanılacaktır: 

|**İletişim Türü**|**Hedef**<br>**Kitle**|**İletişim**<br>**Kanalı**|**Sıklık**|**İçerik ve**<br>**Amaç**|
|---|---|---|---|---|
|**Danışman**<br>**Görüşmeleri**|Proje<br>Danışmanı<br>, Proje<br>Yöneticisi|Yüz yüze<br>/ E-posta|Haftalık /<br>İki Haftada<br>Bir|Haftalık<br>ilerleme<br>raporlarının<br>sunulması,<br>akademik<br>geri bildirim<br>alınması ve<br>onayların<br>(milestones)<br>geçilmesi.|
|**Ekip İçi**<br>**Senkronizasyo**<br>**n**|Tüm<br>Geliştirme<br>Ekibi|WhatsAp<br>p /<br>Discord /<br>Slack|Günlük /<br>Haftada 3<br>Gün|Günlük<br>yapılan<br>işlerin (Daily<br>Scrum)<br>paylaşılması,<br>karşılaşılan<br>teknik<br>engellerin<br>(bug) hızlıca<br>tartışılıp<br>çözülmesi.|



|**İletişim Türü**|**Hedef**<br>**Kitle**|**İletişim**<br>**Kanalı**|**Sıklık**|**İçerik ve**<br>**Amaç**|
|---|---|---|---|---|
|**Kod ve**<br>**Doküman**<br>**Paylaşımı**|Tüm<br>Geliştirme<br>Ekibi|GitHub /<br>Google<br>Drive|Sürekli<br>(Asenkron<br>)|Versiyon<br>kontrolü,<br>kodların<br>birleştirilmes<br>i ve proje<br>raporlarının<br>eşzamanlı<br>olarak<br>yazılması.|
|**Final Sunumu**<br>**(Demo)**|Jüri,<br>Danışman,<br>Ekip|Konferans<br>Salonu|Proje<br>Sonunda<br>(1 Kez)|Çalışan<br>sistemin canlı<br>testi, sunum<br>dosyası<br>(PPTX)<br>eşliğinde<br>analizlerin ve<br>bulguların<br>savunulması.|



## **4. Paydaş Katılımını En Üst Düzeye Çıkarma Stratejileri** 

Proje sürecinde kopuklukları önlemek ve katılımı artırmak için şu stratejiler benimsenecektir: 

1. **Görsel ve Pratik Geri Bildirim:** Danışman hoca ve ekiple yapılan toplantılarda sadece kod veya teorik metrikler üzerinden değil, _çalışan arayüz prototipi_ üzerinden konuşulacaktır. İnsanların görsel bir sistemle etkileşime girmesi geri bildirim kalitesini artırır. 

2. **Şeffaf Engel Yönetimi:** Herhangi bir üye teknik bir tıkanıklık yaşadığında (Örn: Modelin sürekli %0 veya %99 vermesi gibi durumlar), bu durum anında ekip içi iletişim kanalından şeffafça paylaşılacak ve ortak beyin fırtınası yapılacaktır. 

3. **Dokümantasyon Erişilebilirliği:** Tüm raporlar, kodlar ve veri setleri merkezi bir bulut sürücüsünde tutulacak, böylece her paydaş güncel duruma dilediği an ulaşabilecektir. 

