def fopen(fl, a):
    try:
        if a == "r":
            with open(fl, 'r') as file:
                content = file.read()
                return content
        if a == "l":
            with open(fl, 'r') as file:
                for line in file:
                    return line
    except FileNotFoundError:
        print("Файл не существует")
print(fopen("Example.txt", "r"))