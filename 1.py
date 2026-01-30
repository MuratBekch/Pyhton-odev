x,y,z=2,5,107
numbers = 1, 5, 7, 10, 6

# ilk=int(input("Bir sayı giriniz: "))
# ikinci=int(input("Bir sayı daha giriniz: "))

# a=ilk*ikinci-(z+y+x)

# a=y//x
# a=x+y+z
# a= a%3

# a= y**x

x , *y,z = numbers

a=z**3

b= y[0] + y[1]+y[2]

print(a,b)

""" baştan itibaren gelirsek; ilk olarak x, y ve z değişkenlerine atama yaptım.
Sonrasında kullanıcıdan aldığım 2 tane integer değerlerini çarpıp, oradan x,y ve z'nin toplamını çıkardım.
daha sonra y nin x'e bölümünün tan kısmını aldım . Sonrasında x,y ve z'nin toplamını aldım ve 3'e modunu buldum
x,y ve z değişkenlerini numbers adlı demetden unpack ettim.
Son olarak z'nin küpünü a'ya atadım ve y listesindeki elemanların toplamını b'ye atadım ve ekrana yazdırdım."""