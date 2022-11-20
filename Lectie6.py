# # # class Masina:
# # #     culoare = None
# # #     roti = None
# # #     tractiune = None
# # #     forma = None
# # #
# # #
# # #     def putere(self):
# # #         if self.tractiune == 4:
# # #             print('Puterea creste cu 50CP')
# # #
# # # object = Masina()
# # # object.tractiune = 4
# # # object.putere()
# # #
# # # class Floare:
# # #     petale = 4
# # #     culoare = 'Rosie'
# # #     inaltime = 5
# # #
# # #     # constructor
# # #     def __init__(self, a, b):
# # #         self.culoare = a
# # #         self.inaltime = b
# # #
# # #     def verifica_floarea(self):
# # #         if self.culoare == 'Rosie':
# # #             print('Floarea este trandafir')
# # #         elif self.culoare == 'Galben':
# # #             print('Floarea este galbena')
# # #
# # #     def verifica_inaltime(self):
# # #         if not self.inaltime == 0:
# # #             print('Floarea este vie')
# # #         else:
# # #             print('Floarea este moarta')
# # #             return True
# #
# # class Floare2:
# #     petale = None
# #     culoare = None
# #     inaltime = None
# #
# #     # constructor
# #     def __init__(self, _culoare, _inaltime):
# #         self.culoare = _culoare
# #         self.inaltime = _inaltime
# #
# #     def verifica_floarea(self):
# #         if self.culoare == 'Rosie':
# #             print('Floarea este trandafir')
# #         elif self.culoare == 'Galben':
# #             print('Floarea este galbena')
# #
# #     def verifica_inaltime(self):
# #         if not self.inaltime == 0:
# #             print(f'Floarea este vie - {self.inaltime}')
# #         else:
# #             print(f'Floarea este moarta - {self.inaltime}')
# #             return True
# #
# #
# # floare1 = Floare2('albastra', 23)
# # floare2 = Floare2('rosu', 4)
# # floare3 = Floare2('alb', 0)
# #
# # floare1.verifica_inaltime()
# # floare2.verifica_inaltime()
# # floare3.verifica_inaltime()
# #
# # # clasa,obiect,atribute/field,metode,constructor
# # # ctril +alt +l aranjare in pagina
#
#
# class Cerc:
#     raza = None
#     culoare = None
#
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#     def descriere_cerc(self):
#         return(self.raza,self.culoare)
#
#     def area(self):
#         return math.pi * raza * raza
#
#     def diametru(self):
#         return 2*raza
#
#     def circumeferinta(self):
#         return math.pi * raza * raza
#
# raza = float(input(' Please Enter the radius of a circle: '))
#
# Cerc1 = Cerc(8,'Verde')
# print(Cerc1.descriere_cerc())
# print(Cerc1.area())
# print(Cerc1.diametru())
# print(Cerc1.circumeferinta())
#
