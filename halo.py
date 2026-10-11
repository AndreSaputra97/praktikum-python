# halo.py - program Python pertama
from datetime import datetime
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}! Selamat datang di praktikum Python.")
try:
    tahun_lahir = int(input("Masukkan tahun lahir Anda: "))

    tahun_sekarang = datetime.now().year

    if tahun_lahir > tahun_sekarang:
        print("Tahun lahir tidak boleh lebih dari tahun sekarang.")
    elif tahun_lahir < 1900:
        print("Tahun lahir tidak valid.")
    else:
        umur = tahun_sekarang - tahun_lahir
        print(f"Perkiraan usia Anda adalah {umur} tahun.")

except ValueError:
    print("Input tidak valid! Masukkan tahun lahir berupa angka.")

print("Semoga sukses!")

