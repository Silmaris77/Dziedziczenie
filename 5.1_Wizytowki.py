from faker import Faker

fake = Faker()

class Kontakty:
    def __init__(self, name, address, e_mail):
         self.name = name
         self.address = address
         self.e_mail = e_mail

dane = []

for i in range(5):
    dane.append(Kontakty(fake.name(), fake.address(), fake.email()))

nowy = Kontakty("Pawel Ksiazyk", "Warszawa, ul. Marszalkowska 30/45", "pksi@popsdf.pl")
dane.append(nowy)
for i in dane:
    print(f"{i.name}, {i.address}, {i.e_mail}.\n")