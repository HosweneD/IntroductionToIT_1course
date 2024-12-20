class Employee:   #общие данные работников
    def __init__(self, name, eid):
        self.name = name
        self.eid = eid

    def get_info(self):
        return f"[{self.eid}] {self.name}"

class Manager(Employee):    #данные менеджера
    def __init__(self, name, eid, department):
        super().__init__(name, eid)
        self.department = department

    def manage_project(self):
        return f"[{self.eid}] {self.name} Управляет проектом в отделе {self.department}."

class Technician(Employee):     #данные технического специалиста
    def __init__(self, name, eid, specialization):
        super().__init__(name, eid)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"[{self.eid}] {self.specialization} {self.name} провёл техническое обслуживание."

class TechManager(Manager, Technician):      #данные технического менеджера
    def __init__(self, name, eid, department, specialization):
        Employee.__init__(self, name, eid)
        self.department = department
        self.specialization = specialization
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return "Список подчинённых пуст."
        t = ""
        for x in self.team:
            t += x.get_info() + "\n"
        return t
slave = Employee("Богдан", "1")
boss = Manager("Владимир","2","IT")
engineer = Technician("Дональд","3","Конструктор")
smart = TechManager("Ростислав","4","VPN","Проектировщик")

print(slave.get_info())
print(boss.get_info())
print(boss.manage_project())
print(engineer.perform_maintenance())
print(smart.manage_project())
print(smart.perform_maintenance())
smart.add_employee(slave)
smart.add_employee(engineer)
print("Команда тех.менеджера:")
print(smart.get_team_info())
