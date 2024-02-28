import random

def mazeret_uret():
    mazeretler = [
        "Baştan başlayamadım çünkü çok yorgundum.",
        "Internet bağlantım kesildi ve kaynaklara erişimim yoktu.",
        "Önemli bir aile meselesiyle ilgilenmek zorundaydım.",
        "Ödevimi yapacak kadar zamanım olmadı çünkü başka derslerden çok fazla ödevim vardı.",
        "Sağlık sorunları nedeniyle konsantre olamadım.",
        "Evde beklenmedik bir elektrik kesintisi yaşandı.",
        "Bilgisayarımın bozulması nedeniyle dosyalarıma erişim sağlayamadım.",
        "Kaynak kitapları kütüphanede ödünç alamadım.",
        "Ödev konusunda anlamadığım bir konu vardı ve yardım alacak kimsem yoktu.",
        "Çalışma alanım sessiz olmadığı için konsantre olamadım.",
        "Ödevimi yapmama engel olan bir acil durum çıktı.",
        "Ödevi yapacak kadar enerjim yoktu çünkü stres altındaydım.",
        "Ailemle ilgilenmek zorundaydım, bu yüzden ödev yapacak zamanım olmadı.",
        "Ödevi yapmak için gerekli malzemeleri temin edemedim.",
        "Bilgisayarımın güncelleme yapması nedeniyle zamanımın çoğunu bekleyerek geçirdim.",
        "Evdeki gürültü nedeniyle konsantre olamadım.",
        "Ödevimi yapmama engel olan beklenmedik bir misafir ziyareti oldu.",
        "Ödevimi tamamlamak için gereken yazılı materyalleri kaybettim.",
        "Ödevimi yapacak kadar motivasyonum yoktu çünkü konu beni ilgilendirmiyordu.",
        "Ödevimi yaparken bilgisayarımın çöktüğü bir teknik sorun yaşandı.",
        "Ödevi yapmama engel olan bir sağlık sorunu yaşadım.",
        "Evdeki gürültü nedeniyle konsantre olamadım.",
        "Öğretmenimizin ödevi verirken söylediği talimatları yanlış anladım.",
        "Ödevimi tamamlamak için gerekli olan veri toplama işlemi daha uzun sürdü.",
        "Ödevimi yapacak kadar uygun bir çalışma ortamı bulamadım.",
        "Ödevimi yapacak zamanım olmadı çünkü işe yetişmek için ekstra mesai yapmak zorunda kaldım.",
        "Ödev konusuyla ilgili kaynaklara ulaşmak için gereken zamanı bulamadım.",
        "Ödev yapmak için gereken malzemeleri almak için ekstra zaman harcadım.",
        "Ödevi yapacak kadar odaklanamadım çünkü aklım sürekli başka bir konuda dolaşıyordu.",
        "Ödevimi yapmak için gerekli olan araç ve gereçlerim kayboldu.",
        "Ödevimi yapmak için gerekli olan bilgisayarı paylaşmak zorunda kaldım ve bu yüzden beklemek zorunda kaldım.",
        "Ödevi yapmak için gerekli olan yazılı materyalleri bulmak için gereken zamanda evdeki düzen eksikliği nedeniyle zaman kaybettim.",
        "Ödevimi yapacak kadar zamanda internet bağlantım yavaş olduğu için veri toplama işlemi uzun sürdü.",
        "Ödevi yapmak için gerekli olan yazılı kaynaklarımı ödünç aldığım kişi geri dönmedi.",
        "Ödevimi yapmak için gerekli olan bilgisayarı kullanmak için gereken zamanda kardeşim sürekli bilgisayarı kullanmak istedi.",
        "Ödevimi yapacak kadar uygun bir çalışma ortamı bulamadım çünkü evimde tadilat çalışmaları vardı ve gürültü çok fazlaydı.",
        "Ödevimi yapmak için gereken zamanda bir randevuya geç kaldım ve sonrasında zamanım kısıtlıydı.",
        "Ödevimi yapmamı engelleyen bir ev kazası yaşandı ve bununla ilgilenmek zorunda kaldım.",
        "Ödevimi yapmak için gerekli olan bilgisayarı kullanmak için gereken zamanda kardeşim sürekli bilgisayarı kullanmak istedi.",
        "Ödevimi yapacak kadar uygun bir çalışma ortamı bulamadım çünkü evde bir parti vardı ve gürültüden konsantre olamadım.",
        "Ödevi yapmamı engelleyen bir doğal afet yaşandı ve bununla ilgilenmek zorunda kaldım.",
        "Ödevi yapmak için gerekli olan yazılı materyalleri almak için gereken zamanda mağazalar kapalıydı.",
        "Ödevimi yapmamı engelleyen bir kişisel kriz yaşadım.",
        "Ödevimi yapacak kadar uygun bir çalışma ortamı bulamadım çünkü evde beklenmedik bir tadilat çalışması başladı ve gürültü engel oldu.",
        "Ödevi yapmak için gerekli olan malzemeleri almak için gereken zamanda mağazalar kapalıydı.",
        "Ödevi yapmak için gereken zamanda başka bir zorunluluk nedeniyle ev dışında bulundum ve çalışma ortamım yoktu.",
        "Ödevimi yapmak için gereken yazılı materyalleri almak için gereken zamanda kaynak kitaplar kütüphanede bulunmuyordu.",
        "Ödevimi yapmak için gereken yazılı materyalleri ararken zaman kaybettim.",
        "Ödevi yapmak için gereken zamanda hastalık nedeniyle evden çıkamadım.",
        "Ödevimi yapmak için gereken zamanı bulamadım çünkü diğer sorumluluklarım vardı.",
        "Ödevi yapmamı engelleyen bir ailevi sorun yaşadım ve bununla ilgilenmek zorunda kaldım.",
        "Ödevimi yapacak kadar uygun bir çalışma ortamı bulamadım çünkü evde tadilat çalışmaları vardı ve gürültü çok fazlaydı.",
        "Ödevimi yapmak için gerekli olan yazılı materyalleri almak için gereken zamanda trafik sıkışıklığı nedeniyle geç kaldım.",
        "Ödevi yapmak için gereken yazılı materyalleri almak için gereken zamanda mağazalar kapalıydı.",
        "Ödevi yapmamı engelleyen bir ailevi sorun yaşadım ve bununla ilgilenmek zorunda kaldım."
    ]
    return random.choice(mazeretler)

def main():
    print("Ödev mazeret makinasına hoş geldiniz!")
    while True:
        input("Ödev yapamama sebebi için bir mazeret üretmek için ENTER tuşuna basın...")
        print(mazeret_uret())
        devam = input("Başka bir mazeret üretmek ister misiniz? (Evet/Hayır): ")
        if devam.lower() != "evet":
            print("Mazeret makinası kapanıyor. İyi günler!")
            break

if __name__ == "__main__":
    main()
