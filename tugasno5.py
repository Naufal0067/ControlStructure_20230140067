# Program untuk mencetak pola berdasarkan input pengguna

# Meminta input dari pengguna
n = int(input("Masukkan nilai n: "))

# Perulangan luar untuk menangani baris (dari 1 hingga n)
for i in range(1, n + 1):
    # Perulangan dalam untuk mencetak angka 'i' sebanyak ('i' kali)
    for j in range(i):
        print(i, end=" ")  # Mencetak angka 'i' diikuti dengan spasi
    print()  
