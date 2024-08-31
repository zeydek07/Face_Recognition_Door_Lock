Yüz tanıma sistemi kullanarak kapı kilidini açan bir güvenlik sistemi geliştirmeyi amaçlar. Sistem, Raspberry Pi ve çeşitli Python kütüphaneleri kullanılarak oluşturulmuştur. Kamera, önceden tanımlanmış yüzleri tanıyarak kilidi açar.

Kurulum Adımları:
Gerekli Donanımlar:

Raspberry Pi 2 Model B
USB Web Kamerası
Elektromıknatıslı Solenoid Valf
L298 Motor Sürücü
Raspberry Pi Ayarları:

SSH ayarları yapılır, böylece Raspberry Pi'ye uzaktan erişim sağlanır.
Kamera modülü aktif hale getirilir.
Ağ Bağlantısı:

Raspberry Pi’nin internet bağlantısı paylaştırılır.
Sanal Ortam ve Python Kütüphanelerinin Kurulumu:

virtualenv kullanılarak bir sanal ortam oluşturulur.
Gerekli Python kütüphaneleri (dlib, Pillow, numpy, face_recognition, opencv-contrib-python, Rpi.GPIO) bu sanal ortama kurulur.
Yazılım Aşaması:

Face_Recog.py dosyası ile yüz tanıma işlemleri gerçekleştirilir.
Face_Trainer.py dosyası ile yüz tanıyıcı model eğitilir.


Raspberry Pi Ayarları: Raspberry Pi’nin SSH bağlantısı Mobaxterm ile kurulur. Kamera arayüzü terminalden aktif hale getirilir.
Python Kütüphaneleri Kurulumu: Terminal komutları ile gerekli kütüphaneler kurulur. Opencv kütüphanesi piwheels.org üzerinden indirilip kurulmuştur.
Yazılım: Yüz tanıma işlemleri, kamera görüntülerinin işlenmesiyle gerçekleştirilir.
Bu adımların izlenmesiyle proje çalışır hale getirilecektir. İleride, daha yüksek çözünürlüklü kameralar eklenerek sistem geliştirilebilir.
