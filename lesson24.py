# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 12:23:16 2022

@author: user
"""

"""
lambda funksiyasi nomsiz funksiya bo'liq checsiz argument va bitta ifoda qabul qiladi 

map() Bu funksiya argument sifatida ro'yxat (yoki lug'at) va boshqa bir
 funksiyani qabul qilib, ro'yxat elementlariga qabul qilingan funksya
 yordamida ishlov beradi.

"""
from math import sqrt

import random
def daraja(n):
    return lambda x:x**n


son = daraja(2)


sonlar = list(range(10))

ildiz = list(map(sqrt, sonlar))
sonlar_darajasi = list(map(daraja(2), sonlar))

kvadrat = list(map(lambda x:x*x, sonlar))


ismlar = ['azamat','hasan','olim','yorqin']

ism = list(map(lambda matn:matn.upper(), ismlar))

#---------------------------------------------

# filter() funtion haqida to'liq or'rganamiz 


from random import sample

sonlar = sample(range(100),30)

def juftmi(x):
    return x%2==0


# juft_sonlar = list(filter(juftmi, sonlar))

juft_sonlar = list(filter(lambda x:x%2==0, sonlar))

toq_sonlar = list(filter(lambda x:x%2!=0, sonlar))

#-----------------------------
"""
startswith() method bu method berilgan matndan misol uchun 'b' harfini bilan boshlanadigan 
qildiradi agar bo'lsa True bo'lmasa False qaytaradi 

"""

mevalar =['olma','anor','nok','shaftoli','anjir']

mevalar_a = list(filter(lambda meva:(meva.startswith('a') or meva.startswith('o')), mevalar))



mevalar_len = list(filter(lambda meva:(len(meva)>5), mevalar))





















































