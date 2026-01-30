
"""Ehliyet Alma Durumu Kontrolü"""

# isim=input("İsminizi ve soyisminizi giriniz: ")
# yas=int(input("Yaşınızı giriniz: "))
# egitim=input("Eğitim durumunuzu giriniz: ")

# if yas>=18 and (egitim=="lise","Lise" or egitim=="Üniversite","üniversite"):
#     print("Ehliyet alabilirsiniz.")
# elif yas<18 and (egitim=="lise","Lise" or egitim=="Üniversite","üniversite"):
#     print("Ehliyet alamazsınız.")
# else:
#     print("Ehliyet alamazsınız.")


"""Notlandırma Sistemi"""
yazili1=int(input("İlk yazılı sınavından aldığınız notu giriniz: "))
yazili2=int(input("İkinci yazılı sınavından aldığınız notu giriniz: "))
sozlu=int(input("Sözlü sınavından aldığınız notu giriniz: "))

ortalama= (yazili1 + yazili2 + sozlu)/3

if ortalama>=85:
    print("Notunuz:5")
elif ortalama>=70 and ortalama<85:
    print("Notunuz:4")
elif ortalama>=55 and ortalama<70:
    print("Notunuz:3")
elif ortalama>=45 and ortalama<55:
    print("Notunuz:2")
elif 25<=ortalama<45:
    print("Notunuz:1")
else:
    print("Notunuz:0")


"""araç muayene kontrolü"""
Anahtar_reslim=int(input("Aracınız kaç gündür sizinle?"))
if (Anahtar_reslim//365)==1:
    print("1. muayene gerekiyor.")
elif (Anahtar_reslim//365)==2:
    print("2. muayene gerekiyor.")
elif (Anahtar_reslim//365)==3:
    print("3. muayene gerekiyor.")
else:
    print("Araç muayenesi gerekmiyor.")