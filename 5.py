sayilar=1,3,5,7,9,12,19,21
i=0
# 3'e bölünen sayıları filtreleme
sayilar = [1, 3, 5, 7, 9, 12] # Liste tanımlandı
for sayı in sayilar:
    if sayı % 3 == 0: # Eğer sayının 3 ile bölümünden kalan 0 ise
       print(sayı)
    else:
       pass # Hiçbir şey yapma

# Sayılar listesindeki sayıların toplamını bulma
# HATA DÜZELTİLDİ: Toplam değişkeni dışarıda tanımlanmalıydı, yoksa sadece son sayıyı toplar.
toplam_sonuc = 0
for sayı in sayilar:
    toplam_sonuc += sayı # Her sayıyı toplam değişkenine ekler
print("\nToplam:", toplam_sonuc)

# Tek sayıların karesini alma
for sayı in sayilar:
    if sayı % 2 == 1: # Sayı tek ise
        sayı_orjinal = sayı # Değeri kaybetmemek için yedekle
        karesi = sayı**2 # Karesini hesapla
        print(f"Sayı:{sayı_orjinal} , karesi:{karesi}")

# 5 harf ve daha kısa şehirleri yazdırma
Sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]
for sehir in Sehirler:
    if len(sehir) <= 5: # Karakter uzunluğu 5 veya daha küçükse
        print(sehir)
# Fiyatı 5000'den küçük ürünleri listeleme
ürünler = [
    {"name": "samsung s6", "price": 3000},
    {"name": "samsung s7", "price": 4000},
    {"name": "samsung s8", "price": 5000},
    {"name": "samsung s9", "price": 6000},
    {"name": "samsung s10", "price": 7000}
]

toplam = 0
for urun in ürünler:
    toplam += urun["price"] # Her ürünün fiyatını toplama ekle
    if urun["price"] <= 5000: # Fiyat kriterini kontrol et
        print(urun["name"])
print(f"Tüm ürünlerin toplam fiyatı: {toplam}")
# Sayıları indeks kullanarak teker teker yazdırma
sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
i = 0 # HATA DÜZELTİLDİ: i değişkeni başlangıçta tanımlanmalı
while i < len(sayilar):
    print(sayilar[i])
    i += 1 # Sayaç artırılmazsa sonsuz döngüye girer

# İki sayı arasındaki tek sayıları bulma
a = int(input("Bir sayı yazın: "))
b = int(input("Bir sayı daha yazın: "))

# Mantık: Eğer 'a' çift ise bir sonrakinden başla (tek yap), sonra 2'şer artır
i = 0
if a % 2 == 0:
    a += 1 # Başlangıç sayısını tek sayıya çekiyoruz
while (a + i) < b:
    print(a + i)
    i += 2

# 100'den geriye sayma
i = 100
while 1 <= i:
    print(i)
    i -= 1 # Her adımda bir azalt
# Kullanıcıdan alınan sayıları sıralama
Sayilar = []
i = 0
# 5 adet sayı alma döngüsü
while i < 5:
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    Sayilar.append(sayi)
    i += 1
Sayilar.sort() # Listeyi küçükten büyüye sıralar
print("Sıralanmış liste:", Sayilar)

# Dinamik Depo Oluşturucu
SayiAdedi = int(input("Kaç ürün gireceksiniz: "))
Ürünler = []
i = 0
while i < SayiAdedi:
    ürünadi = input(f"{i+1}. ürün adını girin: ")
    ürünfiyati = input(f"{i+1}. ürün fiyatını girin: ")
    # Verileri sözlük yapısında listeye ekle
    Ürünler.append({"Ürün adı": ürünadi, "Ürün fiyatı": ürünfiyati})
    i += 1
print(Ürünler)

# Sayı Tahmin Oyunu
import random
hedef_sayi = random.randint(1, 100)
hak = int(input("Kaç hakkınız olsun? "))

while hak > 0:
    tahmin = int(input(f"Tahmininiz ({hak} hak kaldı): "))
    hak -= 1
    if tahmin == hedef_sayi:
        print("Tebrikler, oyunu kazandınız!")
        break # Doğru tahminde döngüden çık
    elif tahmin < hedef_sayi:
        print("Daha yukarı!")
    else:
        print("Daha aşağı!")
else: # Hak bittiğinde çalışır
    print(f"Hakkınız bitti. Sayı: {hedef_sayi} idi.")

# Asal Sayı Kontrolü
sayi = int(input("Sayıyı giriniz: "))
if sayi < 2:
    print("Asal değildir.")
else:
    asalmi = True
    for i in range(2, sayi):
        if sayi % i == 0: # Kendinden küçük bir sayıya bölünüyorsa asal değildir
            asalmi = False
            break
    if asalmi:
        print("Sayı asaldır.")
    else:
        print("Sayı asal değildir.")
