import random


renkler = ["Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Yeşil","Kirmizi","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı"]
renk = random.choice(renkler)
print("Çevirelim mi? 'y/n'")
cevap1 = input()
devam = 0
if cevap1 == "y":
    devam = 1
else:
    print("Tamamdır.Hoşçakal")
    input()

while devam == 1:
    
    
    if cevap1 == "y"or"Y": 
        sayi1 = str(random.randrange(0,36))
        print(sayi1 +","+ renk)
        devam = 0
        input()    