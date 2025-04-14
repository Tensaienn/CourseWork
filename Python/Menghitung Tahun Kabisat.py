tahun = int(input("Masukkan Tahun: "))

if (tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)):
    print("Tahun:", tahun)
    print("Tahun:", tahun, "Merupakan Tahun Kabisat")
else:
    print("Tahun:", tahun)
    print("Tahun:", tahun, "Bukan Tahun Kabisat")