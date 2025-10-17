# lib/book.py

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # title getter and setter
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    # page_count getter and setter
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            raise Exception("Page count must be an integer")
        self._page_count = value

    # method for reading
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    
        