# base case: jika angka yang dicari tinggal satu digit, kembalikan angka tersebut
# ini penting agar rekusrsi tidak berjalan selamanya.

def jumlah_digit(n):
    if n < 10:
        return n
    
    # rekursi stepnya:
    # 1. n % 10 akan mengambil angka paling kanan atau satuan
    # 2. n // 10 membuang angka paling kanan
    # 3. fungsi memanggil dirinya sendiri dengan sisa angka yang ada
    return (n % 10) + jumlah_digit(n // 10)

# contoh penggunaannya adalah
angka = 6789
hasil = jumlah_digit(angka)

print(f"Jumlah digit dari {angka} adalah {hasil}")
# logikanya: 9 + (8 + (7 + 6)) = 30
