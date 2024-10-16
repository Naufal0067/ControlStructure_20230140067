# Meminta input dari pengguna untuk menentukan jumlah elemen deret Fibonacci
n = int(input("Masukkan nilai n: "))

# Inisialisasi dua angka pertama dalam deret Fibonacci
a, b = 0, 1
# List kosong untuk menyimpan hasil deret Fibonacci
hasil = []

# Perulangan untuk menghitung deret Fibonacci sebanyak 'n' kali
for i in range(n):
    hasil.append(a)  # Menambahkan nilai 'a' ke dalam list hasil
    a, b = b, a + b  # Menghitung angka Fibonacci berikutnya dengan menggeser nilai a dan b

# Menampilkan hasil deret Fibonacci
print("Deret Fibonacci hingga", n, ":", hasil)
