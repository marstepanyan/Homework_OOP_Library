class Student:
    def __init__(self, name):
        self._name = name
        self._books = {}

    def get_name(self):
        return self._name

    def get_books_to_be_borrowed(self):
        return self._books

    def borrow_book(self, books: dict, library):
        print(f'{self._name} wants to borrow this books: ', books)
        self._books = books
        library.borrow(self)
