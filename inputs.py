"""
x =input("1. sayıyı giriniz: ") #Kullanıcıdan veri alır ve x değişkenine atar
y =input("2. sayıyı giriniz: ") #Kullanıcıdan veri alır ve y değişkenine atar

toplam = int(x)+ int(y) #Kullanıcıdan alınan x ve y değerleri string olarak alındı. 
                        #String yani kelime veri tipi matematiksel bir işleme tabi tutulamaz 
                        #Basitçe kelimeler sayılarla çarpılamaz. Bundan dolayı alınan verileri Sayılara dönüştürdük

print("toplam :",toplam)
"""
print("Daire alan ve çevre hesaplama programı \n")
pi=3.14
r=input("Dairenin yarıçapını giriniz: ")
r=float(r)
dairecevresi=2*pi*(r)
daireninalani=pi*(r)**2
print(" \n Dairenin alanı:",daireninalani , "\n" , "Dairenin çevresi:", dairecevresi)