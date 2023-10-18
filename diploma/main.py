from Database import Database
from Person import Person
import sys

db = Database()

def validate(text, validate_func) :
    while True :
        user_input = input(text)
        if validate_func(user_input) :
            return user_input
        print('Invalid input. Please try again')

while True:
    print('Menu:')
    print('1. Add new person')
    print('2. Save person(s) to file')
    print('3. Search by name')
    print('4. Upload from file')
    print('5. Exit')

    choice = input('Your choise:\n > ')

    if choice == '1': # adding a new person
        # user enters FIO
        first_name  = validate('Enter the name > ', Person.is_correct_fio)
        last_name   = validate('Enter the last name   (Enter if not exist) > ', lambda value : value == '' or Person.is_correct_fio)
        middle_name = validate('Enter the middle name (Enter if not exist) > ', lambda value : value == '' or Person.is_correct_fio)

        last_name   = last_name   if last_name   else None
        middle_name = middle_name if middle_name else None

        # user enters Bdate, Ddate, gender
        birth_date = validate('Enter the birth date (in format DD.MM.YYYY) > ', Person.check_date)
        death_date = validate('Enter the death date (in format DD.MM.YYYY) > ', lambda value : value == '' or Person.check_date(value))
        gender     = validate('Enter the gender (M or F) ', Person.is_correct_gender).upper()

        death_date = death_date if death_date else None

        # all checks passed, adding person to database
        db.add_person(Person(first_name, gender, birth_date, last_name, middle_name, death_date))

    elif choice == '2': # saving all the data to file
        file_path = input('Save to file (name): ')
        db.save_to_file(file_path)

    elif choice == '3':
        filename    = input('Enter file name: ')
        name = input('Enter name of the person for search: ')
        
        people = db.search_by_name(filename, name)
        db.show_people(people)

    elif choice == '4':
        filename = input('Upload from file (name): ')
        people_from_db = db.load_from_file(filename)
        db.show_people(people_from_db)

    elif choice == '5':
        print('Goodbye!')
        sys.exit()

    else:
        print('Wrong choise, choose in 1,2,3,4,5 only please')
