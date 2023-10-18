from datetime import datetime, date
import re

class Person:
    def __init__(self, first_name, gender, birth_date, last_name=None, middle_name=None, death_date=None) :
        self.first_name  = first_name
        self.last_name   = last_name
        self.middle_name = middle_name
        self.birth_date  = Person.normalize_date(birth_date)
        self.death_date  = Person.normalize_date(death_date) if death_date else None
        self.gender      = gender

    def __str__(self) :
        result_str =  f'Name: {self.first_name} '
        result_str += self.last_name   if self.last_name   else ''
        result_str += self.middle_name if self.middle_name else ''

        result_str += f', Age: {self.calculate_age()}'
        result_str += f', Sex: {self.gender}'
        return result_str

    def calculate_age(self) :
        sub_day = self.death_date
        if self.death_date is None :
            sub_day = date.today()
        return sub_day.year - self.birth_date.year - ((sub_day.month, sub_day.day) < (self.birth_date.month, self.birth_date.day))

    @staticmethod
    def normalize_date(rawdate) :
        try:
            return datetime.strptime(rawdate, '%Y-%m-%d').date()
        except ValueError:
            possible_delimeters = ['/', ' ', '-', '.']
            for delimiter in possible_delimeters :
                try :
                    return datetime.strptime(rawdate, f'%d{delimiter}%m{delimiter}%Y').date()
                except ValueError:
                    continue
            raise ValueError('Wrong data format')

    @staticmethod
    def check_date_format(date) :
        return bool(re.match(r'^(0?[1-9]|[12][0-9]|3[01])[./\s-](0?[1-9]|1[0-2])[./\s-](\d{4})$', date))

    @staticmethod
    def check_date(date) :
        return Person.check_date_format(date) and (Person.normalize_date(date) <= datetime.today().date())

    @staticmethod
    def is_correct_gender(gender) :
        return gender.upper() in ['M', 'F']

    @staticmethod
    def is_correct_fio(string) :
        return bool(re.match(r'^[А-Яа-яіІa-zA-Z]{1,15}$', string))
