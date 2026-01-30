
"""Kelime yazdırma"""
# def yazdır(kelime,sayi):
#     print(kelime*sayi)

# yazdır("beş ",5)

"""sonsuz Liste olurma"""
# def listele(*parametre):
#     list =[]
#     for i in parametre:
#         list.append(i)

#     return list    
# a=listele("1","2",3)
# print(a)

"""Aralarındaki asalları bul"""

# def asalBul(baslangic,bitis):
#    for sayi in range(baslangic, bitis + 1):
#      if sayi > 1:
#         for i in range(2, sayi):
#             if (sayi % i) == 0:
#                 break
#         else:
#             print(sayi)

# baslangic = int(input("Başlangıç değerini girin: "))
# bitis = int(input("Bitiş değerini girin: "))
# asalBul(baslangic,bitis)

# """Bölen Buldurucu"""
# def BölenleriBul(a):
#    Bolenler=[]
#    for i in range(2,a):
#       if a%i==0:
#             Bolenler.append(i)
#    return Bolenler

# print(BölenleriBul(10))


# """Bankacılık uygulaması"""
# YiğitHesap = {#Hesap oluşturduk
#     "ad": "Yiğit Bekç",
#     "HesapNo": "123654789",
#     "Bakiye": 4000,
#     "Ek bakiye": 1000
# }

# def paraCek(hesap, miktar):
#     print(f"Merhaba {hesap['ad']}")

#     if hesap["Bakiye"] >= miktar:
#         hesap["Bakiye"] -= miktar # Bakiyeyi güncelleme
#         print("Paranızı alabilirsiniz.")
#     else:
#         toplam = hesap["Bakiye"] + hesap["Ek bakiye"]
        
#         if toplam >= miktar:
#             ekHesapKullanimi = input("Ek hesap kullanılsın mı? (e/h): ")
#             if ekHesapKullanimi == "e":
#                 ekHesapKullanilacakMiktar = miktar - hesap["Bakiye"] # ek hesaba gidildiği taktirde ek hebın bakişye miktarı azalır
#                 hesap["Bakiye"] = 0
#                 hesap["Ek bakiye"] -= ekHesapKullanilacakMiktar
#                 print("Paranızı alabilirsiniz.")
#             else:
#                 print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} TL bulunmaktadır.")
#         else:
#             print("Üzgünüz, bakiyeniz yetersiz.")

# paraCek(YiğitHesap, 3000)