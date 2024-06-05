class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.set_author(author)
        self.set_book(book)
        self.set_date(date)
        self.set_royalties(royalties)
        Contract.all.append(self)

    def get_author(self):
        return self._author
    
    def set_author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value
    author = property(get_author, set_author)


    def get_book(self):
        return self._book
    
    def set_book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of Book")
        self._book = value
    book = property(get_book, set_book)


    def get_date(self):
        return self._date
    
    def set_date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value
    date = property(get_date, set_date)

    def get_royalties(self):
        return self._royalties
    
    def set_royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer")
        self._royalties = value

    royalties = property(get_royalties, set_royalties)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.get_date() == date]
