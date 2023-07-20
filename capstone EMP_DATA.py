employees = [
    {
        'employee_id': 42001,
        'name': 'Este Haim',
        'gender': 'Female',
        'join date': '2022-10-01',
        'position': 'Manager',
        'salary': 10_000_000
    },
    {
        'employee_id': 42002,
        'name': 'Edward Halomoan',
        'gender': 'Male',
        'join date': '2018-09-08',
        'position': 'Eng Staff',
        'salary': 7_000_000
    },
    {
        'employee_id': 42003,
        'name': 'Gabe Michael',
        'gender': 'Male',
        'join date': '2014-04-10',
        'position': 'Adm Staff',
        'salary': 7_000_000
    },
    {
        'employee_id': 42004,
        'name': 'Danielle Hunter',
        'gender': 'Female',
        'join date': '2017-08-12',
        'position': 'Analyst',
        'salary': 8_000_000
    },
    {
        'employee_id': 42005,
        'name': 'Oliver Gosling',
        'gender': 'Male',
        'join date': '2008-12-11',
        'position': 'Manager',
        'salary': 10_000_000
    }
]

# MAIN MENU
def Main_Menu():
    print('''
    ====== WELCOME TO EMPLOYEE DATABASE ======
         ===== PT BE HAPPY BE REAL =====
             
    Main Menu :
    1. Show Employees Database
    2. Add Employee Data
    3. Delete Employee Data
    4. Update Employee Data
    5. Payslip
    6. Exit Program
''')

# Menu 1 READ/SHOW DATA
def Option_1_Show_Data():       
    while True:
        Show_Data_Menu = (input('''
        Employee Database :
        1.  Show all employee data
        2.  Show data by Employee ID
        3.  Back to Main Menu
        
        Please enter menu :  '''))

        if Show_Data_Menu == '1':
            all_data_employee()
        elif Show_Data_Menu == '2':
            specific_employee()
        elif Show_Data_Menu == '3':
            back_to_main = input('\nBack to Main Menu? (Y/N):').lower()
            if back_to_main == 'y':
                break
            elif back_to_main == 'n':
                continue
            else:
                print("Please input 'y' for Yes to continue or 'n' for No to back to main menu") 
        else:
            print("Data menu doesn't exist. Please input No. 1 - 3.")
            
# Sub-MENU SHOW ALL DATA
def all_data_employee():        
    if len(employees) == 0:
        print("Database doesn't exist")
    else:
        print('List All Employees \n')
        print('No.\t| Employee ID \t| Name     \t\t| Gender \t  | Join Date \t\t| Position      \t| Salary')
        print('------------------------------------------------------------------------------------------------------------------------')
        for i in range(len(employees)):
            print(f'{i+1} \t| {employees[i]["employee_id"]}\t\t| {employees[i]["name"]}     \t| {employees[i]["gender"]}    \t  | {employees[i]["join date"]} \t\t| {employees[i]["position"]}  \t\t|{employees[i]["salary"]}')

# Sub-MENU SHOW SPESIFIC DATA
def specific_employee():        
    if len(employees) == 0:
        print("Database doesn't exist")
    else:
        employee_id = input('Input Employee ID: ')
        if employee_id.isnumeric():
            employee_id = int(employee_id)
        for i in range(len(employees)):
            if employee_id == employees[i]['employee_id']:
                print(f'This is employee data with ID : {employee_id}')
                print('No.\t| Employee ID \t| Name     \t\t| Gender \t  | Join Date \t\t| Position      \t| Salary')
                print('------------------------------------------------------------------------------------------------------------------------')
                print(f'{i+1} \t| {employees[i]["employee_id"]}\t\t| {employees[i]["name"]}     \t| {employees[i]["gender"]}    \t  | {employees[i]["join date"]} \t\t| {employees[i]["position"]}  \t\t|{employees[i]["salary"]}')
                break
            elif (i == len(employees) - 1) and employee_id != employees[i]['employee_id']:
                print("Data doesn't exist. Try again.")

# MENU 2  CREATE DATA
def Option_2_Add_Data():
    while True:
        Add_Data = input('''
        Add Employee Database :

        1.  Add Employee Data
        2.  Back to Main Menu
        
        Please enter menu:  ''')

        if Add_Data == '1':
            add_employee()
        elif Add_Data == '2':
            exit_add_data = input('Back to Main Menu? (Y/N):').lower()
            if exit_add_data == 'y':
                break
            elif exit_add_data == 'n':
                continue
            else:
                print("Please input 'y' for Yes to continue or 'n' for No to back to main menu")    
        else:
            print("Data menu doesn't exist. Please input No. 1 or 2.") 

# Sub-MENU ADD DATA
def add_employee():
    ID = input('Input New employee ID : ')
    if ID.isnumeric():
        ID = int(ID)

    for i in range (len(employees)):
        if ID == employees[i]['employee_id']:
            print('Employee ID already exists. Input new ID.')
            break
        elif (i == len(employees) - 1) and ID != employees[i]['employee_id']:
            Name = input('Name : ').title()
            Gender = input('Gender: ').capitalize()
            Join_Date = input('Join Date (YYYY-MM-DD) : ')
            Position = input('Position: ').title()
            Salary = input('Salary: ')
            if Salary.isnumeric():
                Salary = int(Salary)
    
            save_data = input('Are you sure to save this data? (Y/N): ').lower()
            if save_data == 'y':
                print('"Data successfully saved"')
                employees.append({'employee_id':ID, 'name':Name,'gender':Gender,'join date':Join_Date,'position':Position,'salary':Salary})
            elif save_data == 'n':
                print('"Data not saved"')
            else:
                print("Please input 'y' for Yes to continue or 'n' for No to back to main menu")            

# MENU 3 DELETE DATA
def Option_3_Delete_Data(): 
    while True:
        Delete_Data = input('''
        Delete Employee :

        1.  Delete Employee Data
        2.  Back to Main Menu
        
        Please enter menu:  ''')

        if Delete_Data == '1':
            delete_employee()
        elif Delete_Data == '2':
            exit_del_data = input('Back to Main Menu? (Y/N):').lower()
            if exit_del_data == 'y':
                break
            elif exit_del_data == 'n':
                continue
            else:
                print("Please input 'y' for Yes to continue or 'n' for No to back to main menu")
        else:
            print("Data menu doesn't exist. Please input No. 1 or 2.")

#Sub-MENU DELETE DATA 
def delete_employee():
    del_id = input('Input Employee ID you want to delete: ')
    if del_id.isnumeric():
        del_id = int(del_id)

    for i in range (len(employees)):
        if del_id == employees[i]['employee_id']:
            print(f'This is employee data with ID : {del_id}')
            print('No.\t| Employee ID \t| Name     \t\t| Gender \t  | Join Date \t\t| Position      \t| Salary')
            print('------------------------------------------------------------------------------------------------------------------------')
            print(f'{i+1} \t| {employees[i]["employee_id"]}\t\t| {employees[i]["name"]}     \t| {employees[i]["gender"]}    \t  | {employees[i]["join date"]} \t\t| {employees[i]["position"]}  \t\t|{employees[i]["salary"]}')
    
            delete_data = input('Are you sure to delete this data? (Y/N): ').lower()
            if delete_data == 'y':
                print('"Data successfully deleted"')
                del employees[i]
                break
            elif delete_data == 'n':
                continue
            else:
                print("Please input 'y' for Yes to continue or 'n' for No to back to main menu")        
        elif (i == len(employees) - 1) and del_id != employees[i]['employee_id']:
            print("The data you are looking for doesn't exist")

# MENU 4 UPDATE DATA
def Option_4_Update_Data():
    while True:
        Update_Data = input('''
        Update Employee :

        1.  Update Employee Data
        2.  Back to Main Menu
        
        Please enter menu:  ''')

        if Update_Data == '1':
            update_employee()
        elif Update_Data == '2':
            exit_update_data = input('Back to Main Menu? (Y/N):').lower()
            if exit_update_data == 'y':
                break
            elif exit_update_data == 'n':
                continue
            else:
                print("Please input 'y' for Yes to continue or 'n' for No to back to main menu")       
        else:
            print("Data menu doesn't exist. Please input No. 1 or 2.")
            
#SUB-MENU UPDATE EMPLOYEE
def update_employee():
    id_update = input('Input Employee ID you want to update: ')
    if id_update.isnumeric():
        id_update = int(id_update)

    employee_found = False
    for i in range (len(employees)):
        if id_update == employees[i]['employee_id']:
            employee_found = True
            print(f'This is employee data with ID : {id_update}')
            print('No.\t| Employee ID \t| Name     \t\t| Gender \t  | Join Date \t\t| Position      \t| Salary')
            print('------------------------------------------------------------------------------------------------------------------------')
            print(f'{i+1} \t| {employees[i]["employee_id"]}\t\t| {employees[i]["name"]}     \t| {employees[i]["gender"]}    \t  | {employees[i]["join date"]} \t\t| {employees[i]["position"]}  \t\t|{employees[i]["salary"]}')
                
            update_data = input('Are you sure to continue update this employee data? (Y/N): ').lower()
            if update_data == 'y':
                continue_update = input('Choose column you want to update : ').lower()
                    
                if continue_update == 'employee id':    
                    new_ID = input('Input new Employee ID: ')
                    if new_ID.isnumeric():
                        new_ID = int(new_ID)
                    duplicate_ID = False
                    for employee in employees:
                        if new_ID == employee['employee_id']:
                            print('Employee ID already exists. Please input new ID.')
                            duplicate_ID = True       
                    if not duplicate_ID:
                        ok_to_update = input(f'Are you sure to change employee id with {new_ID} ? (Y/N): ').lower()
                        if ok_to_update == 'y':
                            employees[i]['employee_id'] = new_ID
                            print (f'"New name with {new_ID} successfully updated."')    
                        elif ok_to_update == 'n':
                            break
                        else:
                            print("Please input 'y' for Yes to continue or 'n' for No to cancel update")
                                       
                elif continue_update == 'name':
                    new_name = input('Input new Name: ').title()
                    ok_to_update = input(f'Are you sure to change name with {new_name} ? (Y/N): ').lower()
                    if ok_to_update == 'y':
                        employees[i]['name'] = new_name
                        print (f'"New name with {new_name} successfully updated."')  
                    elif ok_to_update == 'n':
                        break
                    else:
                        print("Please input 'y' for Yes to continue or 'n' for No to cancel update")
                            
                elif continue_update == 'gender':
                    new_gender = input('Input new Gender: ').capitalize()
                    ok_to_update = input(f'Are you sure to change gender with {new_gender} ? (Y/N): ').lower()
                    if ok_to_update == 'y':
                        employees[i]['gender'] = new_gender
                        print (f'"New gender with {new_gender} successfully updated."')   
                    elif ok_to_update == 'n':
                        break
                    else:
                        print("Please input 'y' for Yes to continue or 'n' for No to cancel update")
                        
                elif continue_update == 'join date':
                    new_join_date = input('Input new Join Date: ')
                    ok_to_update = input(f'Are you sure to change join date with {new_join_date} ? (Y/N): ').lower()
                    if ok_to_update == 'y':
                        employees[i]['join date'] = new_join_date
                        print (f'"New join date with {new_join_date} successfully updated."')
                            
                    elif ok_to_update == 'n':
                        break
                    else:
                        print("Please input 'y' for Yes to continue or 'n' for No to cancel update")
                            
                elif continue_update == 'position':
                    new_position = input('Input new Position: ').title()
                    ok_to_update = input(f'Are you sure to change position with {new_position} ? (Y/N): ').lower()
                    if ok_to_update == 'y':
                        employees[i]['position'] = new_position
                        print (f'"New position with {new_position} successfully updated."')
                    elif ok_to_update == 'n':
                        break
                    else:
                        print("Please input 'y' for Yes to continue or 'n' for No to cancel update")
                            
                elif continue_update == 'salary':
                    new_salary = input('Input new salary: ')
                    if new_salary.isnumeric():
                        new_salary = int(new_salary)
                    ok_to_update = input(f'Are you sure to change salary with {new_salary} ? (Y/N): ').lower()
                    if ok_to_update == 'y':
                        employees[i]['salary'] = new_salary
                        print (f'"New salary with {new_salary} successfully updated."')    
                    elif ok_to_update == 'n':
                        break
                    else:
                        print("Please input 'y' for Yes to continue or 'n' for No to cancel update")  
                else:
                    print("Sorry column doesn't exist")
                    break

    if not employee_found:
        print("The data you are looking for doesn't exist")

# MENU 5 PAYSLIP
def Options_5_Show_Salary():
    while True:
        Salary_Data = input('''
        Employee Payroll :

        1.  Print Payslip
        2.  Payroll Expenses                  
        3.  Back to Main Menu
        
        Please enter menu:  ''')

        if Salary_Data == '1':
            id_payslip = input('Input Employee ID: ')
            if id_payslip.isnumeric():
                id_payslip = int(id_payslip)
            for i in range(len(employees)):
                if id_payslip == employees[i]['employee_id']:
                    print(f'This is employee with ID : {id_payslip}')
                    print('No.\t| Employee ID \t| Name     \t\t| Gender \t  | Join Date \t\t| Position      \t| Salary')
                    print('------------------------------------------------------------------------------------------------------------------------')
                    print(f'{i+1} \t| {employees[i]["employee_id"]}\t\t| {employees[i]["name"]}     \t| {employees[i]["gender"]}    \t  | {employees[i]["join date"]} \t\t| {employees[i]["position"]}  \t\t|{employees[i]["salary"]}')
                
                    print_payslip = input('Do you want to print payslip? (Y/N) :').lower()
                    import math
                    if print_payslip == 'y':
                        payslip_period = input('Input Payroll Period you want to print (MM-YYYY) :  ')
                        overtime = int(input('Input total hours of overtime  : '))
                        OT_pay = math.ceil(overtime * 2 * employees[i]["salary"] / 173)
                        total_income = employees[i]["salary"] + OT_pay
                        tax = math.ceil(5 * employees[i]["salary"] / 100)
                        take_home_pay = total_income - tax
                        print(f'''
=========================================================
    PT BE HAPPY BE REAL                                                                                                                                                                                                    
    Payroll Period  : {payslip_period}                                           
    Employee ID     : {employees[i]["employee_id"]}                                                           
    Name            : {employees[i]["name"]}                              
    Position        : {employees[i]["position"]}                       
    Date of Join    : {employees[i]["join date"]}                         
                                                                        
    Basic Salary    : {employees[i]["salary"]}                                                                                                      
    Overtime Pay    : {OT_pay}                                                        
    TOTAL INCOME    : {total_income}                                      
                                                                         
    Deduction:                                                       
    Tax              : {tax}                                                       
    Total Deduction  : {tax}                                             
                                                                       
    TAKE HOME PAY    : {take_home_pay}                                                                          
 ==========================================================                                                    
      
-If you require further details, please personally approach the HRD staff-
      ''')
                        break
                    elif print_payslip == 'n':
                        break
                    else:
                        ("Please input 'y' for Yes to continue print or 'n' for No")
                        break
                elif (i == len(employees) - 1) and id_payslip != employees[i]['employee_id']:
                    print("Data payslip doesn't exist")
                    break
        
        elif Salary_Data == '2':
            company_total_salary = sum(employee['salary'] for employee in employees)
            print(f'Total company payroll expenses per month : {company_total_salary}')
            total_salary_year = company_total_salary * 12
            print(f'\nTotal company payroll expenses per year : {total_salary_year}')
            print('Please note that this information is based on the basic salary of all employees.')
        
        elif Salary_Data == '3':
            exit_salary = input('Back to Main Menu? (Y/N):').lower()
            if exit_salary == 'y':
                break
            elif exit_salary == 'n':
                continue
            else:
                print("Please input 'y' for Yes to continue or 'n' for No to back to main menu")
                
        else:
            print("Data menu doesn't exist. Please input No. 1-3.")           

# RUN PROGRAM
def run_program():
    while True:
        Main_Menu()
        Option = input('Input Options Menu: ')
        if Option == '1':
            Option_1_Show_Data()
        elif Option == '2':
            Option_2_Add_Data()
        elif Option == '3':
            Option_3_Delete_Data()
        elif Option == '4':
            Option_4_Update_Data()
        elif Option == '5':
            Options_5_Show_Salary()
        elif Option == '6':
            print('Thank you! Be Happy Be Real!')
            break
        else:
            print('The option you entered is not valid.')
run_program()