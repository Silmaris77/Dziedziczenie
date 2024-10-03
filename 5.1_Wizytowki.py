from faker import Faker

fake = Faker()

class Kontakty:
    def __init__(self, first_name, last_name, address, e_mail):
         self.first_name = first_name
         self.last_name = last_name
         self.address = address
         self.e_mail = e_mail
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.e_mail}'

dane = []

for i in range(5):
    dane.append(Kontakty(fake.first_name(), fake.last_name(),fake.address(), fake.email()))

dane_by_name = sorted(dane, key=lambda name:name.first_name)
dane_by_lastname = sorted(dane, key=lambda lastname:lastname.last_name)
dane_by_email = sorted(dane, key=lambda email:email.e_mail)

print("Kontakty posortowane według imienia:")
for i in dane_by_name:
    print(i)
print("-" * 10)
print("Kontakty posortowane według nazwiska:")
for i in dane_by_lastname:
    print(i)
print("-" * 10)
print("Kontakty posortowane według e-mail:")
for i in dane_by_email:
    print(i)
print("-" * 10)