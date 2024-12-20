class Circle:
    def __init__(self, radius):  # задаёт значение для класса
        self.radius = radius  # self нужен чтобы обращаться к свойствам внутри класса

    def get_radius(self):  # возвращает значение радиуса
        return f"Значение радиуса: {self.radius} см"

    def set_radius(self, new_radius):  # меняет старое значение радиуса на новое
        self.radius = new_radius


krug = Circle(1)
a = float(input("Какой должен быть радиус круга? Ответ: "))
krug.set_radius(a)
print(krug.get_radius())
