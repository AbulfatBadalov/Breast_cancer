Bu proje, Decision Tree Classifier kullanarak meme kanseri teşhisi yapmayı amaçlamaktadır.
Veri seti, çeşitli tümör özelliklerini içerir ve her örnek "Malignant" (kötü huylu) veya "Benign" (iyi huylu) olarak sınıflandırılmıştır.

📂 Proje İçeriği
Veri Yükleme: breast-cancer.csv dosyası okunur.

Veri Hazırlama:

diagnosis (teşhis) hedef değişken (y) olarak seçildi.

id sütunu çıkarıldı ve kalan özellikler giriş verisi (X) olarak belirlendi.

Veri Bölme:

Veriler %80 eğitim ve %20 test seti olarak ayrıldı (train_test_split).

Model Eğitimi:

DecisionTreeClassifier kullanılarak model eğitildi.

Model Değerlendirme:

Test verisi üzerinde doğruluk oranı (accuracy) hesaplandı ve yazdırıldı.

🛠 Kullanılan Teknolojiler
Python 3

Pandas

NumPy

scikit-learn

📈 Sonuç
Model, test verisi üzerinde yaklaşık %94 doğruluk oranı elde etmiştir.
(Çalıştırdığında tam sonucu yerine koyabilirsin.)

📄 Notlar
Daha iyi sonuçlar almak için model hiperparametreleri (max_depth, min_samples_split gibi) ayarlanabilir.

Ek olarak, model başarımını detaylı görmek için confusion matrix, classification report gibi araçlar da kullanılabilir.

✨ İleride Geliştirilebilecekler
Karar ağacı görselleştirme eklenebilir.

Feature importance analiz edilerek en etkili özellikler belirlenebilir.

Farklı modeller (Random Forest, SVM gibi) ile karşılaştırmalı çalışmalar yapılabilir.

👩‍💻 Hazırlayan
**Badalov Abulfat**
