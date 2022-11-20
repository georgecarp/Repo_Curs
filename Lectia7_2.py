# # 3. Clasa Angajat
# # Atribute: nume, prenume, salariu
# # Constructor pt toate atributele
# # Metode:
# # ● descrie()
# # ● nume_complet()
# # ● salariu_lunar()
# # ● salariu_anual()
# # ● marire_salariu(procent)
#
# class Angajat:
#     nume: None
#     prenume: None
#     salariu: None
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descriere(self):
#         return (self.nume, self.prenume, self.salariu)
#
#     def nume_complet(self):
#         return (self.nume + " " + self.prenume)
#
#     def salariu_lunar(self):
#         return (self.salariu)
#
#     def salariu_anual(self):
#         return (self.salariu * 12)
#
# # s = 100.000
# # p = 10
# # fin = 110.000
#     def marire_salariu(self, procent):
#         self.salariu = self.salariu + (self.salariu / 100 * procent)
#         print(f'Salariu marit = {self.salariu}')
#
#
# Angajat1 = Angajat('Carp', 'George', 7000)
# print(Angajat1.descriere())
# print(Angajat1.nume_complet())
# print(Angajat1.salariu_lunar())
# print(Angajat1.salariu_anual())
# print(Angajat1.marire_salariu(10))
#
# print(Angajat1.salariu_lunar())
# print(Angajat1.salariu_anual())
#
# print('##############################')
#
# print(Angajat1.marire_salariu(10))
#
# print(Angajat1.salariu_lunar())
# print(Angajat1.salariu_anual())