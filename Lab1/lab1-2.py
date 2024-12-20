n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
if n1 > n2:
    print("Большее число:", n1)
elif n1 < n2:
    print("Большее число:", n2)
elif n1 == n2:
    print("Числа равны:")
    print(n1, "=", n2)
