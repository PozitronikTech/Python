#Mükkemmel sayi  6 = 3 + 2 + 1    => mükemmel sayidir.
#                8 = 4 + 2 + 1    => mükemmel sayi değildir.
#Girilen sayi araliğinda ki mükemmel sayilari vermektedir.
#It gives the perfect number in the entered range.
def mukkemmelSayi (sayi):
    sonuc = 0

    for i in range(1,sayi):
        if (sayi % i == 0):
            sonuc+=i
    return sonuc == sayi

first = int(input("First: "))
last = int(input("Last: "))

for i in range(first, last):
    if (mukkemmelSayi(i)):
        print("Mukemmel Sayi", i)
