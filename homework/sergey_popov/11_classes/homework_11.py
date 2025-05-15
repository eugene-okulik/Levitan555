
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


def reserve_book(reserve):
    if reserve is True:
        print(', зарезервирована')
    else:
        print('')


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

print(
    f'Название: {book_1.name_book}, Автор: {book_1.author},'
    f' Страниц: {book_1.count_page}, Материал: {Book.material}', end=""
)
reserve_book(False)
print(
    f'Название: {book_2.name_book}, Автор: {book_2.author},'
    f' Страниц: {book_2.count_page}, Материал: {Book.material}', end=""
)
reserve_book(True)
print(
    f'Название: {book_3.name_book}, Автор: {book_3.author},'
    f' Страниц: {book_3.count_page}, Материал: {Book.material}', end=""
)
reserve_book(False)
print(
    f'Название: {book_4.name_book}, Автор: {book_4.author},'
    f' Страниц: {book_4.count_page}, Материал: {Book.material}', end=""
)
reserve_book(False)
print(
    f'Название: {book_5.name_book}, Автор: {book_5.author},'
    f' Страниц: {book_5.count_page}, Материал: {Book.material}', end=""
)
reserve_book(False)
print()
print(
    f'Название: {schoolbook_1.name_book}, Автор: {schoolbook_1.author},'
    f' Страниц: {schoolbook_1.count_page}, Предмет: {schoolbook_1.subject}, Класс: {schoolbook_1.class_number}', end=""
)
reserve_book(False)
print(
    f'Название: {schoolbook_2.name_book}, Автор: {schoolbook_2.author},'
    f' Страниц: {schoolbook_2.count_page}, Предмет: {schoolbook_2.subject}, Класс: {schoolbook_2.class_number}', end=""
)
reserve_book(False)
print(
    f'Название: {schoolbook_3.name_book}, Автор: {schoolbook_3.author},'
    f' Страниц: {schoolbook_3.count_page}, Предмет: {schoolbook_3.subject}, Класс: {schoolbook_2.class_number}', end=""
)
reserve_book(True)
