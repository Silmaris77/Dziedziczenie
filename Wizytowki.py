from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, phone, e_mail):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.e_mail = e_mail

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.e_mail}'

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name) + 1

class BusinessContact(BaseContact):
    def __init__(self, position, company, work_phone, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.position = position
        self.company = company
        self.work_phone = work_phone

    def contact(self):
        print(f"Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.last_name}")

def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        if contact_type == 'base':
            contacts.append(BaseContact(
                fake.first_name(), fake.last_name(), fake.phone_number(), fake.email()
            ))
        elif contact_type == 'business':
            contacts.append(BusinessContact(
                fake.first_name(), fake.last_name(), fake.phone_number(), fake.email(),
                fake.job(), fake.company(), fake.phone_number()
            ))
    return contacts

# Example usage
prywatne = create_contacts('base', 5)
sluzbowe = create_contacts('business', 5)

print("Base Contacts:")
for contact in prywatne:
    print(contact)
    contact.contact()
    print(f"Długość etykiety: {contact.label_length}")
    print("-" * 10)

print("Business Contacts:")
for contact in sluzbowe:
    print(contact)
    contact.contact()
    print(f"Długość etykiety: {contact.label_length}")
    print("-" * 10)