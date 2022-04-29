
import random
def sontop_pc(x=10):
    print(f"1 dan {x} son o'yladim topa olasizmi ")
    natija = 1
    son = random.randint(1,x)
    while True:
        a= int(input(">>> "))
        if son>a:
            print("men o'ylagan son bundan kattaroq ")
            natija+=1
        elif a>son:
            print("men o'ygan son bundan kichikroq ")
            natija+=1
        else:
            print("tabriklaymiz siz yutdingiz")
            print(f"Siz {natija} taxmin bilan topdingiz ")
            break
    return natija


def sontop(x=10):
    print("Keling siz son o'ylaysiz men topishga harakat qilaman ")
    input(" o'ynash uchun ixtiyoriy kinobkani bosing ")
    
    natija =1 
    quyi =1
    yuqori =x
    while True:
      
        if quyi!=yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin= quyi
        javob = input(f"siz {taxmin} sonni o'yladingiz agar katta(+) kichik bo'lsa(-) teng bo'lsa(t) ".lower())
        if javob=='+':
            quyi =taxmin+1
            natija+=1
        elif javob=='-':
            yuqori = taxmin-1
            natija+=1
        elif javob=='t': 
            break
        else:
            print("Iltimos sonni to'g'ri kiriting ")
    print(f"men {natija} taxmin bilan topdim ")
    return natija
   

def play():
    kirit = True
    while kirit:
        sontop_foydalanuvchi = sontop_pc()
        sontop_computer= sontop()
        if sontop_computer<sontop_foydalanuvchi:
            print(f"men sizni yutdim {sontop_computer}")
        elif sontop_computer>sontop_foydalanuvchi:
            print(f"men yutqazdim siz {sontop_foydalanuvchi} yuddingiz  ")
        else:
            print("Durrang ") 
        kirit = input("yana o'ynamoqchimisz ha(1) yoq(0) ")
        
play()




