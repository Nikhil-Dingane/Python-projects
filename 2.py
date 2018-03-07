class Book():
    def getBookType(self):
        print("Book")


class TextBook(Book):
    def getBookType(self):
        print("Text")

class NoteBook(Book):
    def getBookType(self):
        print("Note")

b = TextBook()
b.getBookType()
b = NoteBook()
b.getBookType()
