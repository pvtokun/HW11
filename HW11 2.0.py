from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self._is_valid_phone(value):
            raise ValueError("Неправильний формат номера телефону.")
        super().__init__(value)

    def _is_valid_phone(self, value):
        # Реалізуйте логіку перевірки номера телефону тут
        # Поверніть True, якщо номер телефону є коректним, False в іншому випадку
        # Наприклад: перевірка, чи номер телефону має 10 цифр
        return len(str(value)) == 10



class Birthday(Field):
    def __init__(self, value):
        if not self._is_valid_birthday(value):
            raise ValueError("Неправильний формат дня народження.")
        super().__init__(value)

    def _is_valid_birthday(self, value):
        # Реалізуйте логіку перевірки дня народження тут
        # Поверніть True, якщо день народження є коректним, False в іншому випадку
        # Наприклад: перевірка, чи дата дня народження є коректною
        try:
            datetime.strptime(str(value), "%Y-%m-%d")
            return True
        except ValueError:
            return False



class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.today().date()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day).date()
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day).date()
            days_left = (next_birthday - today).days
            return days_left


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, name):
        del self.data[name]

    def search(self, search_term):
        # Реалізуйте функціонал пошуку записів за ім'ям або іншими параметрами
        # Повертайте список знайдених записів
        pass

    def __iter__(self):
        return iter(self.data.values())

    def iterator(self, n):
        if n <= 0:
            raise ValueError("Кількість записів на сторінку повинна бути додатним числом.")
        
        count = 0
        current_page = []
        for record in self:
            current_page.append(record)
            count += 1
            if count == n:
                yield current_page
                current_page = []
                count = 0
        if current_page:
            yield current_page
