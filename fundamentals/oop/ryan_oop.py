class Department():

    departments = []

    def __init__(self, name, location):
        # name: department name
        # location: room number
        self.name = name
        self.location = location
        self.employees = []
        Department.departments.append(self)

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def transfer_employee(self, other_department, employee_id):

        for employee in self.employees:
            if employee.employee_id == employee_id:
                transfer_employee = employee
                self.remove_employee(transfer_employee)
                other_department.add_employee(transfer_employee)

    @classmethod
    def get_all_departments(cls):
        return cls.departments

    @classmethod
    def print_all_department_info(cls):

        for department in cls.departments:
            print(department.name)
            for employee in department.employees:
                print(f"Full name: {employee.get_full_name()} Salary: {employee.salary}")
            print('-' * 80)


class Employee():

    def __init__(self, first_name, last_name, salary, department, employee_id, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = int(salary)
        self.department = department
        # employee ID - first initial/last initial/six digits
        self.employee_id = employee_id
        # self.department.employees.append(self) - bad
        self.department.add_employee(self)


    def get_full_name(self):
        if self.middle_name == None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

    def set_salary(self, new_salary):
        if isinstance(new_salary, int) or isinstance(new_salary, float):

            if new_salary < 40000 or new_salary > 200000:
                return None
            else:
                self.salary = int(new_salary)

        else:
            return None

department_a = Department('Engineering', '202C')
department_b = Department('Sales', '304B')
department_c = Department('Facilities', '099A')

departments = [department_a, department_b, department_c]

employee1 = Employee('Alice', 'Jones', 87000, department_a, 'AJ457812', middle_name ='Anne')
employee2 = Employee('Brad', 'Smith', 61000, department_b, 'BS125876')
employee3 = Employee('Charlie', 'Doe', 79000, department_b, 'CD136985', middle_name = 'Zachary')
employee4 = Employee('Dean', 'Wallace', 58000, department_a, 'DW358746')
employee5 = Employee('Earl', 'Adams', 61000, department_c, 'EA136587')

employees = [employee1, employee2, employee3, employee4, employee5]

# for employee in employees:
#     print(f"Full name: {employee.get_full_name()} Salary: {employee.salary} Department: {employee.department.name}")

# for department in Department.get_all_departments():
#     print(department.name)
#     for employee in department.employees:
#         print(f"Full name: {employee.get_full_name()} Salary: {employee.salary}")
#     print('-' * 80)

Department.print_all_department_info()

department_b.transfer_employee(department_a, 'BS125876')
employee2.set_salary(employee2.salary * 1.2)

Department.print_all_department_info()

# for department in Department.get_all_departments():
#     print(department.name)
#     for employee in department.employees:
#         print(f"Full name: {employee.get_full_name()} Salary: {employee.salary}")
#     print('-' * 80)

# Department A Name
# Department A Employee 1
# Department A Employee 2 ...
# Department B Name ...