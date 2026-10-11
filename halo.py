# halo.py - program Python pertama

from datetime import datetime
from colorama import init, Fore, Style
from art import text2art

# Inisialisasi Colorama
init(autoreset=True)

# Menampilkan judul dekoratif
print(Fore.CYAN + Style.BRIGHT + text2art("HALO"))

print(Fore.YELLOW + Style.BRIGHT + "=" * 35)
print(Fore.GREEN + Style.BRIGHT + "   PROGRAM PYTHON PERTAMA")
print(Fore.YELLOW + Style.BRIGHT + "=" * 35)

# Meminta nama pengguna
nama = input(Fore.CYAN + "Masukkan nama Anda: ")

print(
    Fore.GREEN
    + Style.BRIGHT
    + f"\nHalo, {nama}! Selamat datang di praktikum Python."
)

print(Fore.MAGENTA + "Mari belajar Python dengan semangat!\n")

# Meminta tahun lahir dan menghitung perkiraan usia
try:
    tahun_lahir = int(input(Fore.CYAN + "Masukkan tahun lahir Anda: "))

    tahun_sekarang = datetime.now().year

    if tahun_lahir > tahun_sekarang:
        print(
            Fore.RED
            + Style.BRIGHT
            + "Tahun lahir tidak boleh lebih dari tahun sekarang."
        )

    elif tahun_lahir < 1900:
        print(
            Fore.RED
            + Style.BRIGHT
            + "Tahun lahir tidak valid."
        )

    else:
        umur = tahun_sekarang - tahun_lahir

        print(Fore.YELLOW + "\n" + "-" * 35)
        print(
            Fore.GREEN
            + Style.BRIGHT
            + f"Perkiraan usia Anda adalah {umur} tahun."
        )
        print(Fore.YELLOW + "-" * 35)

except ValueError:
    print(
        Fore.RED
        + Style.BRIGHT
        + "Input tidak valid! Masukkan tahun lahir berupa angka."
    )

# Pesan penutup
print(Fore.CYAN + Style.BRIGHT + "\nSemoga sukses!")
print(Fore.MAGENTA + text2art("GOOD LUCK"))

