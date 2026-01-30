a=int(input("Bir sayı giriniz: "))
b=int(input("Bir sayı daha giriniz: "))

if a<b:# büyüklük küçüklük karşılaştırması
    print(f"{a} sayısı {b} sayısından küçüktür.")
elif a>b:
    print(f"{a} sayısı {b} sayısından büyüktür.")
else:
    print(f"{a} sayısı {b} sayısına eşittir.")

"""Bu kod parçasında kullanıcıdan iki sayı alınıyor ve bu sayılar karşılaştırılıyor."""

vize1=int(input("Birinci vize notunu giriniz: "))
final=int(input("Final notunu giriniz: "))

ortalama= vize1*60/100+final*40/100 #not ortalama hesaplama
if ortalama>=50:
    print("Dersi geçtiniz.")
else:
    print("Dersi geçemediniz.")


sayi=int(input("Herhangi bir sayı giriniz: "))#Çift mi tek mi olduğunu bulan program

if sayi/2==0:
    print(f"{sayi} sayısı çifttir.")
else:
    print(f"{sayi} sayısı tektir.")

sayi=int(input("Herhangi bir sayı giriniz: "))#pozitiflik negatiflik kontrolü
if sayi<0:
    print("Negatif sayı girdiniz.")
elif sayi==0:
    print("Sıfır girdiniz.")
else:
    print("Pozitif sayı girdiniz.")




eposta= "Abc@gmail.com"
şifre= "12345"
# Kullanıcıdan e-posta ve şifre bilgilerini alalım
giriş_eposta=input("E-posta adresinizi giriniz: ")
giriş_şifre=input("Şifrenizi giriniz: ")
# Giriş bilgilerini kontrol edelim
if giriş_eposta == eposta and giriş_şifre == şifre:
    print("Giriş başarılı ile yapıldı.")
else:
    print("E-posta adresi veya şifre hatalı.")    