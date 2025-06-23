
# README.md

Streamlit ini akan dijalankan langsung dari google collab dan bukan dari sistem komputer local. Sehingga saya menggunakan referensi lain untuk menghubungankan streamlit dengan google collab.


## Referensi

 - [Tutorial menghubungkan google collab dan anaconda](https://www.youtube.com/watch?v=ZZsyxIWdCko)

## Buka file dashboard.py
Buka file dashboard.py dari Google Collab dan lakukan copy path. 

## Menjalankan streamlit di notebook

Install streamlit dan localtunnel

```python
  !pip install streamlit
  !npm install localtunnel
```
Kemudian jalankan streamlit dan localtunnel

```python
  !streamlit run app.py &>/content/logs.txt &
```
Untuk mencari ip address

```python
  !wget -q -O - ipv4.icanhazip.com
```
Untuk menjalankan dashboard di tab browser baru
Sebelumnya salin path dari file dashboard.py

```python
  ! streamlit run /content/drive/MyDrive/Proyek_Akhir_Dicoding_Analisis_Data/Dashboard/dashboard.py & npx localtunnel --port 8501
```
Setelah langkah di atas, akan tampil output berupa: Local url, Network url, External URL, dan link running dashboard. 

Buka link tersebut

Setelah di buka, masukkan IP address 

Streamlit sudah berjalan





