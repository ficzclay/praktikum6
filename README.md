# Praktikum 6

## Latihan 1

- Buat Dictionary daftar kontak

- Nama sebagai key, dan nomor sebagai value
```
# Nama | Nomor Telepon
# ====================
# Ari  | 081267888
# Dina | 087677776
```

- Tampilkan kontaknya Ari
- Tambah kontak baru dengan nama Riko, nomor 087654544
- Ubah kontak Dina dengan nomor baru 088999776
- Tampilkan semua Nama
- Tampilkan semua Nomor
- Tampilkan daftar Nama dan nomornya
- Hapus kontak Dina.

Penjelasan:
   Kode ini digunakan untuk mencetak data dari daftar kamus dalam format tabel menggunakan Python. 

- Inisialisasi Data: `(list_of_dicts)` berisi informasi nama dan nomor telepon beberapa orang.
- Tentukan Lebar Kolom: Lebar kolom dihitung berdasarkan panjang teks terpanjang dalam dictionary ditambah 2.
- Cetak Header Tabel: Nama kolom dicetak sebagai header tabel.
- Cetak Garis Pembatas: Garis pembatas antara header dan data.
- Cetak Data: Setiap entri data dicetak dalam format tabel dengan lebar kolom yang telah ditentukan.


Hasil Akhir:






## Tugas Praktikum

Buat program sederhana yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:
- Program dibuat dengan menggunakan Dictionary
- Tampilkan menu pilihan: (Tambah Data, Ubah Data, Hapus Data,
Tampilkan Data, Cari Data)
- Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%,
uts: 35%, uas: 35%)
- Buat flowchart dan penjelasan programnya pada README.md.
- Commit dan push repository ke github.

Penjelasan:
Program tersebut merupakan aplikasi sederhana untuk manajemen data mahasiswa. Cara kerjanya adalah sebagai berikut:
1. **Inisialisasi**: Program dimulai dengan inisialisasi dictionary `data_mahasiswa` yang digunakan untuk menyimpan informasi mahasiswa.
2. **Menu Utama**: Pengguna diberikan opsi untuk melihat daftar nilai (`L`), menambahkan data mahasiswa (`T`), menghapus data mahasiswa (`H`), mengubah data mahasiswa (`U`), mencari data mahasiswa (`C`), atau keluar dari program (`K`).
3. **Tambah Data Mahasiswa**: Saat pengguna memilih untuk menambah data (`T`), program meminta input NIM, nama, nilai UTS, UAS, dan tugas. Nilai akhir dihitung dan data disimpan dalam `data_mahasiswa`.
4. **Lihat Daftar Nilai Mahasiswa**: Saat pengguna memilih untuk melihat daftar nilai (`L`), program menampilkan tabel daftar nilai mahasiswa.
5. **Hapus Data Mahasiswa**: Saat pengguna memilih untuk menghapus data (`H`), program meminta input NIM mahasiswa yang akan dihapus dan menghapusnya dari `data_mahasiswa`.
6. **Ubah Data Mahasiswa**: Saat pengguna memilih untuk mengubah data (`U`), program meminta input NIM mahasiswa yang akan diubah, menampilkan data saat ini, meminta input baru, dan menghitung nilai akhir setelah perubahan.
7. **Cari Data Mahasiswa**: Saat pengguna memilih untuk mencari data (`C`), program meminta input NIM dan menampilkan informasi mahasiswa tersebut jika ada.
8. **Keluar**: Saat pengguna memilih keluar (`K`), program berhenti.


Berikut Hasilnya:

Tambah Data Mahasiswa:

Lihat Daftar Nilai Mahasiswa:

Hapus Data Mahasiswa

Ubah Data Mahasiswa:

Cari Data Mahasiswa:


Flowchart:<br>



## Langkah-langkah pengerjaan latihan

1. Konfigurasi terlebih dahulu username dan email pada global repository-nya

```
git config --global user.name “nama_user”
```

```
git config --global user.email “email_user”
```

2. Buat repository local

```
mkdir bahasa_pemrograman
```

```
cd bahasa_pemrograman
```

```
mkdir praktikum5
```

3. Jika sudah, jalankan command (command git init digunakan untuk menginisialisasi repositori git baru)

```
git init
```

## Menambahkan File Baru Pada Repository Lokal

1. Untuk membuat file baru bisa juga dengan text editor

disini akan menggunakan terminal

```
echo “# praktikum5 >> README.md
```

2. Untuk menambahkan file yang baru saja dibuat, gunakan command

```
git add README.md
```

3. Untuk menyimpan perubahan yang ada pada database repositori
   lokal, gunakan command

```
git commit -m "first commit"
```

## Membuat Repository Server

1. Server repository yang digunakan adalah github
2. Buat akun github terlebih dahulu
3. Klik tombol + new repository
4. Isi nama repository-nya,

```
contoh: praktikum5
```

5. lalu klik tombol Create repository

## Menambahkan Remote Repository

- Remote Repository merupakan server repositori yang akan digunakan untuk menyimpan segala perubahan yang dilakukan pada repositori lokal, dan bisa diakses oleh banyak pengguna
- Untuk menambahkan remote repository server, gunakan command

```
git remote add origin [url]
```

## Mengirim perubahan ke server (Push)

- Untuk mengirim perubahan pada repositori lokal ke server, gunakan command

```
git push -u origin master
```

## Clone Repository

- git clone digunakan untuk mengambil salinan dari repositori Git dari server ke repositori lokal
- gunakan command ini untuk melakukan kloning ke repositori lokal

```
git clone [url]
```
