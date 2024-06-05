import os
from prettytable import PrettyTable

class Database:
    def print_prompt (self):
        print('''
Please select what you would like to do:
    1. View all employees
    2. View all companies
    3. Add new employee
    4. Add new company
    5. Update employee
    6. Update company
    7. Delete employee
    8. Delete company
    9. Quit
''')

    def view_employees (self, updating):
        os.system('clear')
        if updating:
            print('=========')
            print('Employees')
            print('=========\n')
        else:
            print('==============')
            print('View Employees')
            print('==============\n')

        self.cursor.execute('SELECT * FROM employees')
        data = self.cursor.fetchall()
        valid_ids = []

        if updating:
            output_table = PrettyTable(['ID', 'First', 'Last', 'Age', 'Email'])
            for entry in data:
                valid_ids.append(entry[0])
                output_table.add_row([entry[0], entry[1], entry[2], entry[3], entry[4]])
        else:
            output_table = PrettyTable(['First', 'Last', 'Age', 'Email'])
            for entry in data:
                output_table.add_row([entry[1], entry[2], entry[3], entry[4]])
        
        print(output_table, '\n')

        if not updating:
            input('[Enter] to go back to menu. ')

            os.system('clear')
            self.print_prompt()
        else:
            return valid_ids
    
    def view_companies (self):
        os.system('clear')
        print('==============')
        print('View Companies')
        print('==============\n')

        self.cursor.execute('SELECT * FROM companies')
        data = self.cursor.fetchall()

        output_table = PrettyTable(['Name', 'State'])
        for entry in data:
            output_table.add_row([entry[1], entry[2]])
        
        print(output_table, '\n')
        input('[Enter] to go back to menu. ')

        os.system('clear')
        self.print_prompt()
    
    def add_employee (self, first, last, age, email):
        self.cursor.execute('''INSERT INTO employees 
                ( first_name, last_name, age, email )
            VALUES
                (%s, %s, %s, %s)
            ''', [first, last, age, email])
        self.connection.commit()
        
        os.system('clear')
        print('New employee added...')
        self.print_prompt()
    
    def add_employee_prompt (self):
        os.system('clear')
        print('================')
        print('Add New Employee')
        print('================\n')
        
        valid_first, valid_last, valid_age, valid_email = [False, False, False, False]

        while valid_first == False:
            first_name = input('First name: ')
            if len(first_name) <= 20:
                valid_first = True
            else:
                print('Invalid input. Try again.\n')
        
        while valid_last == False:
            last_name = input('Last name: ')
            if len(last_name) <= 20:
                valid_last = True
            else:
                print('Invalid input. Try again.\n')
        
        while valid_age == False:
            age = input('Age: ')
            try:
                age = int(age)
                valid_age = True
            except ValueError:
                print('Invalid input. Try again.\n')

        while valid_email == False:
            email = input('Email: ')
            if len(email) <= 32:
                valid_email = True
            else:
                print('Invalid input. Try again.\n')
        
        self.add_employee(first_name, last_name, age, email)
    
    def add_company (self, name, state):
        self.cursor.execute('''INSERT INTO companies 
                ( name, state )
            VALUES
                (%s, %s)
            ''', [name, state])
        self.connection.commit()
        
        os.system('clear')
        print('New company added...')
        self.print_prompt()
    
    def add_company_prompt (self):
        os.system('clear')
        print('===============')
        print('Add New Company')
        print('===============\n')
        
        valid_name, valid_state = [False, False]

        while valid_name == False:
            name = input('Company name: ')
            if len(name) <= 20:
                valid_name = True
            else:
                print('Invalid input. Try again.\n')
        
        while valid_state == False:
            state = input("Company state (2 character abbreviation, ex. 'NY'): ")
            if len(state) == 2:
                valid_state = True
            else:
                print('Invalid input. Try again.\n')
        
        self.add_company(name, state)
    
    def update_employee (self, id, property, value):
        self.cursor.execute(("UPDATE employees SET " + property + " = %s WHERE id = %s"), [value, id])
        self.connection.commit()
    
    def update_employee_prompt (self):
        valid_ids = self.view_employees(True)
        employee_id = ''

        valid_id_selected = False
        while not valid_id_selected:
            employee_id = input('Please enter the ID of the employee you would like to update: ')
            
            if int(employee_id) in valid_ids:
                employee_id = int(employee_id)
                valid_id_selected = True
            else:
                print('Invalid input. Please try again.\n')
        
        print('\n===============')
        print('Update Employee')
        print('===============')

        user_updating = True
        while user_updating:
            print('''
What would you like to update?
    1. First name
    2. Last name
    3. Age
    4. Email
    5. Done Updating
            ''')
            
            update_selection = input('> ')
            match update_selection:
                case '1':
                    valid_name, name = [False, '']
                    while not valid_name:
                        name = input('\nNew first name: ')
                        if len(name) <= 20:
                            valid_name = True
                        else:
                            print('Invalid input. Please try again.\n')
                    
                    self.update_employee(employee_id, 'first_name', name)
                case '2':
                    valid_name, name = [False, '']
                    while not valid_name:
                        name = input('\nNew last name: ')
                        if len(name) <= 20:
                            valid_name = True
                        else:
                            print('Invalid input. Please try again.\n')
                    
                    self.update_employee(employee_id, 'last_name', name)
                case '3':
                    valid_age, age = [False, '']
                    while not valid_age:
                        age = input('\nNew age: ')
                        try:
                            age = int(age)
                            valid_age = True
                        except ValueError:
                            print('Invalid input. Try again.\n')
                    
                    self.update_employee(employee_id, 'age', age)
                case '4':
                    valid_email, email = [False, '']
                    while not valid_email:
                        email = input('\nNew email: ')
                        if len(email) <= 32:
                            valid_email = True
                        else:
                            print('Invalid input. Please try again.\n')
                    
                    self.update_employee(employee_id, 'email', email)
                case '5':
                    user_updating = False
                case _:
                    print('Invalid input. Please try again.\n')
        
        os.system('clear')
        print('Employee updated...')
        self.print_prompt()
    
    def __init__ (self, connection, cursor):
        self.connection = connection
        self.cursor = cursor


# # SHOW ALL ENTRIES FOR TESTING
# # Show all employee entries
# cursor.execute('SELECT * FROM employees')
# print(cursor.fetchall())

# # Show all company entries
# cursor.execute('SELECT * FROM companies')
# print(cursor.fetchall())

# # Show all role entries
# cursor.execute('SELECT * FROM roles')
# print(cursor.fetchall())
