from abc import ABC, abstractmethod

class OrganizationComponent(ABC):

    @abstractmethod
    def display(self, indent=0):
        pass

    @abstractmethod
    def get_budget(self):
        pass

    @abstractmethod
    def get_employee_count(self):
        pass

class Employee(OrganizationComponent):
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display(self, indent=0):
        print(" " * indent + f"{self.name} ({self.position}) - {self.salary}")

    def get_budget(self):
        return self.salary

    def get_employee_count(self):
        return 1

    def change_salary(self, new_salary):
        self.salary = new_salary

class Contractor(Employee):
    def get_budget(self):
        return 0

class Department(OrganizationComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        if component not in self.children:
            self.children.append(component)

    def remove(self, component):
        if component in self.children:
            self.children.remove(component)

    def display(self, indent=0):
        print(" " * indent + f"Отдел: {self.name}")
        for child in self.children:
            child.display(indent + 2)

    def get_budget(self):
        return sum(child.get_budget() for child in self.children)

    def get_employee_count(self):
        return sum(child.get_employee_count() for child in self.children)

    def find_employee(self, name):
        for child in self.children:
            if isinstance(child, Employee) and child.name == name:
                return child
            elif isinstance(child, Department):
                found = child.find_employee(name)
                if found:
                    return found
        return None

    def list_all_employees(self):
        result = []
        for child in self.children:
            if isinstance(child, Employee):
                result.append(child.name)
            elif isinstance(child, Department):
                result.extend(child.list_all_employees())
        return result

if __name__ == "__main__":
    emp1 = Employee("Ali", "Manager", 1000)
    emp2 = Employee("Dana", "Developer", 800)
    emp3 = Contractor("Temp", "Freelancer", 500)

    dept1 = Department("IT")
    dept2 = Department("HR")
    company = Department("Company")

    dept1.add(emp1)
    dept1.add(emp3)
    dept2.add(emp2)

    company.add(dept1)
    company.add(dept2)

    company.display()

    print("\nБюджет:", company.get_budget())
    print("Сотрудников:", company.get_employee_count())

    found = company.find_employee("Dana")
    if found:
        print("\nНайден:", found.name)

    print("\nВсе сотрудники:", company.list_all_employees())
