# a = 5
# b = 3
# a+=(a+b)
# # a= a + [a*(b+2)]
# print(a)


# propozitie = 'Ana are mere.'
# fructe= 'mere'
# nume = propozitie[0:3] # pornire de la 0 si ia 3 elemente de la start
# print(nume)
#
# # if fructe == propozitie[8:len(propozitie)-1]:
#
# fructe = 'pere'
# nume = 'Ana'
#
# if fructe == 'mere' and nume == 'Ana':
#     print('Ana are 5 mere.')
# elif fructe == 'mere' and nume != 'Ana':
#     if fructe == 'mere':
#         print('fructele sunt mere')
# elif nume == "Ana":
#     print('Am fost aici')
# else:
#     print('Ana nu are mere')

# x = 4
#
# if x < 25 and not x >= 5:
#     print ('Numarul nu se regaseste intre 5 si 25')
# else:
#     print ('Numarul se regaseste intre 5 si 25')


# Tema extra

# 1
# str = input("Ce fel de articol doriti ?")

# x = len(str)
#
# y = x // 2
#
# print('Ce fel de articol doriti :', str[y])

# # 2
#
# def is_palindrome(numar):
#
# string = numar
# if (string== string [::-1]):
#     print("The string IS a palindrome")
#     return True
# else:
#     print("The string is NOT a palindrome")
#     return False
#
# assert is_palindrome ('cojoc')

# 3


# #leguma='rosie'
#
# # print(leguma(len(leguma))
#
# #declarare
#
# # nume,prenume,adresa,varsta='ion','popescu','romania',72
# # print(nume)
# # print(prenume)
# # print(adresa)
# #
# # scrisoare=nume + prenume + adresa
# # print(scrisoare)
#
# propozitie="Ionel pleaca la piata sa cumpere cartofi"
#
# # assert (type(propozitie)==str)
# # print('this line is 4')
#
# #assert len(propozitie) >1
#
# # propozitie2=input('Aceasta este propozitia :')
# # print(type(propozitie2))
# # propozitie2=input('Aceasta este varsta :')
# # print(type(propozitie2))
# print(propozitie[0: len(propozitie)-1: 2])

propozitie = 'Ana are mere.'
# print(propozitie[5]) # printeaza o variabila
# print(propozitie[5:]) #len returneaza un numar

# print(propozitie[5::-1])

# numar_spatii = propozitie.count(' ')
# print(propozitie.split(" "))
# for index in propozitie.split(" "):
#     if index == "mere.":
#         print(index[:len(index)-1])
#     elif index != "mere.":
#         print(index)
#
