import random


renkler = ["Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Siyah","Yeşil","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı","Kırmızı",]
renk = random.choice(renkler)

print("Çevirelim mi? 'y/n'")
cevap1 = input()
if cevap1 == "y"or"Y":    
    sayi1 = str(random.randrange(0,36))
    print(sayi1 +","+ renk)
elif cevap1 == "n" or "N":
    print("Tamamdır.Hoşçakal")


