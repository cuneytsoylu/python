"""
    Uygulama 1: Bir öğrencinin aşağıdaki bilgileri için gerekli değişkenleri oluşturunuz.
    Öğrenci adı
    Öğrenci soyadı
    Öğrenci ad + soyad
    Öğrenci numarası
    Öğrenci cinsiyet
    Öğrenci tc kimlik
    Öğrenci doğum yılı
    Öğrenci adres bilgisi   
    Öğrenci yaşı 
"""

ogrenciAdi = 'cuneyt'
ogrenciSoyad = 'soylu'
ogrenciAdSoyad = ogrenciAdi + ' ' + ogrenciSoyad
print(ogrenciAdSoyad)

ogrenciNumarasi = 20230303
print(ogrenciNumarasi)

ogrenciCinsiyet = True  # Erkek
print(ogrenciCinsiyet)

ogrenciCinsiyet = False  # Kadın
print(ogrenciCinsiyet)

ogrenciTcKimlik = "12345678911"

ogrenciDogumYili = 1992

ogrenciYas = 2023 - ogrenciDogumYili
print(ogrenciYas)

ogrenciAdres = 'Adana merkez'


"""
    Uygulama 2: Aşağıdaki ürünlerin toplam bilgisini hesaplayınız.
    
    Ürün 1 => 50     TL
    Ürün 2 => 60.5   TL
    Ürün 3 => 356.45 TL
"""

urun1 = 50
urun2 = 60.5
urun3 = 356.45

toplam = urun1 + urun2 + urun3
print("Ürün toplamı:", toplam)
