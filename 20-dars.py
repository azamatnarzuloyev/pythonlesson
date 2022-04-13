


def toliq_ism(ism, familyase):

    full_ism = f" {ism} {familyase}"
    return full_ism


a= toliq_ism('azamat', 'narzulloyev')
# print(a)


# -----------------------------------


def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()

# atasini ismini kiritish majburiy emas 
b = toliq_ism_yasa('azamat','narzulloyev')
# print(b)
#------------------------------------
def avto_info(kompanyasi, madali, karopkasi, narxi=''):
    avto = {
        'kompanya' : kompanyasi,
        'madel': madali,
        'karabokasi': karopkasi,
        'narx': narxi
    }
    return avto

avtolar = avto_info('gm', 'lasetti', 'afto', '200000')

# print(avtolar)
#-------------------------------------------


def oraliq(min, max):
    sonlar = []
    while max>min:
        sonlar.append(min)
        min+=1
    return sonlar

c = oraliq(10,20)
# print(c)
#--------------------------------------

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniyasi=input("Ishlab chiqaruvchi: ")
#     madeli=input("Modeli: ")
  
#     korobka=input("Korobka: ")
    
#     narxi=input("Narxi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniyasi, madeli,  korobka,  narxi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# topshiriqlar
#1-topshriq
def Info(ismlari, familasi, tugilgan_yili, manzili=''):
    malumot = {
        'ism':ismlari,
        'familyasi': familasi,
        'tugilgan_yil':tugilgan_yili,
        'manzili': manzili,
    }
    return malumot
b = Info('azamat', 'narzulloyev', '1996')
# print(b)
#------------------------
# 2-topshiriq



