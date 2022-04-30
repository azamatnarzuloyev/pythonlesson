# x= '10'
# print(type(x))


# def salom_ber():
#     print("hello word")

# print(type(salom_ber))

class User:
    def __init__(self,first_name, last_name, age):
        self.first_name =first_name
        self.last_name = last_name
        self.age =age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def yosh(self,yil):
        return f"{yil-self.age}"

    def manzil(self):
        pass
        

user1= User('Azamat','Narzulloyev',26)

print(user1.full_name())
print(user1.yosh(2022))

# pass operatoridan if-else, for, while operatorlari badanida ham foydalanish mumkin














