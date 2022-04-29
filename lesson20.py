# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 22:53:08 2022

@author: user
"""

# def toliq_ism(ism,familya, otasi_ismi=''):
#     if otasi_ismi:
#         return f"{ism} {familya} {otasi_ismi}"
#     else:
#         return f"{ism} {familya}"
    
    
    
    
# ism1= toliq_ism('azamat', 'narzulloyev','anvar ogli')
# print(ism1)


def avto_info(kampanya, madel, rang, yil, narx=None):
    avto = {
        'kampanya':kampanya,
        'madel':madel,
        'rang':rang,
        'yil':yil,
        'narxi':narx

        }
    return avto
    

avto1 = avto_info('GM', 'lasette', 'qora', 2019)
avto2 = avto_info('Wolswagen', 'malorol', 'oq', 2020,20000)

avtolar = [avto1,avto2]


        