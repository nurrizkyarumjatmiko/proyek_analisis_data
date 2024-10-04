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

# Menambahkan bagian untuk analisis clustering penggunaan sepeda berdasarkan musim dan hari kerja
st.subheader('Clustering Penggunaan Sepeda Berdasarkan Musim dan Hari Kerja')

# DataFrame `usage_summary` (Pastikan Anda sudah memiliki data ini, misalnya dari analisis clustering sebelumnya)
# Berikut adalah contoh bagaimana data tersebut bisa dibuat
# usage_summary = df.groupby(['season', 'Cluster']).agg({'cnt': 'mean'}).reset_index()

# Untuk contoh ini, kita akan menggunakan data buatan
# Anda bisa mengganti bagian ini dengan data yang sudah ada
season_order = ['Winter', 'Spring', 'Summer', 'Fall']
clusters = ['Cluster 1', 'Cluster 2', 'Cluster 3']  # Contoh cluster
usage_summary = pd.DataFrame({
    'season': ['Winter', 'Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall'],
    'cnt': [300, 400, 800, 600, 350, 450, 850, 650, 330, 380, 780, 620],
    'Cluster': ['Cluster 1', 'Cluster 1', 'Cluster 1', 'Cluster 1', 'Cluster 2', 'Cluster 2', 'Cluster 2', 'Cluster 2', 'Cluster 3', 'Cluster 3', 'Cluster 3', 'Cluster 3']
})

# Membuat plot dengan peningkatan visual
fig7, ax7 = plt.subplots(figsize=(14, 8))
scatter_plot = sns.scatterplot(
    data=usage_summary, 
    x='season', 
    y='cnt', 
    hue='Cluster', 
    palette='coolwarm', 
    s=200,  # Ukuran titik lebih besar
    legend='full', 
    ax=ax7
)

# Menambahkan anotasi pada setiap titik dengan nilai penggunaan sepeda
for i in range(usage_summary.shape[0]):
    ax7.text(
        usage_summary['season'][i], 
        usage_summary['cnt'][i] + 50,  # Sedikit di atas titik
        usage_summary['cnt'][i], 
        horizontalalignment='center', 
        size='medium', 
        color='black', 
        weight='semibold'
    )

# Menambahkan informasi visual tambahan
ax7.set_title('Clustering Penggunaan Sepeda Berdasarkan Musim dan Hari Kerja', fontsize=18, weight='bold')
ax7.set_xlabel('Musim', fontsize=14, weight='bold')
ax7.set_ylabel('Rata-rata Penggunaan Sepeda', fontsize=14, weight='bold')
ax7.set_xticks(range(len(season_order)))
ax7.set_xticklabels(season_order, fontsize=12)
ax7.tick_params(axis='y', labelsize=12)

# Mengatur posisi legenda di luar grafik agar tidak menghalangi
ax7.legend(title='Cluster', title_fontsize='13', fontsize='11', bbox_to_anchor=(1.05, 1), loc='upper left')

# Tampilkan plot dengan grid yang halus
ax7.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
st.pyplot(fig7)