# Mengambil input angka pertama dari pengguna dan mengonversinya ke tipe integer
a = int(input("Masukkan Angka Pertama: "))

# Mengambil input angka kedua dari pengguna dan mengonversinya ke tipe integer
b = int(input("Masukkan Angka Kedua: "))

# Mengambil input angka ketiga dari pengguna dan mengonversinya ke tipe integer
c = int(input("Masukkan Angka Ketiga: "))

# Menentukan angka terbesar di antara ketiga angka yang dimasukkan
if a >= b and a >= c:
    # Jika a adalah yang terbesar, simpan nilai a di AngkaTerbesar
    AngkaTerbesar = a
elif b >= a and b >= c:
    # Jika b adalah yang terbesar, simpan nilai b di AngkaTerbesar
    AngkaTerbesar = b
else:
    # Jika c adalah yang terbesar, simpan nilai c di AngkaTerbesar
    AngkaTerbesar = c

# Menampilkan angka terbesar kepada pengguna
print("Angka Terbesar:",AngkaTerbesar)