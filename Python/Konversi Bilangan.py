print ("=============DAFTAR MENU=============")
print ("1. Konversi Bilangan Desimal ke Biner")
print ("2. Konversi Bilangan Biner ke Desimal")
print ("3. Konversi Bilangan Desimal ke Oktal")
print ("4. Konversi Bilangan Oktal ke Desimal")
print ("=====================================")

pilihan = (int(input("Masukkan Pilihan Anda (1/2/3/4): ")))

if pilihan == 1:
    desimal = int(input("Masukkan Bilangan Desimal: "))
    biner = bin(desimal)[2:]
    print ("Bilangan Biner dari", desimal, "adalah", biner)

elif pilihan == 2:
    biner = input("Masukkan Bilangan Biner: ")
    desimal = int(biner, 2)
    print ("Bilangan Desimal dari", biner, "adalah", desimal)

elif pilihan == 3:
    desimal = int(input("Masukkan Bilangan Desimal: "))
    oktal = oct(desimal)[2:]
    print ("Bilangan Oktal dari", desimal, "adalah", oktal)

elif pilihan == 4:  
    oktal = input("Masukkan Bilangan Oktal: ")
    desimal = int(oktal, 8)
    print ("Bilangan Desimal dari", oktal, "adalah", desimal)
else:
    print ("Pilihan tidak ada. Silakan coba lagi.")
