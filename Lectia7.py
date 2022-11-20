# # # numar = 3
# # #
# # # try:
# # #       assert numar % 2 == 0, "pacat"
# # # except AssertionError as e:
# # #     print(e)
# #
# #
# # # def masina():
# # #     try:
# # #         numar_roti = int(input('Introdu numar de roti: '))
# # #     except ValueError:
# # #         print('Numarul nu este de tip integer')
# # #     try:
# # #         return numar_roti
# # #     except UnboundLocalError:
# # #         print('Nr roti este gol')
# # # masina()
# #
# # class om:
# #     def __init__(self, inaltime, greutate, culoare_ochi):
# #         self.inaltime = inaltime
# #         self.greutate = greutate
# #         self.culoare_ochi = culoare_ochi
# #     __tip_vesimentar = 'Elegant' # incapsulare
# # ion = om(180, 80 , 'Caprui')
# # ion.
# #
# # class Angajat(om):
# #     def __init__(self, inaltime, greutate, culoare_ochi):
# #         super().__init__(inaltime, greutate, culoare_ochi)
# # #
# # class elev_absolvent(om):
# #     def __init__(self, inaltime, greutate, culoare_ochi, clasa):
# #         super().__init__(inaltime, greutate, culoare_ochi)
# #         print('Invata fizica avansata')
# # elev1 = elev(120,50,'verzi',12)
# # elev2 = elev_absolvent(130,40,'caprui',12)
# # elev1.invata()
# # elev2.invata()
#
# #
# # class Angajat:
# #     nume = None
# #     prenume = None
# #     salariu = None
# #
# #     def __init__(self, a, b, c):
# #         self.nume = a
# #         self.prenume = b
# #         self.salariu = c
# #
# #     def descrie(self):
# #         print(f'Numele angajatului este: {self.nume} ')
# #         print(f'Prenumele angajatului este: {self.prenume}')
# #         print(f'Are salariul {self.salariu}')
# #
# #     def nume_complet(self):
# #         print(self.nume + ' ' + self.prenume)
# #
# #     def salariu_lunar(self):
# #         print(f'salariul lunar este de')
#
# from abc import abstractmethod
#
#
# class figura_geometrica():
#     @abstractmethod
#     def defineste_forma(self):
#         raise NotImplementedError
#
#     @abstractmethod
#     def stabileste_perimetrul(self):
#         raise NotImplementedError
#
#
# class patrat(figura_geometrica):
#     def defineste_forma(self):
#         numar_laturi = input('Introdu numarul laturilor')
#
#
# #
# # patrat1 = patrat
# # patrat1.defineste_forma()
#
#
# # class om:
# #    def __init__(self, inaltime, greutate, culoare_ochi):
# #         self.inaltime = inaltime
# #         self.greutate = greutate
# #         self.culoare_ochi = culoare_ochi
# #
# #
# # class elev(om):
# #     def __init__(self, inaltime, greutate, culoare_ochi, clasa):
# #         super().__init__(inaltime, greutate, culoare_ochi)
# #         self.clasa = clasa
#
# class French:
#     def say_hello(self):
#         print('Bonjour')
#
#
# class Chinese:
#     def say_hello(self):
#         print('Nihao')
#
#
#
# George = French()
# John = Chinese()
#
# for lang in (George,John):
#     lang.say_hello()

# class Tomato():
#     def type(self):
#         print("Vegetable")
#
#     def color(self):
#         print("Red")
#
#
# class Apple():
#     def type(self):
#         print("Fruit")
#
#     def color(self):
#         print("Red")
#
#
# def func(obj):
#     obj.type()
#     obj.color()
#
#
# obj_tomato = Tomato()
# obj_apple = Apple()
# func(obj_tomato)
# func(obj_apple)
#
# class India():
#     def capital(self):
#         print("New Delhi")
#
#     def language(self):
#         print("Hindi and English")
#
#
# class USA():
#     def capital(self):
#         print("Washington, D.C.")
#
#     def language(self):
#         print("English")
#
#
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
#     country.capital()
# country.language()

# class Belgia():
#     def bautura_traditionala(self):
#         print('Bere de abatie')
# class Franta():
#     def bautura_traditionala(self):
#         print('Vinul rosu')
#
# Belgia_bautura = Belgia()
# Franta_bautura = Franta()
# for bautura in (Belgia_bautura,Franta_bautura):
#     bautura.bautura_traditionala()


# def add(x, y, z = 0):
#     return x + y + z
# print(add(2,3))
# print(add(2,3,4))

# a = 5
# b = 2
#
# try:
#     print('Resource Open')
#     print(a/b)
#     k = int(input('Enter a number:'))
#     print(k)
# except ZeroDivisionError as e:
#     print('Hey you cannot divide a number by 0',e)
# except ValueError as e:
#     print('Invalid input')
# except Exception as e:
#     print('Something went wrong')


# class Animal():
#     def sound(self):
#         raise NotImplementedError
#     def sleep(self):
#         raise NotImplementedError
# class Dog(Animal):
#     def sound(self):
#         print('ham ham')
#     def sleep(self):
#         print('ZZZ')
# class Cat(Animal):
#     def sound(self):
#         print('Miau miau')
#     def sleep(self):
#         print('prrr')
#
# Dog1 = Dog()
# Cat1 = Cat()
# print(Dog1.sound())
# print(Cat1.sleep())
#
# # print(Cerc1.diametru())
# # print(Cerc1.circumeferinta())


# class Chef:
#     def make_salad(self):
#         print('salad')
#     def make_fries(self):
#         print('fries')
# class Japanesechef(Chef):
#     def make_sushi(self):
#         print('sushi')
# class Italianchef(Chef):
#     def make_sushi(self):
#         print('pizza')

# class Car:
#     __color = 'green'
#
# def get_color