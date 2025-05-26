kata = input("Masukkan Kalimat: ")
kapital = 0
kecil = 0
for huruf in kata:
    if huruf.isupper():
        kapital += 1
    elif huruf.islower():
        kecil += 1
print(f"Jumlah huruf kapital: {kapital}")
print(f"Jumlah huruf kecil: {kecil}")