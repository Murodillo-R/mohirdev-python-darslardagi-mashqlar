# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:01:51 2022

@author: Murodillo
"""

def fibanachi_sonlarni_to(son):
    fibanachi_sonlar = []
    for n in range(son):
        fibanachi_son = fibanachi_sonlar[(n-2)+(n-1)]
        fibanachi_sonlar.append(fibanachi_son)
        print(fibanachi_sonlar)
fibanachi_sonlarni_to(50)