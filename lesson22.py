# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:29:27 2022

@author: user
"""

"""
*args , **kwarse usullari haqida
*args bu funksiydaargument qaytaradi 
**kwarse esa funksiyda ro'yhat qanyaradi '
"""
# def sonlar(x,y,*args):
#     summa=1
#     for i in args:
#         summa=summa*i
#     return summa*y*x
        
    
# son1= sonlar(2, 3, 4,5,6,7,8)

def talabalar(ism, familya, **malumotlar):
    malumotlar['ism']=ism
    malumotlar['familya']=familya
    return malumotlar


talaba1 = talabalar('azamat', 'narzulloyev', yosh=26,manzil='bukhara')    
    
    
