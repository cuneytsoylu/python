website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sifirdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?
sonuc = len(website)
print(sonuc)
# 2- 'website' içinden www karakterlerini alın.
sonuc = website[7:10]
print(sonuc)
# 3- 'website' içinden com karakterlerini alın.
karakterSayisi = len(website)
sonuc = website[karakterSayisi-3:karakterSayisi]
print(sonuc)
# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.
sonuc = kursAdi[0:15]
print(sonuc)
sonuc = kursAdi[:15]
print(sonuc)
sonuc = kursAdi[-15:]
print(sonuc)
# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.
sonuc = kursAdi[::-1]
print(sonuc)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

print('abc ' * 3)

name, surname, age, job = 'Cuneyt', 'Soylu', 31, 'QA ENGINEER'

# 9- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Cuneyt Soylu, Yasim 31 ve mesleğim QA ENGINEER.'

sonuc = "Benim adim " + name + " " + surname + \
    ",Yasim " + str(age) + " ve meslegim " + job + "."
sonuc = "Benim adim {0} {1},Yasim {2} ve meslegim {3}".format(
    name, surname, age, job)
sonuc = f"Benim adim {name} {surname},Yasim {age} ve meslegim {job}."

print(sonuc)
