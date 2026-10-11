# Program Halo Python

## Deskripsi Proyek

Program Halo Python adalah aplikasi sederhana yang dibuat menggunakan bahasa pemrograman Python sebagai latihan dasar pemrograman.

Program ini dapat:

* Meminta pengguna memasukkan nama.
* Menampilkan pesan sapaan kepada pengguna.
* Meminta pengguna memasukkan tahun lahir.
* Menghitung perkiraan usia pengguna.
* Menangani kesalahan input menggunakan `try/except`.
* Menampilkan teks berwarna di terminal menggunakan pustaka Colorama.

## Persyaratan

Sebelum menjalankan program, pastikan perangkat sudah memiliki:

* Python 3.10 atau versi yang lebih baru.
* Terminal atau Command Prompt.
* Pip untuk menginstal pustaka Python.

## 1. Membuat Virtual Environment

Virtual environment digunakan untuk memisahkan dependensi proyek dari instalasi Python utama.

Buka terminal pada folder proyek, kemudian jalankan perintah:

```bash
python -m venv .venv
```

Perintah tersebut akan membuat folder `.venv` yang digunakan sebagai lingkungan virtual proyek.

## 2. Mengaktifkan Virtual Environment

### Windows (Command Prompt)

```bat
.venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### Linux atau macOS

```bash
source .venv/bin/activate
```

Jika berhasil, nama lingkungan virtual biasanya akan muncul di awal baris terminal, misalnya:

```text
(.venv)
```

## 3. Menginstal Dependensi

Pastikan virtual environment sudah aktif.

Instal semua dependensi yang tercantum dalam `requirements.txt` menggunakan perintah:

```bash
python -m pip install -r requirements.txt
```

Program ini menggunakan pustaka Colorama untuk menampilkan teks berwarna di terminal.

Untuk memeriksa paket yang sudah terinstal, jalankan:

```bash
pip list
```

## 4. Menjalankan Program

Setelah dependensi berhasil diinstal, jalankan program menggunakan perintah:

```bash
python halo.py
```

Program akan meminta nama dan tahun lahir pengguna, kemudian menampilkan pesan sapaan serta perkiraan usia.

### Contoh Hasil Program

```text
=== Program Halo ===
Masukkan nama Anda: Andre
Halo, Andre! Selamat datang di praktikum Python.
Semoga sukses!
Masukkan tahun lahir Anda: 1997
Perkiraan usia Anda adalah 29 tahun.
Tahun depan usia Anda sekitar 30 tahun.
```

*Catatan: Perkiraan usia dihitung berdasarkan tahun saat program dijalankan tanpa memeriksa tanggal dan bulan lahir.*

## 5. Menonaktifkan Virtual Environment

Jika sudah selesai menggunakan program, nonaktifkan virtual environment dengan perintah:

```bash
deactivate
```

## Struktur Proyek

```text
halo-project/
├── .venv/
├── halo.py
├── requirements.txt
├── README.md
└── .gitignore
```

Folder `.venv/` merupakan lingkungan virtual dan sebaiknya tidak diunggah ke repositori GitHub.

## Penutup

Proyek ini dibuat sebagai latihan dasar penggunaan Python, pengelolaan dependensi, virtual environment, penanganan kesalahan input, dan dokumentasi proyek menggunakan Markdown.
