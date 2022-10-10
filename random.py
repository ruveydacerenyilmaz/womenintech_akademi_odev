import random
num=random.randint(0,100) #randint ikinci parametreyi dahil ederken, randrange dahil etmez.
guess=int(input("Sayıyı tahmin ediniz."))
while guess!=num:
    if guess>num:
        print("Daha küçük bir sayı giriniz!")
        guess=int(input("Tekrar tahmin et:"))
    if guess<num:
        print("Daha büyük bir sayı giriniz!")
        guess=int(input("Tekrar tahmin et:"))
    if guess==num:
        print("Tebrikler!Doğru bildiniz!")