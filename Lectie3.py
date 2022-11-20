#structuri de date

# lista poate a avea mai multe tipuri de variabile:caractere,numere,boleane,se foloseste [
# dictionar foloseste tip de date cheie:valoare,se foloseste {
# set se foloseste {,valorile sunt unice
# tuple se folosesc (,valori ordonate.valorile sunt inmutabile.

# lista

# lista = (1,5)
# print(lista)
# # lista.append(7)
# print(lista)
# print(type(lista))

# print(lista + (1,5))

# lista2 = (lista + (1,5))
# print(lista2)
# -- lista
# masina = {'culoare','roti','scaune','lungime','culoare'}
# print(masina)
# # print(masina[2])
# masina.copy()

# -- dictionar

# dictionar = { 'culoare':'verde','roti':'4','marca':'BMW','specificatii':{'lungime':20,'latime':10}}
# print(dictionar)
# # print(dictionar.get('specificatii').get('latime'))
# print(len(dictionar))
#
# dictionar2 = {
#     'putere':250,
#     'model':520,
# }
# # print(dictionar['roti'].replace(dictionar2['model','roti']))
# print(dictionar.get('roti').replace('4','6'))
# print(dictionar.update('roti').replace('4','6'))


#array o structura care tine sub acceiasi umbrela mai multe date

# listele in pyton pot sa cuprinda elemete de tipuri diferite
# au dimensiune dinamica
# sunt mutabile putem modifica elemente

# fructe = ['mar','banana',3,True]
# print(fructe)
#
# # accesam un element in functie de index
#
# print(fructe[1])
# # adaugam un nou element
# fructe.append('rosie')
# print(fructe)
#
# #suprascriem un element
#
# fructe[0] = 'para'
# print(fructe)
#
# #aflam dimensiunea
# print(len(fructe))
#
# #scoate si ne returneaza ultimul element
#
# last = fructe.pop()
#
# print(last)
# print(fructe)
#
# # de cate ori apare un element
#
# print(fructe.count(3))
# # extindem lista
#
# fructe_exotice = ['ananas','kiwi']
#
# fructe.extend(fructe_exotice)
# print(fructe)

# nums = [36,25,96,22,14,67,88]
# names = ['kiran','navin','john']
#
# print(max(nums))


# nums.extend([100,136])
# nums.remove(25)
# push and pop push=adauga pop remove
# names.clear()
# nums.append(45)
# nums.extend(names)
# mil = [nums,names]
# print(mil)
# nums.insert(2,47)
# names.pop(2)




#tupples

# nu putem schimba valor

tup = (21,36,14,25)

# print(type(tup))
# print(tup[1])

#seturi

# nu accepta duplicate
# nu sunt ordonate

# set = {22,25,14,21,5}

# print(type(set))
# print(set)

# dictionare

# data = {1:'Navin',2:'Kiran',4:'Hars'}
# # print(type(data))
# # print(data[2])
# # print(data.get(3,'Not found'))
# keys = ['Navin','Kiran','Hars']
# values = ['Pyton','Java','JS']
# data = dict(zip(keys,values))
# data['George']='CC'
# data['Monika'] = 'CS'
# del data['Hars']
# print(data)

# prog = {'JS':'Atom','CS':'VS','Pyton':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
# print(prog['Java']['JEE'])

# thislist = ['do','re','mi','fa','sol','la','si','do']
# thislist=thislist[::-1]
# print(thislist)

# data = {1:'Navin',2:'Kiran',4:'Harsh'}

# print(data.get(3)) o sa aduca ca rezultat non
# print(data.get(1))
# print(data[3]) o sa dea eroare sau nu v-a aduce nimic pt ca nu avem valoare 3
# print(data.get(1)) luam o anumita valuare
# print(data[2]) printam valoare nr 2 folosind cheia (mandatory)

# keys = ['Navin','Kiran','Hars']
# values = ['Pyton','Java','JS']
# data = dict(zip(keys,values))
# # print(data['Kiran'])
# # print(data['Monika'])
# data['Monika']='CS'
# # print(data)
# del data['Hars']
# print(data)


# prog = {'JS':'Atom','CS':'VS','Pyton':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
# prog.update({'DEE':'SQL'})
# print(prog)


#tupple

#

tup = (21,36,14,25)
print(len(tup))
# print(tup[1])