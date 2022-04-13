class Talaba:
    def __init__(self, ism, familya, tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
   
    def get_name(self):
        return self.ism.title()

    def tanishtir(self):
        return f"Mening ism {self.ism}" 

talaba1 = Talaba('azamat', 'narzulloyev', 1996)

# print(talaba1.tyil)
# print(talaba1.tanishtir())
print(talaba1.get_name())