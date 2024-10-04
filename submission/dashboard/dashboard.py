import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Menghilangkan peringatan FutureWarning
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Judul untuk dashboard
st.title('Analisis Penggunaan Sepeda Harian')

# Membaca data (dari sumber yang sama seperti sebelumnya)
df_day = pd.read_csv("https://raw.githubusercontent.com/anggerharyo/Proyek-Analisis-Data_Angger-Haryo-Putranto/main/dashboard/Bike_sharing_Dataset/day.csv")

# Menambahkan kolom untuk memisahkan hari kerja dan hari libur
df_day['Hari'] = df_day['workingday'].apply(lambda x: 'Hari Kerja' if x == 1 else 'Hari Libur')

# Pertanyaan 1: Rata-rata jumlah pengguna sepeda pada hari kerja vs hari libur
st.subheader('Rata-rata Pengguna Sepeda: Hari Kerja vs Hari Libur')

working_day_avg = df_day[df_day['workingday'] == 1]['cnt'].mean()
holiday_avg = df_day[df_day['workingday'] == 0]['cnt'].mean()

# Membuat DataFrame baru untuk visualisasi
avg_df = pd.DataFrame({
    'Hari': ['Hari Kerja', 'Hari Libur'],
    'Rata-rata Pengguna': [working_day_avg, holiday_avg]
})

# Visualisasi Barplot
fig, ax = plt.subplots()
sns.barplot(data=avg_df, x='Hari', y='Rata-rata Pengguna', color='red', ax=ax)
ax.set_title('Rata-rata Pengguna Sepeda: Hari Kerja vs Hari Libur')
ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
st.pyplot(fig)

# Menampilkan output teks
st.write(f"Rata-rata jumlah pengguna sepeda pada hari kerja adalah {working_day_avg:.2f} orang.")
st.write(f"Rata-rata jumlah pengguna sepeda pada hari libur adalah {holiday_avg:.2f} orang.")

# Line plot untuk tren pengguna sepeda berdasarkan hari kerja dan hari libur
st.subheader('Tren Pengguna Sepeda: Hari Kerja vs Hari Libur')
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

fig2, ax2 = plt.subplots(figsize=(10,6))
sns.lineplot(data=df_day, x='dteday', y='cnt', hue='Hari', palette='coolwarm', ax=ax2)
ax2.set_title('Tren Pengguna Sepeda: Hari Kerja vs Hari Libur')
ax2.set_xlabel('Tanggal')
ax2.set_ylabel('Jumlah Pengguna Sepeda')
plt.xticks(rotation=45)
st.pyplot(fig2)

# Histogram Pengguna Sepeda: Hari Kerja vs Hari Libur
st.subheader('Distribusi Pengguna Sepeda: Hari Kerja vs Hari Libur')
fig3, ax3 = plt.subplots(figsize=(8,6))
sns.histplot(data=df_day, x='cnt', hue='Hari', element='step', kde=True, palette='Set1', ax=ax3)
ax3.set_title('Histogram Pengguna Sepeda: Hari Kerja vs Hari Libur')
ax3.set_ylabel('Frekuensi')
ax3.set_xlabel('Jumlah Pengguna Sepeda')
st.pyplot(fig3)

# Pertanyaan 2: Bagaimana suhu mempengaruhi jumlah pengguna sepeda?
st.subheader('Pengaruh Suhu Terhadap Pengguna Sepeda')

# Menentukan kategori suhu
def categorize_temp(temp):
    if temp < 0.2:
        return 'Rendah'
    elif 0.2 <= temp < 0.6:
        return 'Sedang'
    else:
        return 'Tinggi'

df_day['Temp Kategori'] = df_day['temp'].apply(categorize_temp)

# Boxplot untuk distribusi pengguna sepeda berdasarkan kategori suhu
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df_day, x='Temp Kategori', y='cnt', palette='Set2', ax=ax4)
ax4.set_title('Distribusi Pengguna Sepeda Berdasarkan Kategori Suhu')
ax4.set_ylabel('Jumlah Pengguna Sepeda')
ax4.set_xlabel('Kategori Suhu')
st.pyplot(fig4)

# Violin plot untuk distribusi dan kepadatan pengguna sepeda
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.violinplot(data=df_day, x='Temp Kategori', y='cnt', palette='Pastel1', ax=ax5)
ax5.set_title('Kepadatan Pengguna Sepeda Berdasarkan Kategori Suhu')
ax5.set_ylabel('Jumlah Pengguna Sepeda')
ax5.set_xlabel('Kategori Suhu')
st.pyplot(fig5)

# Line plot untuk tren penggunaan sepeda dan suhu dari waktu ke waktu
st.subheader('Tren Penggunaan Sepeda dan Suhu dari Waktu ke Waktu')
fig6, ax6 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=df_day, x='dteday', y='cnt', label='Pengguna Sepeda', color='blue', ax=ax6)
sns.lineplot(data=df_day, x='dteday', y='temp', label='Suhu', color='orange', ax=ax6)
ax6.set_title('Tren Penggunaan Sepeda dan Suhu')
ax6.set_ylabel('Jumlah Pengguna Sepeda / Suhu')
ax6.set_xlabel('Tanggal')
plt.xticks(rotation=45)
ax6.legend()
st.pyplot(fig6)