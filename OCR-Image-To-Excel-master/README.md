**Tesseract ile görsel verilerin dijital ortama aktarılması**



<img src="https://github.com/fikretsefa/OCR-Image-To-Excel/blob/master/tesseract.png" width="500" >

Tesseract, çeşitli işletim sistemleri için geliştirilen özgür bir optik karakter tanıma (OCR) motorudur.

Projeyi çalıştırmanız ve Tesseract kullanmanız için indirmeniz ve kurulum yapmanız gerekmektedir.

<a target="_blank" href="https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v4.0.0-beta.4.20180912.exe">Tesseract (32)</a>

<a target="_blank" href="https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.0.0-beta.4.20180912.exe">
Tesseract (64)</a>

Kurulum sırasında Türkçe çevirim yapmak için *Additional language data (download)* seçeneğinden Türkçe'yi seçmeniz gerekmektedir.

Dönüştürülecek görsel Türkçe'nin içerisinde olduğu gibi Fransızca, İngilizce vb. kelimeler içerebileceğinden tümünü indirmeniz fayda sağlayacaktır.

Ardından *pip install pytesseract* ve *pip install Pillow* ile projede kullancağımız python kütüphanelerini kuruyoruz.

*test* klasörünün içerisine attığınız görsellerin text versiyonu excel içerisinde oluşturulmuş olacaktır.


