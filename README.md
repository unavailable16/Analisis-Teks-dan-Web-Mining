# Analisis-Teks-dan-Web-Mining
Tugas Akhir Data Mining Kel1 04TPLP035
Ahdan Setya Ananta (241011401331)
Dina Aura Nur (241011401694)
Aji Mulya Wardana (241011401335)

- Video Presentasi : https://youtu.be/fhSyJeT-8Dg
- Dataset : https://drive.google.com/file/d/1cBq_e5m2yr5yH99bmmnPzfWxyaf9rGjg/view?usp=sharing

  ## Laporan
### Pendahuluan
Analisis teks (text mining) merupakan proses mengekstraksi informasi dan pengetahuan dari data berbentuk teks yang tidak terstruktur. Saat ini sebagian besar data yang dihasilkan organisasi berasal dari email, dokumen, media sosial, review produk, dan berbagai sumber teks lainnya. Melalui text mining, data tersebut dapat diubah menjadi informasi yang berguna untuk pengambilan keputusan.

Contoh penerapan analisis teks meliputi analisis sentimen, spam filtering, chatbot, search engine, topic modeling, dan question answering.

### Text Preprocessing
Text preprocessing adalah tahap awal yang bertujuan membersihkan data teks sebelum dianalisis. Tahapan utama meliputi:

a. Tokenization
Memecah kalimat menjadi token-token atau kata.

b. Lowercasing
Mengubah seluruh huruf menjadi huruf kecil.

c. Stopword Removal
Menghapus kata-kata umum seperti 'dan', 'yang', 'the', dan 'is' yang tidak memberikan informasi penting.

d. Stemming dan Lemmatization
Mengubah kata menjadi bentuk dasarnya sehingga variasi kata dapat dianggap sama.

### Representasi Teks
Setelah preprocessing, teks harus diubah menjadi bentuk numerik.

Bag of Words (BoW):
Representasi berdasarkan frekuensi kemunculan kata dalam dokumen.

TF-IDF:
Memberikan bobot tinggi pada kata yang sering muncul pada suatu dokumen namun jarang muncul pada keseluruhan korpus sehingga lebih informatif dibanding BoW.

### Web Mining
Web Mining adalah proses menggali informasi dari data yang tersedia di web.

Jenis Web Mining:
1. Web Content Mining: mengekstraksi informasi dari isi halaman web.
2. Web Structure Mining: menganalisis hubungan antar halaman melalui hyperlink.
3. Web Usage Mining: menganalisis perilaku pengguna berdasarkan log aktivitas.

Contoh aplikasi:
- Search Engine
- Sistem Rekomendasi
- Analisis Perilaku Pengguna
- Monitoring Harga Produk
  
### Project: Analisis Sentimen Dataset IMDB
Tujuan project adalah mengklasifikasikan review film menjadi sentimen positif atau negatif menggunakan dataset IMDB.

Tahapan:
1. Membaca dataset.
2. Membersihkan teks.
3. TF-IDF Vectorization.
4. Training model Naive Bayes.
5. Evaluasi model.
6. Prediksi review baru.

Contoh review:
Positif: "This movie was fantastic and amazing."
Negatif: "This movie was boring and a waste of time." 

### Code 
<img width="715" height="975" alt="image" src="https://github.com/user-attachments/assets/60097e35-301e-49fd-900c-d6996d15da1d" />
<img width="417" height="942" alt="image" src="https://github.com/user-attachments/assets/cfe94913-67e9-4648-9789-a8200215b665" />
<img width="381" height="145" alt="image" src="https://github.com/user-attachments/assets/d21e7d09-d3ef-4feb-ab6f-faa38b728d2d" />

### Output 
<img width="569" height="860" alt="image" src="https://github.com/user-attachments/assets/d77b697c-227e-4384-8527-a34e62b0523b" />

### Penjelasan Output 
1. Untuk Tahap TF-IDF Matrix
50.000 adalah jumlah data review, sedangkan 5000 adalah jumlah kata penting yang dipilih sistem sebagai fitur analisis.
   
2. Untuk Tahap Accuracy Model
   Hasil evaluasi menunjukkan nilai akurasi sebesar 0.8489 atau sekitar 84,89 persen. Ini berarti dari seluruh data testing yang digunakan, model berhasil melakukan klasifikasi sentimen dengan benar pada sekitar 85 persen data. Artinya dari 10.000 data testing, sekitar 8.489 data berhasil diprediksi dengan benar.

4. Untuk Classification Report
   Precision mengukur seberapa banyak prediksi model yang benar dari seluruh prediksi yang dibuat pada suatu kelas. Ketika model memprediksi review sebagai negatif, sekitar 85 persen prediksi tersebut benar-benar negatif, begitu pula dengan yang positif

   Recall mengukur seberapa banyak data yang berhasil ditemukan dengan benar oleh model dibandingkan seluruh data asli pada kelas tersebut. Dari seluruh review negatif yang sebenarnya ada pada dataset, model berhasil mengenali sekitar 85 persen.

   F1-Score merupakan gabungan antara precision dan recall yang digunakan untuk melihat keseimbangan performa model. Kita mendapatkan nilai 0.85 artinya model memiliki performa yang stabil karena precision dan recall berada pada nilai yang seimbang. Kenapa semuanya bernilai 0.85 atau 85% ? Karena model memiliki performa yang cukup konsisten pada kedua kategori sentimen, baik positif maupun negatif. Ini menunjukkan model tidak terlalu bias terhadap salah satu kelas.

5. Untuk Confusion Matrix
      Prediksi
            Negatif   Positif

Actual Neg    4193      768

Actual Pos     743      4296

Artinya Sebanyak 4193 review negatif berhasil diprediksi dengan benar sebagai negatif. Lalu sebanyak 768 review negatif salah diprediksi sebagai positif. Sebanyak 743 review positif salah diprediksi sebagai negatif. Lalu sebanyak 4296 review positif berhasil diprediksi dengan benar sebagai positif.

6. Hasil Prediksi Review Baru

- Output pertama
Review :
This movie was amazing and very entertaining

Sentiment :
positive

Pada tahap pengujian akhir, saya memasukkan review baru yang belum pernah dilihat model sebelumnya.
Review pertama berisi kata-kata seperti amazing dan entertaining, yang secara umum memiliki makna positif.
Model berhasil mengenali pola tersebut dan memprediksi review sebagai sentimen positif.

- Output kedua
Review :
The movie was boring and a waste of time

Sentiment :
negative

Review kedua berisi kata-kata seperti boring dan waste of time, yang umumnya menunjukkan opini negatif terhadap film.
Model berhasil mengenali pola kata negatif tersebut dan mengklasifikasikannya sebagai sentimen negatif.

### Kesimpulan 
Berdasarkan hasil pengujian, sistem berhasil melakukan analisis sentimen review film menggunakan kombinasi preprocessing teks, TF-IDF, dan algoritma Naive Bayes.

Model memperoleh akurasi sebesar 84,89 persen, menunjukkan bahwa metode yang digunakan cukup efektif dalam membedakan review positif dan negatif.

Selain itu, pengujian pada review baru juga menunjukkan bahwa model mampu melakukan prediksi terhadap data yang belum pernah dipelajari sebelumnya.

<img width="1917" height="1079" alt="Screenshot 2026-06-16 161236" src="https://github.com/user-attachments/assets/e50e0317-171b-47b9-b956-9ebfdac1e4d3" />
<img width="1916" height="1079" alt="Screenshot 2026-06-16 161243" src="https://github.com/user-attachments/assets/cceab072-cfe6-4995-97e1-49e5aa3c0353" />
<img width="1917" height="1079" alt="Screenshot 2026-06-16 161251" src="https://github.com/user-attachments/assets/824876af-afef-48ce-8802-03d255271215" />
<img width="1918" height="1079" alt="Screenshot 2026-06-16 161257" src="https://github.com/user-attachments/assets/ac1e3d84-3fce-472f-bfad-7b0541e1a841" />
<img width="1918" height="1079" alt="Screenshot 2026-06-16 161311" src="https://github.com/user-attachments/assets/bfe195c8-54c2-4e4b-949e-2e9dbf727064" />
<img width="1918" height="1079" alt="Screenshot 2026-06-16 161317" src="https://github.com/user-attachments/assets/67bda35f-686e-412c-813a-17e190a320c3" />
<img width="1917" height="1079" alt="Screenshot 2026-06-16 161326" src="https://github.com/user-attachments/assets/8c80960c-c7c5-4872-9eae-b292200a30d9" />
<img width="1338" height="750" alt="Screenshot 2026-06-16 213133" src="https://github.com/user-attachments/assets/6cc0886f-4903-4279-a26d-4953c00de964" />
<img width="1337" height="750" alt="Screenshot 2026-06-16 213140" src="https://github.com/user-attachments/assets/fb809975-0eaf-41af-8e84-3540f48c01f5" />
<img width="1336" height="752" alt="Screenshot 2026-06-16 213147" src="https://github.com/user-attachments/assets/1fea5693-f4f4-49f7-a8e7-2c4eea937423" />
<img width="1334" height="748" alt="Screenshot 2026-06-16 213152" src="https://github.com/user-attachments/assets/6935920e-db40-4bd7-b0af-04ccbf02510f" />


