a=int(input("masukkan a: "))
b=int(input("masukkan b: "))
c=int(input("masukkan c: "))

if (a==b==c):
    print ("segitiga sama sisi, memiliki nilai sisi a=",a,"b=",b,"c=",c)
elif (a==b or b==c or a==c):
    print ("segitiga sama kaki, memiliki nilai sisi a=",a,"b=",b,"c=",c)
else:
    print ("segitiga sembarang, memiliki nilai sisi a=",a,"b=",b,"c=",c)