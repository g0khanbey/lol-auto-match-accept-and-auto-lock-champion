# LoL Auto Match Accept & Auto Lock Champion  
**League of Legends otomatik maç kabul etme ve otomatik şampiyon kilitleme (pick/lock-in) aracı**

Bu program, League of Legends oynarken aşağıdaki işlemleri otomatik yapar:

- ✔️ **Maç bulunduğunda otomatik kabul eder**  
- ✔️ **Şampiyon arama kısmına otomatik yazı yazar**  
- ✔️ **Seçilen şampiyonu otomatik bulur ve tıklar**  
- ✔️ **Hazır (LOCK-IN) butonuna otomatik tıklar**

Program *tamamen görüntü işleme (OpenCV)* ve *mouse/klavye simülasyonu* ile çalışır.

⚠️ **Riot Games tarafından desteklenmez. Kullanım tamamen sizin sorumluluğunuzdadır.**

---

## 📌 Özellikler
- Tamamen Python ile yazılmıştır  
- OpenCV ile görsel tanıma  
- MSS ile ekran görüntüsü alma  
- Mouse & keyboard kontrolü  
- 1280x720 çözünürlük için optimize edildi  
- Hızlı ve sade UI (Tkinter)

---

## 📁 Proje Yapısı

```
src/
 ├── accept.png
 ├── hazir.png
 ├── ara.png
 └── champion_icons/
       ├── champions.txt
       ├── ahri.png
       ├── yasuo.png
       ├── zed.png
       └── ...
main.py
```

---

## 🔧 Gereksinimler (Requirements)

Aşağıdaki kütüphaneleri yükleyin:

```bash
pip install opencv-python numpy mss mouse keyboard
```

Eğer UI görünmezse:

```bash
pip install pywin32
```

---

## 📝 champions.txt Formatı

`src/champion_icons/champions.txt` dosyası şu formatta olmalıdır:

```
yasuo = yasuo.png
zed = zed.png
ahri = ahri.png
```

Sol taraf → şampiyon ismi  
Sağ taraf → aynı klasördeki resim dosyası

**Bütün şampiyon isimleri küçük harfle yazılmalıdır.**

---

## ▶️ Program Nasıl Kullanılır?

### 1️⃣ Programı Çalıştır
```bash
python main.py
```

### 2️⃣ UI Açıldığında:

### ✔️ **Maç Kabul Etme**
- **Başlat Maç Kabul** → sürekli accept.png arar ve otomatik tıklar  
- **Durdur Maç Kabul** → işlemi durdurur

---

### ✔️ **Şampiyon Arama + Otomatik Kilitleme**
1. “**Şampiyon İsmi**” bölümüne isim yaz  
2. **Ara + Şampiyon Kitle** butonuna bas  
3. Program:
   - ara.png butonunu bulur → tıklar  
   - İsmi otomatik yazar  
   - Şampiyon ikonunu bulur → tıklar  
   - hazir.png (LOCK-IN) butonunu bulur → tıklar  

---

## 📸 Önemli Notlar
- Program **1280x720** ekran çözünürlüğüne göre kalibre edilmiştir.  
- Farklı çözünürlükte hatalı tespit olabilir.  

---

## ⚠️ Uyarı
Bu yazılım **Riot Games tarafından desteklenmez**.  
Tespit edilirse ceza alabilirsiniz.  
Eğitim amaçlıdır.
Kullanım tamamen sizin sorumluluğunuzdadır.

---

## 🧑‍💻 Geliştirici
**Gökhan Altun**  
GitHub: https://github.com/g0khanbey

---

### ⭐ Projeyi beğendiysen repo'ya star vermeyi unutma!
