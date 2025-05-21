## Text File Analyzer
Text File Analyzer, bir metindeki cümleleri ayrıştırarak temel istatistiksel ve anlamsal analizler gerçekleştiren bir Python uygulamasıdır. Uygulama, cümle uzunluğu, en uzun ve en kısa kelime, duygu analizi (sentiment analysis) gibi çeşitli metin özelliklerini çıkarır.

## Özellikler
- Toplam kelime sayısı.
- Cümleleri ayrıştırma.
- Metindeki en uzun ve en kısa kelime.
- Her cümledeki kelimelerin listesi.
- Her cümlede kaç tane kelime var.
- Cümle bazlı duygu analizi. (Polarity & Subjectivity)
- En fazla kelime sayısına sahip cümle.

## Kurulum
Depoyu klonlayın:

```bash
git clone https://github.com/osmantalayhan/text-file-analyzer.git
cd text-file-analyzer
```
Gerekli Python sürümünü kontrol edin:

Bu proje, Python 3 ile uyumludur. Python'un yüklü olduğundan emin olun.

## Kullanım
Analiz etmek istediğiniz metin dosyasını hazırlayın.

Uygulamayı çalıştırın:

```bash
python main.py
```

Analiz sonuçları terminalde görüntülenecektir.

## Dosya Yapısı
- main.py: Uygulamanın giriş noktasıdır.
- analyzer.py: Metin analiz işlemlerini gerçekleştiren modüldür.
- overview.txt: Ornek metin bulunur.

## Kullanılan Kütüphane
- TextBlob
