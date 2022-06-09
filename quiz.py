import re
#nomor 1

pola  = r'@[A-Za-z]+[0-9.\_]+'
xx = input('Masukkan Username: ')
cocok = re.findall(pola, xx)
if cocok:
    if xx == cocok[0]:
        print('PASS')
    elif xx != cocok[0]:
        print('FAILED')
else:
    print('FAILED')


#nomor 2
a = open('text.txt','r')
text = a.read()
a.close

def cekEmail(txt):
    pola = r'[\w.-]+@[\w.-]+'
    cek = re.findall(pola, text)[0]
    print(cek)
