# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:58:38 2022

@author: user
"""
"""
python string yani matn matlar odatda birtirnoq('') qo'shtirnoq ichida yoziladi ("")
"""
shahar = "Toshkent"

# print("🥶")

"""
string ustida amallar 
"""
# a= "havo"
# print("Bugun "+a+" yaxshi")

# f-string opatori 
ism = "Azamat"
familya = "Narzulloyev"

toliq_ism = f"{ism} {familya}"

# matnda boshliq qo'shish uchun \t \n belgilari foydalanamiz
# print('Assalomu \talaykum')

# string methodlar upper() lower() title() capitalize() 

ism = "sabina"

familya = "Anvarov"



"""
lstrip() — matn boshidagi bo'shliqni,
rstrip() – matn oxiridagi bo'shliqni,
strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
"""
matn = "bugun hava yaxshi "

# input haqida tanishamiz 
# ism  = input("ismingizni kiriting ")
# print("Assalum alaykum hurmatli " + ism.title())

# topshriqlar 
#-----------------------------------------------------
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"

# print(f"{kocha} kochasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati ")


kocha = input("kochangizni kiriting ")
mahalla = input("mahallangizni kiriting ")
tuman = input("tumaningizni kiriting ")
viloyat = input("Viloyatingizni kiriting ")

print(f"""{kocha.title()} kochasi {mahalla.title()} mahallasi {tuman.title()} 
      tumani {viloyat.title()} viloyati """)
      
      






























