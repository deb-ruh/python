class Employee:
    def __init__(self, first, last, employee_number, no_years_employed, base_pay = 0, allowance = 0, hourlyrate = 200):
        self.first = first
        self.last = last
        self.employee_number = employee_number
        self.no_years_employed = no_years_employed
        self.base_pay = base_pay
        self.allowance = allowance
        self.hourlyrate = hourlyrate
    def introduce(self):
        print("Hello! My name is",self.first+"!")

    def updateEmployee_Name(self):
        self.first = input("Enter new first name: ")
        self.last = input("Enter new last name: ")

    def compute_salary(self, n_hours):
        return(n_hours*self.hourlyrate)
    
    def employee_info(self):
        info = {
            "Name ": f"{self.first} {self.last}",
            "Employee Number": self.employee_number,
            "Years Employed": self.no_years_employed,
            "Base Pay": self.base_pay,
            "Hourly Rate": self.hourlyrate
        }
        for key, value in info.items():
            print(f"{key}: {value}")

        return info
class Regular(Employee):
    def __init__(self, first, last, employee_number, no_years_employed, hourlyrate = 250, base_pay = 28000, allowance = 2000):
        super().__init__(first, last, employee_number, no_years_employed, hourlyrate)
        self.base_pay = base_pay
        self.allowance = allowance

class Manager(Regular):
    def __init__(self, first, last, employee_number, no_years_employed, hourlyrate = 500, base_pay = 35000, allowance = 5000):
        super().__init__(first, last, employee_number, no_years_employed, hourlyrate, base_pay, allowance)

first = input("Enter first name: ")
last = input("Enter last name: ")
employee_number = input("Enter employee number: ")
no_years_employed = int(input("Enter number of years employed: "))
employment_status = int(input("What is your employment status? [1 - Part-time, 2 - Regular, 3 - Manager]"))
if employment_status == 1:
    employee1 = Employee(first, last, employee_number, no_years_employed)
if employment_status == 2:
    employee1 = Regular(first, last, employee_number, no_years_employed)
if employment_status == 3:
    employee1 = Manager(first, last, employee_number, no_years_employed)

print("This program performs the following actions:")
print("Press 1: Change Name")
print("Press 2: Update Base Pay")
print("Press 3: Update Hourly Rate")
print("Press 4: Compute Monthly Salary")
print("Press 5: Check Employee Information")
option = int(input("Enter course of action: "))
if option == 1:
    employee1.updateEmployee_Name()
    info = employee1.employee_info()
    
if option == 2:
    new_base_pay = float(input("Enter new base pay: "))
    employee1.base_pay = new_base_pay
    info = employee1.employee_info()
    
if option == 3:
    new_hourly_rate = float(input("Enter new hourly rate: "))
    employee1.hourlyrate = new_hourly_rate
    info = employee1.employee_info()

if option == 4:
    n_hours = float(input("Enter number of hours worked: "))
    monthly_salary = employee1.compute_salary(n_hours)
    monthly_salary = employee1.base_pay + employee1.allowance
    print("Monthly Salary is:", monthly_salary)
    info = employee1.employee_info()
if option == 5:
    employee1.employee_info()