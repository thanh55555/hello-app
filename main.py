

# URL: https://web-project415.streamlit.app/


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")

# Các data đc thay thế với các giá trị trung bình
df['budget'].fillna(df['budget'].mean(), inplace=True)
df['gross'].fillna(df['gross'].mean(), inplace=True)
df['runtime'].fillna(df['runtime'].mean(), inplace=True)
df['score'].fillna(df['score'].mean(), inplace=True)
df['votes'].fillna(df['votes'].mean(), inplace=True)


st.sidebar.title("Chức năng")
min_year = df['year'].min()
max_year = df['year'].max()

chon_phim = st.sidebar.selectbox("Chọn phim:", df['name'].unique())
chon_nam = st.sidebar.slider("Chọn năm phát hành:", min_year, max_year, value = 2000)

st.title("Phân tích dữ liệu ")
st.subheader("Thông tin phim:")
st.write(df[df['name'] == chon_phim])

st.subheader(f"Danh sách phim phát hành năm {chon_nam}")
st.write(df[df['year'] == chon_nam][['name', 'rating', 'genre', 'budget', 'gross', 'score']])

df_new = df[df['year'] == chon_nam]

# 1
st.subheader("Biểu đồ scatter giữa Ngân sách và Doanh thu")
fig1 = plt.figure(figsize=(10, 6))
plt.scatter(df_new['budget'], df_new['gross'], color='blue', alpha=0.6)
plt.xlabel("Ngân sách (USD)")
plt.ylabel("Doanh thu (USD)")
st.pyplot(fig1)

#22
st.subheader("Ngân sách trung bình theo thể loại")
avg_budget = df_new.groupby('genre')['budget'].mean().round().reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

fig2 = plt.figure(figsize=(10, 6))
plt.barh(genre, avg_bud, color='mediumseagreen')
plt.xlabel('Ngân sách trung bình')
plt.ylabel('Thể loại')
st.pyplot(fig2)


st.subheader('Biểu đồ Phân phối Điểm số của các Bộ Phim')
fig3 = plt.figure(figsize=(10, 6))
plt.hist(df_new['score'], bins=20, color='red', alpha=0.7, label='Điểm số')
plt.xlabel('Điểm số')
plt.ylabel('Tần suất')
st.pyplot(fig3)
