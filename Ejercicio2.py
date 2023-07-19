class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        print(self.salary)

    def change_salary(self, new_salary):
        self.salary = new_salary

if __name__ == '__main__':

    Javier = Employee("Javier", 28000)
    Javier.get_salary()
    Javier.change_salary(34000)
    Javier.get_salary()

