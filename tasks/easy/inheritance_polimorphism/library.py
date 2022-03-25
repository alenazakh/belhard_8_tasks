"""
Определить класс Person:

- атрибут fullname - ФИО (тип str)
- атрибут phone - номер телефона (тип str)
- магический метод __init__, который принимает fullname и phone

Описать класс LibraryReader, который наследуется от Person:

- атрибут uid - номер читательского билета (тип int)
- атрибут books - список книг (тип set)
- магический метод __init__, который принимает fullname, phone, uid, а books
  заполняет пустым множеством
- метод take_books(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. взял(а)
  книги: Приключения, Словарь, Энциклопедия", если было взято до 3 книг
  включительно. Если было взято больше книг, то возвращает строку: "Петров В.В.
  взял(а) 4 книги".
- метод return_book(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. вернул(а)
  книги: Приключения, Словарь, Энциклопедия", если было возвращено до 3 книг
  включительно. Если было возвращено больше книг, то возвращает строку:
  "Петров В.В. вернул(а) 4 книги". Если какой-то книги нет, то бросить исключение
  ValueError с сообщением "Петров В. В. не брал: Рассказы", при этом книги не
  должны быть удалены

Названия книг в сообщениях должны быть отсортированы по алфавиту.
"""


class Person:
    def __init__(self, fullname, phone):
        self.fullname = fullname
        self.phone = phone


class LibraryReader(Person):
    uid: int
    books: set

    def __init__(self, fullname, phone, uid, books=None):
        super().__init__(fullname, phone)
        if books is None:
            books = set()
        self.uid = uid
        self.books = books

    def take_books(self, *args):
        self.books = self.books.union(args)    # set убирает автоматов повторы и выводит в сортированном порядке
        if len(args) <= 3:
            args = list(args)
            args.sort()
            return(f"{self.fullname} взял(а) книги: {', '.join(args)}")
        else:
            return(f"{self.fullname} взял(а) {len(args)} книги")

    def return_book(self, *args):
        args = set(args)    # set убирает автоматов повторы и выводит в сортированном порядке
        if self.books.issuperset(args):
            self.books = self.books.difference(args)
            if len(args) <= 3:
                lst = list(args)
                lst.sort()
                return(f"{self.fullname} вернул(а) книги: {', '.join(lst)}")
            else:
                return(f"{self.fullname} вернул(а) {len(args)} книги")
        else:
            raise ValueError(f"{self.fullname} не брал(а): {args.difference(self.books)}")


reader5555 = LibraryReader('Ivanova Helen', '+375296555554', 5555)
reader5557 = LibraryReader('Petrov Alex', '+375296555554', 5557)
print(reader5555.take_books('Сто лет одиночества', 'Унесенные ветром', 'Алхимик'))
print(reader5555.take_books('Приключения Арбузика и Бебешки', "Economics"))
print(reader5555.return_book('Приключения Арбузика и Бебешки', 'Алхимик'))
print(reader5555.books)
