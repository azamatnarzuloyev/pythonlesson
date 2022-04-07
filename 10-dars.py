aftolar = ['bmv','mers', 'tayota', 'luks']

for i in aftolar:
    if i=='bmv':
        print(i.upper())
    else:
        print(i.title())

# lower() bu hariflar kichik harflarga ogirib beradi 
cars = ['toyota','Mazda','hyunda','gm','kia']

for car in cars:
    if car!='gm':
        print(car.title())
    else:
        print(car.upper())

ism = input("ismingizni kiriting ")
if ism=='Admin':
    print("xush kelibsiz admin foydalanuvchi ro'yhatini ko'rasizmi ")
else:
    print(f"xush kelibsiz {ism} ")

print("ikki son kiring")
a = input("birinchi sonni kiriting ")
b= input("ikkinchi sonni kiriting ")

if a==b:
    print("sonlar teng")
else:
    print("sonlar teng emas")