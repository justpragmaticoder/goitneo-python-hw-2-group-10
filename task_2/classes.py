from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def get_value(self):
        return self.value


class Phone(Field):
    def get_value(self):
        return self.value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def get_name(self):
        return self.name

    def add_phone(self, phone_number):
        if phone_number:
            self.phones.append(Phone(phone_number))

    def edit_phone(self, number_to_edit, new_number):
        if not (number_to_edit or new_number):
            return self.phones

        for index, phone in enumerate(self.phones):
            if phone.get_value() == number_to_edit:
                self.phones[index] = Phone(new_number)
                break

        return self.phones

    def find_phone(self, phone_number):
        if not phone_number:
            return None

        return next(
            filter(lambda number: number.get_value() == phone_number, self.phones),
            None,
        )

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        if not record:
            return

        record_name = record.get_name()
        self.data[record_name.get_value()] = record

    def find(self, key):
        res = self.data.get(key)
        return res

    def delete(self, key):
        del self.data[key]
