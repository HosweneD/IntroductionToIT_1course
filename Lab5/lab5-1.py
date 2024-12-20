class ABc:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return self.title, self.author, self.year

book = ABc("Код. Тайный язык информатики", "Чарльз Петцольд", 2000)

print(book.get_info())