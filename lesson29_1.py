class Afto:
    def __init__(self,madel, rang, karabka):
        self.madel = madel
        self.rang =rang
        self.karobka = karabka
        self.klametr =0

    def get_color(self):
        return f"{self.madel}"
    
    def get_model(self):
        return f"{self.madel}"


    def set_klametr(self,klametr):
        self.klametr= klametr
    def get_klametr(self):
        return self.klametr

car1 = Afto('gm','oq','aftomat')
car1.set_klametr(1000)
# print(car1.get_klametr())
# print(car1.__dict__.keys())
# print(car1.__dict__.values())

        