#berfungsi untuk mengevaluasi kinerja siswa berdasarkan persentase
def evaluate_performance(percentage):
    #untuk mengecek excellent performance
    if percentage >= 90:
        print ("Execellent perfromance")
    #untuk mengecek very good perfromance
    elif percentage >= 80:
        print ("Very Good performance")
    #untuk mengecek good performance
    elif percentage >= 70:
        print ("Good performance")
    #untuk mengecek average performance
    elif percentage >= 60:
        print ("Average performance")
    #untuk mengecek jika persentase dibawah 60
    else:
        print ("Below average performance")
    
percentage = float(input("Masukkan nilai murid: "))
print(evaluate_performance(percentage))