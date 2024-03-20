from random import randint
print("Mehmet Çoban tarafından hazırlandı.")
print("Lütfen oyun modu seçiniz")
while True:
    mod=input("Kolay,Zor:")
    if mod.lower() == "kolay" or  mod.lower() =="zor":
        break
    else:
        print("Geçerli bir oyun modu giriniz") 
def kolay():
    while True:
        sayi = randint(1,100)
        hak = 10
        while True:
            tahmin = int(input("Bir tam sayı tahmin et:"))
            if tahmin == sayi and hak == 10:
                print("TEK ATTIN")
                break
            if tahmin == sayi :
                print("DOĞRU TAHMİN")
                break
            elif hak == 0 :
                print("KAYBETTİN")
                break
            elif  hak >=2  and tahmin != sayi:
                print("Yanlış tahmin")
                hak-=1
            if  hak <2 and tahmin >sayi and tahmin != sayi:
                print(tahmin-sayi,"sayısı Kadar aşağı veya yukarı")
                hak-=1
            if hak <2 and sayi > tahmin and tahmin != sayi:
                print(sayi-tahmin,"sayısı kadar aşağı veya yukarı")
                hak-=1
        while True:
            soru = input("Tekrar oynamak ister misiniz? E/H:")
            if soru.lower() == "e" or soru.lower() == "h":
                break
        if soru == "h":  
            print("Görüşürüz")
            break
def zor ():
    while True:
        sayi = randint(1,100)
        hak = 5
        while True:
            tahmin = int(input("Bir sayı tahmin et:"))
            if tahmin == sayi and hak == 5:
                print("Mükkemel Tahmin")
                break
            elif tahmin == sayi:
                print("Doğru Tahmin")
                break
            if tahmin != sayi:
                print("Yanlış Tahmin")
                hak -= 1
            if hak == 0:
                print("Kaybettin")
                break
        while True:
            soru = input("Tekrar oynamak ister misiniz? E/H:")
            if soru.lower() == "e" or soru.lower() == "h":
                break
        if soru == "h":  
            print("Görüşürüz")
            break
if mod.lower() == "kolay":
    kolay()
if mod.lower() == "zor":
    zor()