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
    def __init__(self,ism,familya,tyil,idraqam,manzil,dostlari):
        super().__init__(ism,familya,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil= manzil
        self.dostlari = dostlari

    def set_bosqich(self,bosqich):
        self.bosqich= bosqich

    def get_bosqich(self):
        return self.bosqich

    def get_id(self):
        return self.idraqam
        
class Manzil:
    def __init__(self,tuman,viloyat,uy,kocha):
        self.tuman =tuman
        self.viloyat = viloyat
        self.uy =uy
        self.kocha =kocha

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

class Dostlar:
    def __init__(self,name):
        self.name = name
 
    def get_name(self):
        return self.name

talaba_dostlari = Dostlar('Murod')
talaba_manzil = Manzil('Shofirkon','Buxoro','34',"Bog'iqo'rg'on")

talaba  =Talaba('Azamat','Narzulloyev',1996,123,talaba_manzil,talaba_dostlari)

# print(talaba.manzil.get_manzil())
# print(talaba.dostlari.get_name())
# print(talaba.get_yosh(2022))


