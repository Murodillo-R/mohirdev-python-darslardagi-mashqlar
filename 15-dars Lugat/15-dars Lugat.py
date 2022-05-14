# -*- coding: utf-8 -*-
"""
Created on Sat May 14 10:45:40 2022

@author: Murodillo
"""

#python_words = {
#    'integer':'Butun son',
#    'float': "O'nlik son",
#    'boolean':"Mantiqiy qiymat",
#    'for':"Biror amalni qayta-qayta bajarish tsikli",
#    'if':'Shartlarni tekshirish operatori'}

#for key, value in sorted(python_words.items()):
#    print(f"{key.title()} - {value}")

#Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
#keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
#davlatlar = {
#    'Uzbekiston': 'Tashkent',
#    'Rassiya': 'Maskva',
#    'Qazagizton': 'Nur-Sulton',
#    'Qirgiziston': 'Bishkek'
#   } 
#print('\nDavlat nomi')
#for davlat in sorted(davlatlar.keys()):
#    print(davlat)
#print('\nDavlat poytaxti')
#for poytaxt in sorted(davlatlar.values()):
#    print(poytaxt)

#Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
#Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

#davlatlar = {
#    'Uzbekiston': 'Tashkent',
#    'Rassiya': 'Maskva',
#    'Qazagizton': 'Nur-Sulton',
#    'Qirgiziston': 'Bishkek'
#   } 

#davlat_user =  input('Istalgan davlat nomini kiriting')

#if davlat_user in davlatlar:
    #print(davlatlar[davlat_user])
#else:
    #print('Bunday davlat yo\'q')
        
menus = {
    'osh': '15000',
    'somsa': '3500',
    'lagmon': '17000',
    'chuchvara': '13000',
    'choy': '2000',
    'non': '3000',
    'salat': '3000'
   } 
#user_buys = []

#for  n in range(3):
   # user_buys.append(input(f"{n+1} taomni kiriting"))
    
#for user_buy in user_buys:
 #   if user_buy in menus:
  #      print(f"{user_buy} narxi {menus[user_buy]} som" )
   # else:
    #    print(f"Bizda {user_buy} taom yo\'q")
print(menus.get('osh'))