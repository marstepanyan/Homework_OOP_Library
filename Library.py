class Library:
    def __init__(self, books: dict):
        self._books = books

    def get_books_in_library(self):
        print('Books in library: ', end='')
        return self._books

    def borrow(self, student):
        books_to_be_borrowed = student.get_books_to_be_borrowed()
        for book in books_to_be_borrowed:
            if book in self._books:
                if self._books[book] >= 1:
                    if self._books[book] - books_to_be_borrowed[book] >= 0:
                        self._books[book] -= books_to_be_borrowed[book]
                    else:
                        print(f'Library does not have that many {book} books')
                else:
                    print(f'{book} book is out of stock')
            else:
                print(f'Library never had {book} book')
