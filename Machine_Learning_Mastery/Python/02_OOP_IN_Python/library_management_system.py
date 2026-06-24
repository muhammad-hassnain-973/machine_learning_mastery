#Library Management system using oop in python

class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.__isbn=isbn
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}"
    
book=Book("Gift of Fire","Amitav Ghosh","978-0143039433")
print(book.get_info())

