# employee1 = {'first_name': 'Alice', 'last_name': 'Smith', 'salary':85000}
# employee2 = {'first_name': 'Bob', 'last_name': 'Jones', 'salary':74000}
# employee3 = {'first_name': 'Charlie', 'last_name': 'Doe', 'salary':49000}

# #later..
# employee4 = {'first_name': 'Charlie', 'last_name': 'Doe', 'salary':49000}

# employees = [employee1, employee2, employee3, employee4]

# for employee in employees:
#     print(employee['salary'])
#     # print(f"First name: {employee['first_name']}, Last Name: {employee['last_name']}, Salary:{employee['salary']}")
class Department():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
    def remove_employee(self, employee):
        self.employees.remove(employee)
    def transfer_employee(self, other_department, employee_id):

        for employee in self.employee:
            if employee.employee_id == employee_id

class Employee():
    def __init__(self, first_name, last_name, department, salary, employee_id, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name =last_name
        # self.full_name = first_name + last_name # or f"{first_name}{last_name}"
        self.salary = int(salary)
        self.department = department
        self.department.add_employee(self)
        self.employee_id = employee_id
        # def get_full_name(self):
        #     return f"{self.first_name}{self.last_name}"

    def get_full_name(self):
        if self.middle_name == None:
            return f"{self.first_name}{self.last_name}"
        else:
            return f"{self.first_name}{self.middle_name}{self.last_name}"

    def set_salary(self, new_salary):
        if isinstance(new_salary,int) or isinstance(new_salary, float):

            if new_salary < 40000 or new_salary >200000:
                return  None
            else:
                self.salary = int(new_salary)
        else:
            return None
department_a = Department('Engineering', '202C')
department_b = Department('Sales', '304B')
department_c = Department('Facilities', '099A')
departments = [department_a, department_b, department_c]


employee1 = Employee('Alice', 'Jones',87000,department_a, middle_name = 'Anne')
employee2 = Employee('Brad', 'Smith',department_c ,61000)
employee3 = Employee('Charlie', 'Doe',79000, department_b, middle_name = 'Zachary')

employees = [employee1, employee2, employee3]
for employee in employees:
    employee.set_salary(employee.salary*1.1)
    print(f"Full name:{employee.first_name}{employee.middle_name}{employee.last_name} Salary:{employee.salary}")


for department in departments:
    print(department.name)
    for employee in department.employees:
        print(f"Full name:{employee.get_full_name()} Salary:")