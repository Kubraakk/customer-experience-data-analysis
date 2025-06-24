# Gerekli kütüphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
df = pd.read_csv("/customer-experience-data-analysis/customer_experience_data.csv")

print("***Veri Seti Genel Bakış***\n")
print("\nVeri Seti İlk 5 Satır:\n")
print(df.head())
print("\nVeri Boyutu:\n")
print( df.shape)
print("\nVeri Tipleri ve Eksik Değerler:\n")
print(df.info())
print("\nSayısal Özet:\n")
print(df.describe(include='all'))

# Sadece sayısal sütunlar
numerical_df = df.select_dtypes(include=["int64", "float64"])

# describe() ile temel istatistikler
summary = numerical_df.describe().T

# Medyan ve çeyrekleri ekleyelim
summary["median"] = numerical_df.median()
summary["Q1 (25%)"] = numerical_df.quantile(0.25)
summary["Q3 (75%)"] = numerical_df.quantile(0.75)

summary

# Her sütundaki eksik değer sayısını ve yüzdesi
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100

missing_df = pd.DataFrame({
    'Eksik Değer Sayısı': missing,
    'Yüzde (%)': missing_percent
})

# Sadece eksik değeri olan sütunları filtreleme
missing_df = missing_df[missing_df["Eksik Değer Sayısı"] > 0]

missing_df

# Sayısal sütunlar
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

# Aykırı değerlerin sayısını içeren tablo
outlier_summary = {}

# IQR yöntemiyle aykırı değer analizi
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outlier_summary[col] = {
        "Toplam Gözlem": df.shape[0],
        "Aykırı Değer Sayısı": outliers.shape[0],
        "Aykırı Değer Oranı (%)": round(outliers.shape[0] / df.shape[0] * 100, 2)
    }

# Sonuçları DataFrame olarak gösterme
import pandas as pd
outlier_df = pd.DataFrame(outlier_summary).T.sort_values(by="Aykırı Değer Oranı (%)", ascending=False)
outlier_df

import matplotlib.pyplot as plt
import seaborn as sns

# Grafik boyutu
plt.figure(figsize=(15, 10))

# Sayısal değişkenleri döngüyle çiz
for i, col in enumerate(num_cols):
    plt.subplot(4, 3, i+1)
    sns.boxplot(x=df[col], color='skyblue')
    plt.title(col)
    plt.tight_layout()

plt.suptitle("Sayısal Değişkenlerde Aykırı Değer Analizi (Boxplot)", y=1.02, fontsize=16)
plt.show()

# Histogram + KDE (Kernel Density Estimation)
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15, 12))
for i, col in enumerate(num_cols):
    plt.subplot(4, 3, i+1)
    sns.histplot(df[col], kde=True, bins=20, color='cornflowerblue')
    plt.title(f"{col} Dağılımı")
    plt.xlabel(col)
    plt.ylabel("Frekans")
    plt.tight_layout()

plt.suptitle("Sayısal Değişkenlerin Dağılımı", y=1.02, fontsize=16)
plt.show()

cat_cols = df.select_dtypes(include='object').columns.tolist()
cat_cols

plt.figure(figsize=(15, 5))
for i, col in enumerate(cat_cols):
    plt.subplot(1, 3, i+1)
    sns.countplot(data=df, x=col, palette='Set2')
    plt.title(f"{col} Dağılımı")
    plt.ylabel("Adet")
    plt.xticks(rotation=20)
    plt.tight_layout()

plt.suptitle("Kategorik Değişkenlerin Frekans Grafiği", y=1.05, fontsize=16)
plt.show()