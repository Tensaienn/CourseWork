def pascal_segitiga(n):
    segitiga = []
    for i in range(n):
        baris = [1]  
        if segitiga:  
            last_row = segitiga[-1]
            for j in range(1, i):
                nilai = last_row[j - 1] + last_row[j]
                baris.append(nilai)
            baris.append(1)  
        segitiga.append(baris)
    
    
    for row in segitiga:
        print(row)


angka = int(input("input angka: "))
pascal_segitiga(angka)

