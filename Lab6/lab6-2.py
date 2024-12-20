class Vehicle:   #класс "транспортное средство"
    def __init__(self, make, model):
        self.make = make    #марка
        self.model = model   #модель

    def get_info(self):     #информация о транспортном средстве
        return self.make, self.model

class Car(Vehicle):  #класс "автомобиль" с наследованием
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type   #тип топлива

    def get_info(self):  #дополненная информация о ТС
        full_info = super().get_info()
        return full_info, self.fuel_type

car = Car("Lada", "Vesta", "Kerosene")
print(car.get_info())
