# Gerekli kütüphaneleri yüklüyoruz
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Veriyi yüklüyoruz
kanser = pd.read_csv('breast-cancer.csv')

# İlk 3 satırı görüntüleyerek veri hakkında hızlıca bilgi sahibi oluyoruz
kanser.head(3)

# Hedef değişken (bağımlı değişken) olan 'diagnosis' kolonunu y alıyoruz
y = kanser[['diagnosis']]

# Girdi değişkenleri (bağımsız değişkenler) olan diğer kolonları X olarak ayırıyoruz
# 'id' kolonunu modellemede kullanmadığımız için çıkarıyoruz
X = kanser.drop(['diagnosis', 'id'], axis=1)

# Veriyi eğitim ve test kümelerine ayırıyoruz
# %80 eğitim, %20 test verisi
# random_state=42 kullanarak her seferinde aynı bölünmeyi sağlıyoruz (tekrarlanabilirlik için)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Karar ağacı sınıflandırıcısını oluşturuyoruz
tree = DecisionTreeClassifier()

# Modeli eğitim verisi ile eğitiyoruz (fit)
model = tree.fit(X_train, y_train)

# Modelin test verisi üzerindeki doğruluk skorunu hesaplıyoruz
score = model.score(X_test, y_test)

# Doğruluk oranını ekrana yazdırıyoruz
print(f"Accuracy: {score:.2f}")
