# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:57:18 2022

@author: user
"""

"""
python list haqida ma'lumot 
"""

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat

# yangi element qoshish append()
# ismlar.append('Azamat')

# insert() royhatni istalgan joyida yangi element qoshish

# mevalar.insert(1, 'shaftoli')


# listlardagi elementlarni ochirish del() yoki to'liq ochirish

# del mevalar[1]
# print(mevalar)
"""
Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz.
 Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz
 """
# mevalar.remove('olma')
# print(mevalar)
# agar remove da 2 ta va undan ko'p biri xil qiymatlar bo'lsa birinchisi o'chiradi 

"""
pop metodi bilan tanishamiz """

# bozorlik =[]

# bozorlik = mevalar.pop(1)
# print(bozorlik)
#-------------------------------------------------------------

# ismlar = ['Salim', 'Baxrom','Alisher']

# print("Salom "+ismlar[0]+" bugun choyxona bormi ")

sonlar  = [-1, 2,10.5 ,6]

mehmonlar = ['salim', 'bahodir', 'yorqin']
friends = []

friends.append(mehmonlar.pop(1))
print(friends)

































