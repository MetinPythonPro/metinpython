import random

pasword = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("İstediğiniz parolanın uzunluğunu yazınız:"))

parola = ""

for (i) in range(uzunluk):
    parola+=random.choice(pasword)

print(parola)