sayilar=1,3,5,7,9,12,19,21
i=0
"""Sayılar kümesindeki sayıların 3'e bölünenini bulma"""
# for sayı in sayilar:
#     if sayı%3==0:
#        print(sayı)
#     else:
#         pass
"""sayılar listesindeki sayıların toplamını bulma"""
# for sayı in sayılar:
#     sayı+=sayı
# print("\n",sayı)

"""tek sayıların karesini alma"""
# for sayı in sayılar:
#     if sayı%2==1:
#         sayı1=sayı
#         sayı=sayı**2
#         print(f"Sayı:{sayı1} , karesi:{sayı}")


"""5 harf ve daha küçük şehirleri yazdıma"""
# Sehirler=["kocaeli","istanbul","ankara","izmir","rize"]

# for sehir in Sehirler:
#     if len(sehir)<=5:
#         print(sehir)
          
"""Ürünlerin "price"ı 5000'den az olanları yazdırma"""
# ürünler=[{"name":"samsung s6","price":3000},{"name":"samsung s7","price":4000},{"name":"samsung s8","price":5000},{"name":"samsung s9","price":6000},{"name":"samsung s10","price":7000}]

# toplam=0
# for fiyat in ürünler:
#     toplam+=fiyat["price"]
#     if fiyat["price"]<=5000:
#         print(fiyat["name"])
# print(f"Toplam fiyat:{toplam}")

"""Sayıalrı teker teker yazdırma"""
# sayilar =[1,3,5,7,9,12,19,21]

# while (i <len(sayilar)):
#     print(sayilar[i])
#     i+=1    

"""kullanıcının giridği iki sayı arasındaki tek sayıları bulma"""
# a=int(input("Bir sayı yazın:"))
# b=int(input("Bir sayı daha yazın:"))
# if a%2==0:
#     i=1
#     while (i<(b-a)):
#         print(a+i)
#         i+=2    
# else:
#     i=0
#     while (i<(b-a)):
#         print(a+i)
#         i+=2


"""100'den geriye doğru birer birer gelme"""
# i=100
# while 1<=i:
#     print(i)
#     i-=1



"""kullancının girmiş olduğu inputları bir liste içine atıp sıraladıktan sonra yazdırma"""
# a=int(input("Bir sayı girin:"))
# b=int(input("Bir sayı daha girin:"))
# c=int(input("Bir tane daha girin:"))
# d=int(input("Bir sayı daha girin:"))    
# e=int(input("Son bir sayı daha girin:"))
# Sayilar=[a,b,c,d,e]
# Sayilar.sort()
# while i <len(Sayilar):
#     print(Sayilar[i])
#     i+=1    
"""Basit bir depo oluşturucu, kullanıcının isteği doğrultusunda liste uzunluğu belirlenen bir dict oluşturup içeirğini doldurma"""
# SayiAdedi=int(input("Kaç ürün gireceksiniz:"))
# Ürünler=[]
# while i<SayiAdedi:
#     ürünadi=input(f"{i+1}. ürün adını girin:")
#     ürünfiyati=input(f"{i+1} ürün fiyatını girin:")
#     Ürünler.append({"Ürün adı":ürünadi,"Ürün fiyatı":ürünfiyati})
#     i+=1
# print(Ürünler)

"""rastgele"""
# x=1
# sonuç=0
# while x<=100:
#     x+=1
#     if x%2==2:
#         continue
#     sonuç+=x
    
# print(sonuç)
"""Sayı tahmin oyunu"""
# import random as random
 
# x = random.randint(1,100)

# hak=int(input("Kaç hakkınız olsun? "))
# while hak>0:
#     if hak>0:
#         hak-=1
#         a=int(input("Tahmininiz: "))
#         if a == x:
#             hak=0;print("Tebrikler,Oyunu kazandınız")
#         elif a<x:
#          print("yanlış tahmin, tekrar edeneyin, biraz yukarı")
#         elif a>x:
#             print("yanlış tahmin, tekrar deneyin, biraz aşağı")
# else:
#    print("Neyazıkki oyunu kaybettiniz")

# """Asal sayı kontrolü"""

# a=int(input("Sayıyı giriniz: "))
# if a ==1:
#     print("1 sayısı asal değildir")
# asalmi=True
# for i in range(2,a):
#     if a%i==0:
#         asalmi=False
#         break
# if asalmi == True:
#     print("Sayı asaldır")
# else:
#     print("sayı asal değildir")