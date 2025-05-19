class Author:
    def __init__(self, name):
        self.name = name
    
    def contracts(self):
        # Return all contracts that belong to this author
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        # Return unique books from contracts of this author
        return list({contract.book for contract in self.contracts()})
    
    def sign_contract(self, book, date, royalties):
        # Create a contract (and add to Contract.all)
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        # Sum all royalties for this author’s contracts
        return sum(contract.royalties for contract in self.contracts())

        


class Book:
    def __init__(self, title):
        self.title = title
    
    def contracts(self):
        # Return all contracts that belong to this book
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        # Return unique authors from contracts of this book
        return list({contract.author for contract in self.contracts()})



class Contract:
    all = []  # class attribute to hold all contracts
    
    def __init__(self, author, book, date, royalties):
        # Validate types
        if not isinstance(author, Author):
            raise Exception("author must be an Author")
        if not isinstance(book, Book):
            raise Exception("book must be a Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date_str):
        # Return list of contracts matching date, sorted by date
        filtered = [c for c in cls.all if c.date == date_str]
        # Assuming date format 'MM/DD/YYYY', string sort works fine here
        return sorted(filtered, key=lambda c: c.date)
