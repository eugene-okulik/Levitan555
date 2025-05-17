class Book:
    material = 'Бумага'
    text = True

    def __init__(self, name_book, author, count_page, isbn, reserve):
        self.name_book = name_book
        self.author = author
        self.count_page = count_page
        self.isbn = isbn
        self.reserve = reserve


class SchoolBook(Book):

    def __init__(self, name_book, author, count_page, isbn, reserve, subject, class_number, lesson):
        super().__init__(name_book, author, count_page, isbn, reserve)
        self.subject = subject
        self.class_number = class_number
        self.lesson = lesson


def print_title_book(book_num):
    print_book = (
        f'Название: {book_num.name_book}, Автор: {book_num.author},'
        f' Страниц: {book_num.count_page}, Материал: {book_num.material}'
    )
    if book_num.reserve is True:
        print(print_book, end="")
        print(', зарезервирована')
    else:
        print(print_book)


def print_title_schoolbook(schoolbook_num):
    print_schoolbook = (
        f'Название: {schoolbook_num.name_book}, Автор: {schoolbook_num.author},'
        f' Страниц: {schoolbook_num.count_page}, Предмет: {schoolbook_num.subject}, '
        f'Класс: {schoolbook_num.class_number}'
    )
    if schoolbook_num.reserve is True:
        print(print_schoolbook, end="")
        print(', зарезервирована')
    else:
        print(print_schoolbook)


book_1 = Book('Идиот', 'Достоевский', 500, '2-266-11156-6', False)
book_2 = Book('Болван', 'Толстой', 300, '2-266-11156-7', True)
book_3 = Book('Козел', 'Блок', 420, '2-266-11156-8', False)
book_4 = Book('Урод', 'Пушкин', 250, '2-266-11156-9', False)
book_5 = Book('Скотина', 'Лермонтов', 370, '2-266-11156-10', False)

schoolbook_1 = SchoolBook(
    'Алгебра', 'Иванов', 340, '2-266-11156-11', False,
    'Математика', 9, True
)
schoolbook_2 = SchoolBook(
    'Геометрия', 'Петров', 380, '2-266-11156-12', True,
    'Математика', 6, True
)
schoolbook_3 = SchoolBook(
    'Травоведение', 'Сидоров', 310, '2-266-11156-13', False,
    'Биология', 1, False
)

print_title_book(book_1)
print_title_book(book_2)
print_title_book(book_3)
print_title_book(book_4)
print_title_book(book_5)

print_title_schoolbook(schoolbook_1)
print_title_schoolbook(schoolbook_2)
print_title_schoolbook(schoolbook_3)
