def wrtxt(a):
    txt = input()
    if a == "w":
        with open("user_input.txt", "w") as file:
            file.write(txt)
    if a == "a":
        with open("user_input.txt", "a") as file:
            file.write(txt)
print(wrtxt("a"))