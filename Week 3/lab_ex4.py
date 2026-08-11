employee_1_name = input("Enter Employee 1 Name: ")
employee_1_email = input("Enter Employee 1 Email: ")
employee_1_dept_1 = input("Enter Employee 1 Department 1: ")
employee_1_dept_2 = input("Enter Employee 1 Department 2: ")
employee_1_sales = float(input("Enter Employee 1 Sales: "))

employee_one_dict = {
    "name": employee_1_name,
    "email": employee_1_email,
    "departments": [employee_1_dept_1, employee_1_dept_2],
    "sales": employee_1_sales
}

employee_2_name = input("Enter Employee 2 Name: ")
employee_2_email = input("Enter Employee 2 Email: ")   
employee_2_dept_1 = input("Enter Employee 2 Department 1: ")
employee_2_dept_2 = input("Enter Employee 2 Department 2: ")
employee_2_sales = float(input("Enter Employee 2 Sales: "))

employee_two_dict = {
    "name": employee_2_name,
    "email": employee_2_email,
    "departments": [employee_2_dept_1, employee_2_dept_2],
    "sales": employee_2_sales
}

list_employees = [employee_one_dict, employee_two_dict]
print(list_employees)

total_sales = list_employees[0]["sales"] + list_employees[1]["sales"] 
print("Total Sales: ", total_sales)

list_employees[0]["name"] = "Jane"
print(list_employees[0]["name"])