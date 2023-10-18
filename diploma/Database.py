from Person  import Person
from os.path import exists
import csv

class Database:
    def __init__(self) :
        self.people = []

    def add_person(self, person) :
        self.people.append(person)

    def search_by_name(self, file_path, query):
        people = self.load_from_file(file_path)
        result = []
        for person in people :
            if query in person.first_name :
                result.append(person)
        return result        

    def save_to_file(self, file_path) :
        fieldnames = ['First Name', 'Last Name', 'Middle Name', 'Birth Date', 'Death Date', 'Gender'] if not exists(file_path) else ''
        try :
            with open(file_path, 'a', encoding='utf-8') as csv_file :

                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(fieldnames)
                for person in self.people:
                    writer.writerow([
                        person.first_name,
                        person.last_name,
                        person.middle_name,
                        person.birth_date,
                        person.death_date,
                        'Male' if person.gender == 'M' else 'Female',
                    ])
                print(f"Data successfully saved to {file_path}")
        except Exception as e :
            raise Exception(f'Error occurred while saving: {str(e)}')

    def load_from_file(self, file_path) :
        try:
            with open(file_path, 'r') as csv_file:
                csvreader = csv.reader(csv_file)
                next(csvreader) # skip header line
                rawdata = [person for person in [row for row in csvreader] if person != []]
                if rawdata :
                    return self.create_people(rawdata)
                return f'File {file_path} is empty.'
        except FileNotFoundError:
            print(f'File {file_path} not found.')

    def create_people(self, data) :
        person_list = []
        for item in data :
            person_list.append(Person(item[0], item[5], item[3], item[1], item[2], item[4]))
        return person_list

    def show_people(self, people) :
        for person in people :
            print(person)
