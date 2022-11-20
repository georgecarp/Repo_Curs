# FUNCTII

# functii simple
# functii parametri
# functii cu return
# functii cu parametri si return


# functiile pornesc mereu cu "def",parantezele sunt locurile un primesc parametri

# def hi():
#     print('Hi!')
#
# hi()
# hi('Test')
# ------------------------------

# def hi(user):
#     print('Hi!')
#
# hi('Test')
#-------------------------
# verifica daca variabila este string

# x = input('Introduceti o variabila: ')
#
# def verifica_variabila(user):
#     print((type(user))
#     if type(user) == str:
#         print(f'Variabila {user} este un {type(user)}')
#     elif type(user) != str:
#         user2 = user
#         user = str(user)
#         print(f'Variabila {user} a fost convertita din {type(user2)} in {type(user)}')
#         return user
#     else:
#         print(f'Variabila este goala')


#verifica_variabila(x)

#----------------------------

# x = int(input('x = '))
# y = int(input('y = '))

# def suma(x,y):
#     print(x+y)
#
# suma(x,y)

# def suma(a,b):
#     z = a + b
#     return z
# def suma2(h):
#     d=h + suma(5,6)
#     return d
#
# print(suma2(suma(x,y)))



# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
#
#
# raspuns = []
#
# def functie(l1,l2):
#     for i in range(len(l1)):
#         for j in range(len(l2)):
#             if l1[i] == l2[j]:
#                 raspuns.append(l1[i])
#     return raspuns
# print(functie(list1,list2))
#-------------------------------------------------------------
# def numar(valoare =int(input('Numarul este:'))):
#     if valoare %2==0:
#         return True
#     else:
#         return False
# rezultat = numar()
# print(rezultat)

# create liste

# def create_a_list(list):
#     list2 = str(list)
#     list2.split(',')
#     return list2
#
# x = create_a_list('5,4,3,2')
# print(x)
# print(type(x))

# -------------------------------------------------------

# l = int(input('Lungimea listei este: '))
# list = []
#
# for i in range(l):
#     x = input('Introdu` un element in lista: ')
#     list.append(x)
# print(list)

# -------------------------------------------------------------

# list = []
#
# while 1 != 0:
#     x = input('Introdu` un element in lista: ')
#     if x == '':
#         break
#     list.append(int(x))
#
# print(list)

