def perkalian(awal, akhir):
    hasil = [i**2 for i in range(awal, akhir)]
    return hasil

awal = int(input("awal angka: "))
akhir = int(input("akhir angka: "))

hasil = perkalian(awal, akhir)

print(hasil)
    