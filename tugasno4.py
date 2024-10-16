 #Mengambil input nilai n dari pengguna dan mengonversinya ke tipe integer
n = int(input("Masukkan nilai n: "))

# Menampilkan pesan bahwa program akan mencetak angka ganjil hingga n
print("Angka ganjil hingga", n, ":")

# Menggunakan loop untuk iterasi dari 1 hingga n
for i in range(1, n + 1):
    # Memeriksa apakah angka i adalah ganjil
    if i % 2 != 0:
        print(i) 
        
