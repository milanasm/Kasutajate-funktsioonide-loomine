from Kasutajate_funktsioonide_loomine import*
try:
    a=float(input("arv1:"))
    b=float(input("arv2:"))
    t=input("tehe:")
    vastus=arithmetic(a,b,t)
    print(vastus)
    vastus=arithmetic(float(input("arv1:")),float(input("arv2:")),input("Tehe:"))
    print(vastus)
except:
    print("Viga: Vale sisend. Palun sisestage numbriline v��rtus.")


#is_year_leap funktsiooni kasutamine
try:
    aasta=int(input("Mis aasta tahad kontrollida? "))
    if aasta>0:
        v=is_year_leap(aasta)
        print(v)
        if v:
            print(f"{aasta} on liigasta")
        else:
            print(f"{aasta} ei ole liigasta")
    else:
        print("Viga: Aasta peab olema positiivne arv.")
except:
    print("Viga: Sisesta korrektne aasta (number).")
        
#3square() kasutamine:
a=float(input("Ruudu k�lg= "))
while True:
    try:
        a=float(input("Ruudu k�lg= "))    
        if a<=0:
            print("Viga: K�lje pikkus peab olema positiivne number.")
            continue  
        break 
    except:
        print("Viga: Palun sisestage korrektne number.")
print(f"Ruudu k�lg on {a}")
S,P,d=square(a)
print(f"Ruudu pindala: {S}")
print(f"Ruudu perimeeter: {P}")
print(f"Ruudu diagonaal: {d}")
#4
try:
    month=int(input("Sisesta kuu number (1-12): "))
    print(season(month))
except ValueError:
    print("Viga: Palun sisestage korrektne number.")

#5
try:
    summa=float(input("Sisesta algkapital (eurodes): "))
    aastad=int(input("Sisesta aastate arv: "))
    l�ppsumma=bank(summa, aastad)
except ValueError as ve:
    print(f"Viga: {ve}")
else:
    print(f"Teie l�ppsumma p�rast {aastad} aastat on: {l�ppsumma:.2f} eurot.")

#6
try:
    a=input("Sisesta arv (v�i vajuta Enter, et kasutada juhuslikku arvu): ")
    if a=="": 
        print(f"Juhuslik arv: {is_prime()}")
    else:
        a=int(a)
        if a<0 or a>10000:
            print("Viga: Arv peab olema vahemikus 0 kuni 10000.")
        else:
            print(f"Kas {a} on algarv? {is_prime(a)}")
except:
    print("Viga: Palun sisestage kehtiv t�isarv.")
