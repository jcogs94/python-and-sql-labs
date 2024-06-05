import os
from Database import Database

db = Database()
os.system('clear')
print('Welcome to the app.')
db.print_prompt()

running = True
while running:
    user_input = input('> ')
    match user_input:
        case '1':
            print('1')
        case '2':
            print('2')
        case '3':
            db.add_employee_prompt()
        case '4':
            print('4')
        case '5':
            print('5')
        case '6':
            print('6')
        case '7':
            print('7')
        case '8':
            print('8')
        case '9':
            running = False
        case _:
            print('Please enter a valid input.\n')
