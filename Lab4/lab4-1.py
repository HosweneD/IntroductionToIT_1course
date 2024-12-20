import math, datetime
from datetime import date, time
f = datetime.datetime.now()
dtd = date.today()
tmd = f.time()
a = float(input("Для подсчёта квадратного корня, введите число: "))
print("√", a, "=", math.sqrt(a))
print("Дата:", dtd, "|" , "время:", tmd)
