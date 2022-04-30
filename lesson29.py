class Talaba:
    def __init__(self,ism, familya,tyil):
        self.ism =ism
        self.familya =familya
        self.tyil= tyil
        self.bosqich =1

    def get_info(self):
        return f"Men {self.ism} {self.familya} {self.bosqich} -bosqich talabasiman "



class Fan:
    def __init__(self,name):
        self.name =name
        self.soni = 0
        self.talabalar =[]

    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.soni+=1

    def get_students(self):
        return [ talaba.get_info()   for talaba in self.talabalar]


talaba1 = Talaba("Azamat","Narzulloyev",1996)
talaba2 =Talaba('Baxrom','valiyev',1995)
talaba3 = Talaba('Asilbek','Narzulloyev',2003)

matematika = Fan('oliy matematika ')
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

# print(matematika.soni)
# print(matematika.get_students())
 




# Dunder — double underscore (ikki pastki chiziq) so'zlarining qisqartmasi.
def see_method(klass):
    for method in dir(klass):
        if method.startswith('__'):
            continue
        else:
            print(method)
    # return [ method for method in dir(klass) if method.startswith('__') is False]
    

# obj1 = see_method(Fan)
# print(obj1)

# print(talaba1.__dict__)
# print(talaba2.__dict__.keys())
print(dir(str))
