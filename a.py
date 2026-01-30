"""Arabalar= ["Bmw","Mercedes","Opel","Mazda"]
# a=len(Arabalar)
# print(f"\n{a} \nArabalar \n{Arabalar[0]} \n{Arabalar[-1]}")

# Arabalar.pop()
# Arabalar.insert(3,"Toyota")

# print(Arabalar)
# a=Arabalar.index("Opel")
# print(a)

# a=[Arabalar.pop(-1)]
# print(a)

# Arabalar[-2:]=["Totoya","Renault"]
# print(Arabalar)

"""

isimler=["Ali","Yağmur","Hakan","Deniz"]
Yıllar=[1998,2000,1998,1987]

# isimler.insert(0,"Sena")#listenin başına Sena ekledik
# isimler.append("Cenk")#listenin sonuna Cenki ekledik
# isimler.remove("Deniz")#Deniz listeden kaldırdık
# isimler.index("Deniz")#hata verir çünkü deniz listede yok

# VarMi= Ali in isimler #Ali isimler listesinde var mı?
# if VarMi ==True:
#     print("\nAli isimler arasında yer almaktadır")
# else:
#     print("\nAli isimler arasında yer almamaktadır")

# isimler.reverse()#listeyi ters çevirdik
# Yıllar.reverse()

# Yıllar.sort()#Yıllar listesini küçükten büyüğe sıraladık

# print(Yıllar.max())#Yıllar listesinin en büyük elemanını yazdırdık
# print(Yıllar.min())#Yıllar listesinin en küçük elemanını yazdırdık

# ip= "Chavrolet, Dacia, Fiat, Ford, Honda, Hyundai, Kia, Mazda, Nissan, Opel, Peugeot, Renault, Seat, Skoda, Suzuki, Toyota, Volkswagen"
# bölünmüş = ip.split(",")
# print(bölünmüş)


# print(Yıllar.count(1998))# 1998 sıyısının adedini yazdırır

# print(Yıllar.clear())# Yıllar listesini temizler

# a=input("Lütfen bir herhangi marka isim giriniz: ")
# b=input("Lütfen bir herhangi marka isim giriniz: ")#marka isimlerini kullanıcıdan aldık
# c=input("Lütfen bir herhangi marka isim giriniz: ")
# markalar=[a,b,c]#aldığımız stringleri bir listenin içine attık
# print(markalar)

"""
print("",isimler,"\n",Yıllar)"""


"""
ogrenciler = {"120":{"isim":"Ali","soyisim":"Yılmaz","telefon": "532 000 01 02" },"125": {"ad":"can","soyad":"Korkmaz","telefon" :"1325469781"},"128":{"Ad":"Volkan","Soyad":"Demirel","Telefon":"3635422812"}}
"""
ogrenciler = {}

for i in range(3):
    i=i+1
    a=input(f"Lütfen {i}. öğrenci numarasınızı giriniz: ")
    b=input(f"Lütfen {i}. isminizi giriniz: ")
    c=input(f"Lütfen {i}. soyisminizi giriniz: ")            #istediğim gibi olmadı ama 
    d=input(f"Lütfen {i}. telefon numaranızı giriniz: ")
    ogrenciler[i]= { a:{"isim": b,"soyisim": c ,"telefon": d} }
print(ogrenciler)













