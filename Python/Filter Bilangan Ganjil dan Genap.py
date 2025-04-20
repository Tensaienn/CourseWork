angka = [1,2,3,4,5,6,7,8,9]
genap = 0
ganjil = 0

for num in angka:
    if num % 2 == 0:
        genap += 1

for num in angka:
    if num % 2 != 0:
        ganjil +=1

print (angka)
print ("Jumlah Bilangan Genap: ", genap)
print ("Jumlah Bilangan Ganjil: ", ganjil)
