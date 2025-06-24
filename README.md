# Müşteri Deneyimi Veri Analizi Bitirme Projesi

Bitirme projesi kapsamında sunulan veri setlerinden "Customer Experience Dataset" adlı veri seti analiz edilmiştir.
Amaç, istatistiksel özet çıkarımı, eksik değer analizi, aykırı değer tespiti ve uygun görselleştirmeler ile eğitim boyunca öğrenilenler ile veri  analizi becerilerini geliştirmektir. 

## 1. Veri Seti Genel Tanıtımı

Veri seti, 1000 müşteri gözlemi ve 14 değişken içermektedir. Bu değişkenler müşteri profili, etkileşim sayısı, memnuniyet düzeyi gibi bilgileri içermektedir.
Aşağıda veri setinin ilk 5 satırı ve genel yapısı verilmiştir.

![Ekran Resmi 2025-06-24 22 04 50](https://github.com/user-attachments/assets/61bd5763-31c5-456d-b446-4d8547e55627)

## 2. İstatistiksel Özet

Veri setindeki sayısal değişkenlerin merkezi eğilim (ortalama, medyan), dağılım ölçüleri (standart sapma, min, max) ve çeyrek değerleri hesaplanmıştır.

![Ekran Resmi 2025-06-24 22 05 30](https://github.com/user-attachments/assets/6c6b5819-7988-411e-93a9-f9cc1fbd9774) 

## 2.1. İstatistiksel Özet Yorumu
Veri setinde yer alan sayısal değişkenler için temel istatistiksel ölçümler (ortalama, medyan, min, max, çeyrekler) özetlenmiştir:

- **Age (Yaş)**:
  - Ortalama yaş 43.8, medyan 44 → yaş dağılımı oldukça dengeli.
  - Minimum yaş 18, maksimum 69 → geniş bir yaş aralığı var.
  - 25% ve 75% değerleri (31, 56) arasında kalan kullanıcılar çoğunlukta.

- **Num_Interactions (Etkileşim Sayısı)**:
  - Ortalama 7.54, medyan 8 → kullanıcıların çoğu 7-8 etkileşimde bulunmuş.
  - 14’e kadar çıkan kullanıcılar olabilir (muhtemelen aktif kullanıcılar).

- **Feedback_Score (Geri Bildirim Skoru)**:
  - Ortalama 2.98, medyan 3 → skorlar genel olarak 1–5 aralığında ve dengeli dağılmış.
  - Minimum: 1, Maksimum: 5 → sabit bir puanlama sistemi kullanılmış.

- **Products_Purchased (Satın Alınan Ürün)**:
  - Ortalama 10.41, medyan 11 → kullanıcılar ortalama 10–11 ürün satın almış.
  - Maksimum 19 → bazı kullanıcılar çok daha fazla satın alma yapmış olabilir.

- **Time_Spent_on_Site (Sitede Harcanan Süre)**:
  - Ortalama ≈ 32.3 dakika, medyan ≈ 32.5 dakika → normal dağılıma yakın.
  - Minimum 5 dakika, maksimum ≈ 60 dakika → bazı kullanıcılar çok kısa kalmış.

- **Satisfaction_Score (Memnuniyet Puanı)**:
  - Ortalama 5.54, medyan 6 → genel memnuniyet seviyesi orta seviyede.
  - Minimum 1, maksimum 10 → tam skala kullanılmış.

- **Gender_Encoded ve Location_Encoded**:
  - Gender_Encoded ortalaması 0.52 → kullanıcıların yaklaşık %52’si erkek.
  - Location_Encoded ortalaması 1.03 → farklı lokasyonlardan dengeli veri gelmiş.

- **Retention_Status_Encoded (Sadakat Durumu)**:
  - Ortalama ≈ 0.69 → kullanıcıların yaklaşık %69’u sistemde tutulmuş.

İstatistikler, hem kullanıcıların genel davranışları hem de modellemeye temel oluşturacak veri yapısı hakkında bilgi verir.

## 3. Eksik Değer Analizi

Veri setindeki sütunlarda eksik değer (null) olup olmadığı kontrol edilmiştir.
Eksik veri olması durumunda, bu verilerin silinmesi, ortalama/medyan ile doldurulması veya tahminsel yöntemlerle tamamlanması gibi yöntemler değerlendirilecektir.

## 3.1. Eksik Veri Analizi Sonuçları

Veri seti üzerinde yapılan eksik değer (null) analizi sonucunda, **hiçbir sütunda eksik gözlem bulunmadığı** tespit edilmiştir.Verinin temiz olduğunu ve doğrudan analiz veya modelleme çalışmalarına uygun olduğu gözlemlenmiştir.

## 4. Aykırı Değer (Outlier) Analizi

Veri setindeki sayısal değişkenlerde bulunan **aykırı (uç) değerler**, IQR (Interquartile Range) yöntemiyle analiz edilmiştir.

Aykırı değerler, veri setinde istatistiksel olarak olağan dışı olan gözlemler olarak tanımlanır. Bunlar, model performansını düşürebileceği için dikkatle analiz edilmelidir.

![Ekran Resmi 2025-06-24 22 07 46](https://github.com/user-attachments/assets/6ded9212-e76a-4dde-8fb0-078a6cb3d7a2)

## 4.1. Aykırı Değer Analizi Sonuçları

IQR (Interquartile Range) yöntemi ile yapılan aykırı değer analizi sonucunda, **hiçbir sayısal sütunda aykırı değer tespit edilmemiştir**.
Veri setinin istatistiksel açıdan oldukça düzenli olduğunu ve analiz ya da modelleme öncesi aykırı değer temizliği yapılmasına gerek olmadığını göstermektedir.
Bu durum veri kalitesini artırır ve analiz sonuçlarının daha güvenilir olmasını sağlar. 

## 4.2. Aykırı Değerlerin Görselleştirilmesi (Boxplot)

Aşağıdaki kutu grafiklerinde, her sayısal değişkenin dağılımı ve potansiyel aykırı değerleri görselleştirilmiştir. Boxplot (kutu grafiği), verinin medyanını, çeyreklerini ve uç değerlerini grafiksel olarak gösterir.
![Ekran Resmi 2025-06-24 22 09 13](https://github.com/user-attachments/assets/7b9c2a18-fb79-48ac-96ac-3681a9459051)

## 4.3. Aykırı Değerlerin Görsel İncelemesi

Boxplot grafikleri, veri setindeki sayısal değişkenlerin dağılımını ve olası aykırı değerleri göstermektedir.Her bir grafik, değişkenin medyanını, çeyrek değerlerini ve uç değerlerini açıkça görselleştirir.

### Yorum:
- Tüm sayısal değişkenlerde veri dağılımı oldukça dengelidir.
- **Hiçbir değişkende aykırı (uç) gözlem noktası bulunmamaktadır.**
- Verinin istatistiksel olarak temiz olduğunu ve modelleme aşamasında uç değer kaynaklı bozulmalar yaşanmayacağını gösterir.

## 5. Veri Görselleştirme

Veri setindeki sayısal ve kategorik değişkenlerin dağılımı görselleştirilmiştir.
- **Sayısal değişkenler** için histogram ve yoğunluk eğrileri (KDE) kullanılmıştır.
- **Kategorik değişkenler** için frekans grafikleri (countplot) kullanılmıştır.
Görseller verinin genel yapısını anlamamıza, uç değerleri fark etmemize ve değişkenlerin dağılımı hakkında fikir edinmemize yardımcı olur.
![Ekran Resmi 2025-06-24 22 11 07](https://github.com/user-attachments/assets/778519b2-0bb4-40ef-8745-942612b6f2e5)

### 5.2. Kategorik Değişkenlerin Dağılımı

Kategorik değişkenler için sütun grafikleri kullanılarak frekans dağılımları görselleştirilmiştir:
- `Gender`: Erkek ve kadın dağılımı dengelidir (yaklaşık yarı yarıya).
- `Location`: Kullanıcılar Urban, Suburban ve Rural bölgeler arasında eşit dağılmıştır.
- `Retention_Status`: Retained (sitede kalan) kullanıcı sayısı, Churned (kaybedilen) kullanıcı sayısından belirgin şekilde fazladır.
Grafikler, veri setindeki kategorik dengesizliklerin fark edilmesine ve olası veri ön işleme ihtiyaçlarının tespit edilmesine katkı sağlar.

![Ekran Resmi 2025-06-24 22 11 50](https://github.com/user-attachments/assets/41d606e1-7697-4c43-822d-8c450efc1aa2)

## 6. Sonuç ve Değerlendirme

Proje kapsamında, müşteri deneyimini ölçen bir veri seti üzerinde temel veri analizi adımları gerçekleştirilmiştir. Elde edilen bulgular aşağıda özetlenmiştir:
- **İstatistiksel Özet:** Sayısal değişkenler için ortalama, medyan, standart sapma gibi temel istatistikler hesaplanarak verinin merkezi eğilimleri ve dağılımları incelenmiştir.
- **Eksik Değer Analizi:** Veri setinde eksik değer bulunmamaktadır, bu nedenle herhangi bir doldurma veya veri silme işlemi uygulanmamıştır.
- **Aykırı Değer Analizi:** Boxplot ve IQR yöntemine dayalı analizler sonucunda aykırı değer gözlemlenmemiştir. Bu da verinin temiz ve analiz için uygun olduğunu göstermektedir.
- **Görselleştirme:** Sayısal değişkenler için histogram ve KDE eğrileri, kategorik değişkenler için sütun grafikler kullanılmıştır. Bu sayede kullanıcı davranışları, ürün etkileşimleri ve memnuniyet düzeyleri hakkında görsel içgörüler elde edilmiştir.








