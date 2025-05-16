class Book:
    material = 'Бумага'
    text = True

    def __init__(self, name_book, author, count_page, isbn):
        self.name_book = name_book
        self.author = author
        self.count_page = count_page
        self.isbn = isbn


class SchoolBook(Book):

    def __init__(self, name_book, author, count_page, isbn, subject, class_number, lesson):
        super().__init__(name_book, author, count_page, isbn)
        self.subject = subject
        self.class_number = class_number
        self.lesson = lesson


def reserve_book(book_num, reserve):
    print_book = (
        f'Название: {book_num.name_book}, Автор: {book_num.author},'
        f' Страниц: {book_num.count_page}, Материал: {book_num.material}'
    )
    if reserve is True:
        print(print_book, end="")
        print(', зарезервирована')
    else:
        print(print_book)


def reserve_schoolbook(schoolbook_num, reserve):
    print_schoolbook = (
        f'Название: {schoolbook_num.name_book}, Автор: {schoolbook_num.author},'
        f' Страниц: {schoolbook_num.count_page}, Предмет: {schoolbook_num.subject}, Класс: {schoolbook_num.class_number}'
    )
    if reserve is True:
        print(print_schoolbook, end="")
        print(', зарезервирована')
    else:
        print(print_schoolbook)


book_1 = Book('Идиот', 'Достоевский', 500, '2-266-11156-6')
book_2 = Book('Болван', 'Толстой', 300, '2-266-11156-7')
book_3 = Book('Козел', 'Блок', 420, '2-266-11156-8')
book_4 = Book('Урод', 'Пушкин', 250, '2-266-11156-9')
book_5 = Book('Скотина', 'Лермонтов', 370, '2-266-11156-10')

schoolbook_1 = SchoolBook(
    'Алгебра', 'Иванов', 340, '2-266-11156-11',
    'Математика', 9, True
)
schoolbook_2 = SchoolBook(
    'Геометрия', 'Петров', 380, '2-266-11156-12',
    'Математика', 6, True
)
schoolbook_3 = SchoolBook(
    'Травоведение', 'Сидоров', 310, '2-266-11156-13',
    'Биология', 1, False
)

reserve_book(book_1, False)
reserve_book(book_2, True)
reserve_book(book_3, False)
reserve_book(book_4, False)
reserve_book(book_5, False)

reserve_schoolbook(schoolbook_1, False)
reserve_schoolbook(schoolbook_2, True)
reserve_schoolbook(schoolbook_3, False)
