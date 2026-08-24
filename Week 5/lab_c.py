list_employees = []

for employee_number in range(1, 3):

    employee_name = input("Employee " + str(employee_number) + " Name: ")
    employee_email = input("Employee " + str(employee_number) + " Email: ")

    department_list = []

    for department_number in range(1, 3):
        department_code = int(input(
            "Employee " + str(employee_number) +
            " Department Code " + str(department_number) + ": "
        ))
        department_list.append(department_code)

    employee_sales = float(input(
        "Employee " + str(employee_number) + " Sales: "
    ))

    employee_dict = {
        "name": employee_name,
        "email": employee_email,
        "departments": department_list,
        "sales": employee_sales
    }

    list_employees.append(employee_dict)


print(list_employees)

total_sales = list_employees[0]["sales"] + list_employees[1]["sales"]

print(total_sales)

list_employees[0]["name"] = "Jane"

print(list_employees[0]["name"])