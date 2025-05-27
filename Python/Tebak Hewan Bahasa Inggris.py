hewan = {"Ant": "Semut", "Bee": "Lebah", "Mosquito": "Nyamuk", "Butterfly": "Kupu-kupu",
"Spider": "Laba-laba", "Fly": "Lalat", "Hedgehog": "Landak", "Snail": "Siput",}
pilihan = input("Mau Bermain?(y/n): ")
while pilihan == "y":
    benar = 0
    salah = 0
    for soal, jawaban in hewan.items():
        print(soal)
        jawaban_pengguna = input("Jawabanmu?: ")
        if jawaban_pengguna == jawaban:
            print("==============================")
            benar += 1
        else:
            salah += 1
            print("==============================")
    if salah > benar:
        print("Bro your English is cooked 💀 go touch some Duolingo.")
    else:
        print("Bro just soloed the whole animal dictionary 💀💀")
    print("Benar:", benar)
    print("Salah:", salah)
    coba_lagi = input("Mau Coba Lagi?(y/n): ")
    if coba_lagi == "y":
        pilihan = "y"
    else:
        print("ok deh :(")
        break
else:
    print("ok deh :(")