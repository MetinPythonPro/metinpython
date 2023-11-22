import time
import random

spuan=0
bpuan=0

while True:
    secim=input("Seçiminizi yapınız: taş - kağıt - makas: ")
    if secim == "taş" or secim == "kağıt" or secim == "makas" or secim == "Taş" or secim == "Kağıt" or secim == "Makas":
        laptop=random.randint(1, 3)
        if laptop == 1:
            laptop = "taş"
        if laptop == 2:
            laptop = "kağıt"
        else:
            laptop = "makas"
        print("Veeeeee... Sonuçlar!")
        print("3!")
        time.sleep(1)
        print("2!")
        time.sleep(1)
        print("1!")
        time.sleep(1)
        print("0!")
        
        print("Bilgisayarın seçimi......")
        time.sleep(2)
        print(laptop,"!")
        time.sleep(1)
        print("Veeee sizin seçiminiz......")
        time.sleep(2)
        print(secim,"!")
        if laptop == secim:
            print("Beraberlik!")
            print("Bilgisayar puanı:", bpuan)
            print("Senin puanın:", spuan)
        elif secim == "taş" and laptop == "makas" or secim == "Taş" and laptop == "Makas":
            print("Kazandın!")
            spuan += 1
            print("Bilgisayar puanı:", bpuan)
            print("Senin puanın:", spuan)
        elif secim == "kağıt" and laptop == "taş" or secim == "Kağıt" and laptop == "Taş":
            print("Kazandın!")
            spuan += 1
            print("Bilgisayar puanı:", bpuan)
            print("Senin puanın:", spuan)
        elif secim == "makas" and laptop == "kağıt" or secim == "Makas" and laptop == "Kağıt":
            print("Kazandın!")
            spuan += 1
            print("Bilgisayar puanı:", bpuan)
            print("Senin puanın:", spuan)
            
        else:
            print("Kaybettin! Noob!")
            bpuan += 1
            print("Bilgisayar puanı:", bpuan)
            print("Senin puanın:", spuan)

            
    else:
        print("Hatalı giriş! Lütfen tekrar deneyiniz.")