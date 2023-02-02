from Library import Library
from Student import Student

Python_Lib = Library({'Effective Python': 5, 'Learning Python': 10, 'Object-Oriented Python': 2})
print(Python_Lib.get_books_in_library())

print()

std1 = Student('Harry')
std1.borrow_book({'Effective Python': 1, 'Learning Python': 5, 'Extreme C': 1}, Python_Lib)

print()

std2 = Student('Jane')
std2.borrow_book({'Object-Oriented Python': 3, 'Learning Python': 5}, Python_Lib)

print()

std3 = Student('Mary')
std3.borrow_book({'Learning Python': 3}, Python_Lib)

print()
print(Python_Lib.get_books_in_library())
