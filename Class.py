from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


class Name(Field):
    def __init__(self, value):
        self.value = value.capitalize()


class Phone(Field):
    pass


class Record():
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def __str__(self):
        return f"{self.name} - {', '.join([str(p) for p in self.phones])}"

    def __repr__(self):
        return f"{self.name} - {self.phones}"

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def delete_phone(self, phone: Phone):
        for p in self.phones:
            if p.value == phone.value:
                self.phones.remove(p)
                return f'Phone {p.value} delete successful.'
        return f'Phone {phone.value} not found'


class AddressBook(UserDict):
    def add_record(self, rec: Record):
        self[rec.name.value] = rec

    def __str__(self):
        return '\n'.join([str(i) for i in self.values()])
