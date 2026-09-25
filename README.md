# pertemuan-04-validasi-2225250002

## Identitas
* **Nama**: Nasywaa Zaafarani Kurniawan
* **NIM**: 2225250002
* **Kelas**: 3A

---

## Tujuan Repositori
Repositori ini dibuat untuk memenuhi tugas praktikum Pertemuan 4 mata kuliah Algoritma dan Pemrograman. Repositori ini berisi latihan dan praktik penggunaan struktur kontrol seleksi tingkat lanjut seperti rantai `if-elif-else`, validasi masukan (*error handling* dengan `try-except` dan pengecekan rentang nilai), serta percabangan bersyarat untuk menangani berbagai aturan multikondisi pada Python.

---

## Daftar dan Fungsi Berkas

### Folder `latihan/`
* **`01_predikat_nilai.py`**: Menentukan predikat nilai (A sampai E) berdasarkan nilai akhir menggunakan rantai `if-elif-else` terstruktur[cite: 5].
* **`02_kategori_bilangan.py`**: Mengklasifikasikan suatu bilangan bulat ke dalam empat kategori (negatif, nol, positif genap, atau positif ganjil) yang saling lepas[cite: 5].
* **`03_validasi_rentang.py`**: Memvalidasi besar sudut agar berada pada rentang yang sah (lebih dari 0 dan kurang dari 180 derajat) sebelum diklasifikasikan jenis sudutnya[cite: 4].
* **`04_validasi_tipe.py`**: Menggunakan blok `try-except` untuk menangani kesalahan tipe data masukan jumlah soal benar, serta memvalidasi rentang dan status kelulusan[cite: 4].
* **`05_klasifikasi_sudut_segitiga.py`**: Memvalidasi besar tiga sudut segitiga (positif dan jumlah total tepat 180 derajat) serta menentukan jenis segitiga (lancip, siku-siku, atau tumpul)[cite: 3].

### Folder `praktik/`
* **`validasi_klasifikasi_nilai.py`**: Program utama asesmen Pertemuan 4 untuk memvalidasi tipe data dan rentang nilai ujian, tugas, serta kehadiran, menghitung nilai akhir, memeriksa syarat minimum kehadiran, menentukan predikat, dan mengevaluasi status kelulusan mahasiswa.

---

## Hasil Pengujian Tugas Utama (`praktik/validasi_klasifikasi_nilai.py`)

| Ujian | Tugas | Kehadiran | Nilai Akhir | Keluaran yang Diharapkan | Status |
| :-: | :-: | :-: | :-: | :--- | :-: |
| 90 | 80 | 95 | 86.00 | Predikat A, Lulus | Sesuai |
| 75 | 70 | 85 | 73.00 | Predikat B, Lulus | Sesuai |
| 60 | 60 | 80 | 60.00 | Predikat C, Lulus | Sesuai |
| 55 | 50 | 90 | 53.00 | Predikat D, Belum lulus | Sesuai |
| 40 | 30 | 100 | 36.00 | Predikat E, Belum lulus | Sesuai |
| 90 | 90 | 75 | 90.00 | Nilai akhir tetap tampil, status Tidak memenuhi syarat kehadiran | Sesuai |
| 105 | 80 | 90 | - | Pesan penolakan rentang nilai ujian | Sesuai |
| 80 | -5 | 90 | - | Pesan penolakan rentang nilai tugas | Sesuai |
| 80 | 80 | abc | - | Pesan penolakan tipe | Sesuai |

---

## Cara Menjalankan

Buka terminal di direktori utama repositori ini, lalu jalankan program menggunakan perintah berikut:

```bash
python praktik/validasi_klasifikasi_nilai.py
python latihan/01_predikat_nilai.py
python latihan/02_kategori_bilangan.py
python latihan/03_validasi_rentang.py
python latihan/04_validasi_tipe.py
python latihan/05_klasifikasi_sudut_segitiga.py
```

### Refleksi
Dalam praktikum Pertemuan 4 ini, saya mempelajari pentingnya validasi input menggunakan blok try-except serta penerapan struktur seleksi multikondisi menggunakan rantai if-elif-else.

Hal yang paling saya pahami adalah bagaimana menyusun kondisi secara berurutan (menurun) agar tidak ada kasus yang tumpang tindih, seperti pada penentuan predikat nilai dan validasi rentang. Kendala yang sempat saya hadapi adalah ketelitian dalam menentukan posisi blok percabangan (menempatkan if di dalam else atau mengatur tingkat indentasi yang tepat). Terkadang saya keliru meletakkan posisi pengecekan syarat kehadiran di dalam atau di luar blok perhitungan nilai, sehingga program mengeksekusi alur logika yang tidak sesuai. Masalah ini berhasil saya atasi dengan merancang kerangka logika secara bertahap: memvalidasi input terlebih dahulu, menghitung nilai akhir, memeriksa syarat kehadiran minimum, lalu menentukan predikat dan status kelulusan. Ketika menemukan kendala penulisan sintaks dan penempatan struktur percabangan, saya dibantu oleh AI Gemini untuk mengonfirmasi logika kodenya.

### Sumber yang Digunakan
