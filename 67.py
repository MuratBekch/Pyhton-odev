# Belirtilen kelimeyi verilen sayı kadar ekrana yazdıran fonksiyon
def yazdır(kelime, sayi):
    # Python'da string ile tam sayı çarpılırsa string tekrarlanır
    print(kelime * sayi)

# Fonksiyonun çağrılması: "beş " ifadesini 5 kez yazdırır
yazdır("beş ", 5)

# Gönderilen tüm argümanları bir liste içine toplayan fonksiyon
def listele(*parametre):
    liste_olustur = [] # 'list' ismi yerine 'liste_olustur' kullanıldı (çakışmayı önlemek için)
    for i in parametre:
        liste_olustur.append(i) # Her bir parametreyi listenin sonuna ekle

    return liste_olustur

# Farklı veri tiplerinde (string ve int) veriler gönderiliyor
a = listele("1", "2", 3)
print(a)    

# Belirli bir aralıktaki asal sayıları ekrana yazdıran fonksiyon
def asalBul(baslangic, bitis):
    for sayi in range(baslangic, bitis + 1):
        if sayi > 1: # 1 asal sayı değildir, bu yüzden 1'den büyükleri kontrol et
            for i in range(2, sayi):
                if (sayi % i) == 0: # Sayı herhangi bir sayıya tam bölünüyorsa asal değildir
                    break
            else:
                # for döngüsü break ile bitmediyse sayı asaldır
                print(sayi)

# Kullanıcıdan girdi alma ve fonksiyonu çalıştırma
baslangic = int(input("Başlangıç değerini girin: "))
bitis = int(input("Bitiş değerini girin: "))
asalBul(baslangic, bitis)

# Bir sayının tam bölenlerini liste olarak döndüren fonksiyon
def BölenleriBul(a):
    Bolenler = []
    for i in range(2, a): # 2'den başlayarak sayıya kadar olanları kontrol et
        if a % i == 0: # Kalan 0 ise i bir tam bölendir
            Bolenler.append(i)
    return Bolenler

print(BölenleriBul(10))

# Sözlük (Dictionary) veri yapısı ile hesap bilgilerini tutma
YiğitHesap = {
    "ad": "Yiğit Bekç",
    "HesapNo": "123654789",
    "Bakiye": 4000,
    "Ek bakiye": 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    # Durum 1: Ana bakiye yeterli mi?
    if hesap["Bakiye"] >= miktar:
        hesap["Bakiye"] -= miktar # Mevcut bakiyeden miktarı düş
        print("Paranızı alabilirsiniz.")
    else:
        # Durum 2: Ana bakiye yetersiz, ek bakiye dahil toplam kontrolü
        toplam = hesap["Bakiye"] + hesap["Ek bakiye"]
        
        if toplam >= miktar:
            ekHesapKullanimi = input("Ek hesap kullanılsın mı? (e/h): ")
            if ekHesapKullanimi == "e":
                # Kalan miktar ek hesaptan çekilecek
                ekHesapKullanilacakMiktar = miktar - hesap["Bakiye"]
                hesap["Bakiye"] = 0 # Ana bakiye sıfırlanır
                hesap["Ek bakiye"] -= ekHesapKullanilacakMiktar # Kalan miktar ek bakiyeden düşer
                print("Paranızı alabilirsiniz.")
            else:
                print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} TL bulunmaktadır.")
        else:
            # Durum 3: Toplam limit de yetersiz
            print("Üzgünüz, bakiyeniz yetersiz.")

# 3000 TL çekme denemesi
paraCek(YiğitHesap, 3000)

