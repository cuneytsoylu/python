ad = 'Cuneyt'
soyad = 'Soylu'
yas = '31'

msj = 'Benim adim ' + ad + ' ve soyadim ' + soyad + '.Yasim ise ' + yas + '.'
karakterSayisi = len(msj)  # len dediğimizde karakter sayisini veriri bize#

print(msj[0])                   # B
print(msj[1])                   # e
print(msj[-1])                  # .
print(msj[karakterSayisi - 1])  # .

print(msj[0:5])  # 0 ile 5 arasindaki karakterleri alir#
print(msj[6:17])
print(msj[:10])
print(msj[10:])

print(msj[-10:-1])
print(msj[0:40:2])
print(msj[::1])
print(msj[::-1])
