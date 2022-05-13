# -*- coding: utf-8 -*-
"""
Created on Wed May 11 19:19:43 2022

@author: Murodillo
"""

ismlar =  ['Murodillo', 'Bahrom', 'Bekmurod', 'Muhammadali', 'Donyor']
#for ism in ismlar:
#     print('Salom ' + ism)
#n=0
#for ism in ismlar:
#    n=n+1
#    print('Salom ' + ism)
#print("Kod " + str(n) + " martta takrorlandi")
#toq_sonlar = list(range(11,100,2 ))
#for toq_son_kubi in toq_sonlar:
#    print(f"{toq_son_kubi} sonining kubi {toq_son_kubi**3} ga teng")
#kinolar = []
#for n in range(5):
#    kinolar.append(input(f"{n+1}-kino nomini kiriting"))
#for kino in kinolar:
#    print(kino + "\n")
odamlar = []
odam_soni = int(input('Bugun nechta odam bilan suxbatlashdingiz: '))
for n in range(odam_soni) :
   odamlar.append(input(f"{n+1}-odamni ismini kiriting: "))
for odam in odamlar:
    print(odam)