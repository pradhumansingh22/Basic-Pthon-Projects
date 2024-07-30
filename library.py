class Library:
    no_of_books = 0
    def __init__(self, book_name):
        if self.isPresent(book_name):
            print("Book already exists!")
        else:
            self.f =  open("library.txt", 'a')
            self.f.write(f"{book_name}\n")
            self.f.close()
    
    def isPresent(self, book_name):
         with open("library.txt", 'r') as b:
              while True:
                    self.line = b.readline()
                    if self.line.strip() == book_name.strip():
                        return True
                    if not self.line:
                        return False

    @classmethod
    def showBooks(cls):
        with open("library.txt", 'r') as cls.books_available:
                while True:
                    line = cls.books_available.readline()
                    if not line:
                         break
                    cls.no_of_books += 1
                    print(line)
                    
    
#b1 = Library("Ikigai")
#b2 = Library("How do you live?")
b3 = Library("Ikigai")
Library.showBooks()
print(Library.no_of_books)
