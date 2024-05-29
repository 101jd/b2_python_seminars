"""
Дополнено: копированием файла, редактированием записей и поиском
"""

from csv import DictReader, DictWriter
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def standart_write(filename, res):
    with open(filename, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['firstname', 'secondname', 'number'])
        f_w.writeheader()
        f_w.writerows(res)

def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Name: ')
            if len(first_name) < 2:
                raise NameError('Too short name')
            second_name = input('Surname: ')
            if len(second_name) < 4:
                raise NameError('Too short surname')
            phone_number = input('Number: ')
            if len(phone_number) < 11:
                raise NameError('Too short number')
        except NameError as err:
            print(err)
        else: 
            flag = True
    return[first_name, second_name, phone_number]

def create_file(filename):
    with open(filename, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['firstname', 'secondname','number'])
        f_w.writeheader()
        
def remove_row(filename):
    search = int(input('Number of row to del: '))
    res = read_file(filename)
    if search <= len(res):
        res.pop(search-1)
        standart_write(filename, res)
    else: print('Agrrrr!')
    
def write_file(filename):
    user_data = get_info()
    res = read_file(filename)
    new_obj = {'firstname' : user_data[0], 'secondname' : user_data[1], 'number' : user_data[2]}
    res.append(new_obj)
    standart_write(filename, res)


def read_file(filename):
    with open(filename, encoding='UTF-8') as data:
        f_r = DictReader(data)
        return list(f_r) # список словарей
    
def copy_file(filename, new_filename):    # ДЗ
    temp = read_file(filename)
    standart_write(new_filename, temp)
    
def search(filename, search_key):
    temp = read_file(filename)
    for el in temp:
        for val in el.values():
            if search_key in val:
                print(el)
                
def edit(filename, row, key):
    temp = read_file(filename)
    if row <= len(temp):
        temp[row-1][key] = input('New value: ')
        standart_write(filename, temp)

filename = 'phone.csv'
def main():
    
    while True:
        command = input('Enter com ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(filename):
                create_file(filename)
            write_file(filename)
        elif command == 'r':
            if not exists(filename):
                print('No file, enter "w"')
                continue
            print(*read_file(filename))
        elif command == 'd':
            if not exists(filename):
                print('No file, enter "w"')
                continue
            remove_row(filename)
        elif command == 'c':
            copy_file(filename, f'{input("New file name: ")}.csv')
        elif command == 's':
            if not exists(filename):
                print('No file, enter "w"')
                continue
            search(filename, input('Find: '))
            
        elif command == 'e':
            if not exists(filename):
                print('No file, enter "w"')
                continue
            row = int(input("Number of row: "))
            key = input("'n' for name; 's' for surname; '#' for number: ")
            if key.lower() == 'n':
                edit(filename, row, 'firstname')
            elif key.lower() == 's':
                edit(filename, row, 'secondname')
            elif key == '#':
                edit(filename, row, 'number')
            
main()

# copy_data file A to file B: read_file, standart_write(phone2)
# 'c' in main()
