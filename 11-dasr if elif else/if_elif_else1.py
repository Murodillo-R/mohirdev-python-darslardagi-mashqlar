# -*- coding: utf-8 -*-
"""
Created on Thu May 12 06:49:29 2022

@author: Murodillo
"""
#son = int(input('Juft son kiriting'))
#juft = son%2
#if juft == 0:
#    print("Juft son")
#else:
#    print('Toq son')

#yosh = int(input('Yoshingizni kiriting '))
#if yosh < 4 or yosh > 60:
#    narx = 0
#elif yosh < 18:
#    narx = 10000
#elif yosh >= 18:
#    narx = 20000
#print(f"Sizga chipta narxi {narx} so‘m")

mahsulotlar = ['un', 'shakar', 'yog', 'piyoz', 'kartoshka', 'sabzi', 'tuxum','karam','gosht', 'non']
savat = []
#for n in range(5):
#    savat.append(input(f"{n+1} maxsulotni kiriting ")) 
#for sa in savat:
#    if sa in mahsulotlar:
#        print("maxsulot do‘kond bor")
#    else:
#        print('Maxsulot dokonda yoq')

#mahsulotlar = ['un', 'shakar', 'yog', 'piyoz', 'kartoshka', 'sabzi', 'tuxum','karam','gosht', 'non']
#savat = []
#bor_maxsulotlar = []
#yoq_maxsulotlar = []
#for n in range(5):
#    savat.append(input(f"{n+1} maxsulotni kiriting ")) 
#for sa in savat:
#    if sa in mahsulotlar:
#        bor_maxsulotlar.append(sa)
#    else:
#        yoq_maxsulotlar.append(sa)
#if yoq_maxsulotlar:
#    print("quyidagi maxsulotlar dokonimizada yoq: \n")
#    for yoq_maxsulot in yoq_maxsulotlar:
#        print(yoq_maxsulot)
#else:
#    print('Dokonda barcha maxsulotlar bor')

#foydalanuvchilar = ['admin', 'murod', 'salim', 'komol', 'zulfiya']
#login = input('Loginni kiriting')
#if login.lower() in foydalanuvchilar:
#    print('Login band qilingan. Yangi login tanlang')
#else:
#    print("xush kelibsiz")

son = int(input('Istalgan son kiriting'))
sonlar = []
for n in range(2,10):
    qoldiq = n%son
    if qoldiq == 0:
        sonlar.append(n)
        
print("siz kiritgan son quyidagilarga qoldiqsiz bolinadi: \n")
for soni in sonlar:
    print(soni)