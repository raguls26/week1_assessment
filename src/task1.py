import csv

class InvalidSalaryError(Exception):
    pass

#Bonus function with *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    total_extra = sum(extras)
    result = (salary * rate) + total_extra
    if 'cap' in options and result > options['cap']:
        return options['cap']
    return result

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = float(salary)

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Team Size: {self.team_size}"

# Custom Exception Demonstration
try:
    emp_err = Employee("Test", -500)
except InvalidSalaryError as e:
    print(f"Error: {e}")
finally:
    print("Transaction finished")

#  Data Processing with Comprehensions, Map, Lambda, and Filter
data = [
    {"id": 1, "name": "Arun", "department": "Sales", "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT", "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT", "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance", "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales", "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT", "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR", "salary": 48000, "city": "Mumbai"}
]

# List comprehension for salaries above 50000
above_50k = [emp["name"] for emp in data if emp["salary"] > 50000]
print("Above 50000:", above_50k)

# Map + Lambda to add 10% raise
raised_salaries = list(map(lambda emp: {**emp, "salary": emp["salary"] * 1.1}, data))

# Filter to keep Chennai employees
chennai_emps = list(filter(lambda emp: emp["city"] == "Chennai", data))
chennai_names = [emp["name"] for emp in chennai_emps]
print("Chennai:", chennai_names)

# Control Flow (for loop with continue and break)
print("\nLoop execution:")
sample_salaries = [30000, 0, 45000, 60000, 90000, 52000]
for sal in sample_salaries:
    if sal == 0:
        continue 
    if sal > 85000:
        print(f"Stopping at salary above 85000: {sal}")
        break  
    print(f"Processing salary: {sal}")