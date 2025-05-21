class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display(self):
        return f"Name: {self.name}, Salary: {self.salary}"
        
class SalesEmployee(Employee):
    def display(self, id):
        print(self.name, self.salary, id)
        
person = Employee("John", 50000)
print(person.display())  # Output: Name: John, Salary: 50000

person1 = SalesEmployee("Jane", 60000)
print(person1.display(101))  # Output: Name: Jane, Salary: 60000, ID: 101