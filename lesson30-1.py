class Shaxs:
    def __init__(self,ism,familya,tyil):
        self.ism = ism
        self.familya =familya
        self.tyil = tyil
        

    def get_info(self):
        return f"{self.ism} {self.familya}"

    def get_yosh(self,yil):
        return yil-self.tyil

class Talaba(Shaxs):
    def __init__(self,ism,familya,tyil,idraqam):
        super().__init__(ism,familya,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
      

    def set_bosqich(self,bosqich):
        self.bosqich= bosqich

    def get_bosqich(self):
        return self.bosqich
    

    def get_id(self):
        return self.idraqam
   
    def add_fan(self,fan):
        self.fanlar.append(fan)

    def get_fan(self):
        return [fan.get_name() for fan in self.fanlar]



class Fan():
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name


matematika  =Fan('Oliy matematika')
fizika =Fan('Fizika')
talaba  =Talaba('Azamat','Narzulloyev',1996,123,)
talaba.add_fan(matematika)
talaba.add_fan(fizika)
print(talaba.get_fan())
