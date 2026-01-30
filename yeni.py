#isim = "Mahmut"
#print("İsminiz doğru mu? \n{}".format(isim))

# ad=input("Adınızı giriniz: ")
# soyad=input("Soyadınızı giriniz: ")
# print(f"\nAdınız soyadınız doğru mu?\n{ad} {soyad}") 

# AAA="https://www.youtube.com/"
# print(len(AAA)) #uzunluk ölçtüm
# print(AAA[20:23]),print(AAA[8:11]) #belli kısımları kestim
# print(AAA[-1:-(len(AAA)+1):-1]) #ters yazdırdım
# print(AAA[0:7]+AAA[12:len(AAA)]) #www kısmını sçktüm
# print(AAA[-12:-5])


"""
ad , soyad , yash , ish = "Mahmut" , "Kaya" , 25 , "Mühendis"
print(f"Merhaba, ben {ad} {soyad }.{yash} yaşındayım ve bir {ish}'im.")

ish1= "m"+ish[-7:] #ilk harfi değiştirdim -küçülttüm-

print(f"\nMerhaba, ben {ad} {soyad }.{yash} yaşındayım ve bir {ish1}'im.")

print("abs "*3)
"""


"""
website = "http://www.sadikturan.com" 
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

a= " Hello World "
# a=  a.strip()
# print(a)

# website1= website.strip("http://www.").strip(".com")
# print(website1)

# couse = course.lower()
# print(couse)

# kactane = website.count("a") 
# print("\n",kactane)
# acaba = website.startswith("www")
# acaba1 = website.endswith("com")
# print("\n",acaba,"\t",acaba1)


varmi =website.find("com")
if varmi >=0:
    print("Var")
    print(f"{varmi}. karaktere bakınız")
else:
    print("Yok")


# course=course.isalpha()
# print(course)

# icerik= "Content"
# print(icerik.center(50,"*"))

# course=course.replace(" ","-") #boşlukları tire ile değiştirdim

# a= a.replace("World","There") #world'ü there ile değiştirdim

course1= course.split(" ") #course stringini boşlukları baz alarak kelimelerine ayırdım ve diziye attım
course2= "".join(course1) #daha sonra bu diziyi aralarında hiç birşey olmayacak şekilde birleştirdim
print("\n",course2) 


#anlamları yazmayı unuttum 
#daha sonrasında yazmaya üşendim
#beni mazur görün lütfen

print("\n",a)
print("\n",course)
print("\n",website)

"""