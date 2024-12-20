class UserAccount:  #класс "аккаунт"
    def __init__(self, username, email, password):
        self.username = username    #имя пользователя
        self.email = email  #электронная почта
        self.__password = password    #пароль, __ это приватный атрибут

    def set_password(self, new_password):   #смена пароля
        self.__password = new_password

    def check_password(self, password):    #проверка соответствия пароля
        if password == self.__password:
            return True
        else:
            return False

User = UserAccount("Nikita2008", "Nekit@mtuci.ru", "12345")  #пользователь

User.set_password("JxLsHI*213?")
print(User.check_password("JxLsHI*213?"))
