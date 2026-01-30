#Okuyucuya not
#burada bulunan kod satırları , hem 4. bölümdeki operatörler mantığını hemde %.bölümdeki Koşul ifadelerini içermektedir
#burada bu şekilde birleştirilmiş olmalarındaki en büyük sebep 4. bölümdeki uygulamyı koşul ifadeleri üzerinden yapmış olmamdır
#
#Ne yazıkki daha öncesinden Pyhton diline biraz vakıf olduğumdan 4.bölümdeki uygulamayı 5.bölüm ile karışık yazmış oldum
#eğer isterseniz bu kodları ayrı ayrı olarak yazıp tekrardan gönderebilirim


"""girilen sayının pozitif ve belirli aralıkta olup olmadığını kontrol etme programı"""
sayi= int(input("Bir sayı giriniz: "))

if sayi>0 and sayi<100:#sayı 0 ile 100 arasında mı kontrolü
    print(f"{sayi} sayısı 0 ile 100 arasındadır.")
else:
    print(f"{sayi} sayısı 0 ile 100 arasında değildir.")

if sayi/2==0 and sayi>0:#sayı pozitif ve çift mi kontrolü
    print(f"{sayi} sayısı pozitif ve çifttir.")
else:
    print(f"{sayi} sayısı pozitif ve çift değildir.")


"""şifre ve e-posta doğrulama programı"""
şifre= "12345"
eposta= "edsc@gmail.com"

giriş_eposta=input("E-posta adresinizi giriniz: ")
giriş_şifre=input("Şifrenizi giriniz: ")

if giriş_eposta == eposta and giriş_şifre == şifre:# giriş bilgileri doğrulama
    print("Giriş başarılı ile yapıldı.")
else:
    print("E-posta adresi veya şifre hatalı.")  


"""üç sayıtı birbiri içinde karşılaştırıp en büyüğünü bulan program"""
a=int(input("Bir sayı giriniz: "))
c=int(input("Bir sayı daha giriniz: "))
b=int(input("Bir sayı daha giriniz: "))

if a>b and a>c:
    print(f"{a} en büyük sayıdır.")
elif b>a and b>c:
    print(f"{b} en büyük sayıdır.")
elif c>a and c>b:
    print(f"{c} en büyük sayıdır.")


"""not ortalama hesaplama programı"""
vize=int(input("Birinci vize notunu giriniz: "))
final=int(input("Final notunu giriniz: "))
ortalama= vize*60/100+final*40/100 #not ortalama hesaplama
if final>=70:
    print("Dersi geçtiniz.")
elif ortalama>=50:
    print("Dersi geçtiniz.")
else:
    print("Dersi geçemediniz.")


"""boy kilo endeksi hesaplama programı"""
boy=float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
kilo=float(input("Lütfen kilonuzu kilogram cinsinden giriniz: "))
bki=boy/(kilo**2)
if bki<18.5:
    print("Zayıf")
elif bki>=18.5 and bki<24.9:
    print("Normal kilolu")
elif bki>=25 and bki<29.9:
    print("Fazla kilolu")
else:
    print("Obez")
