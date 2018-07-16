from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    read = Column(Boolean)

    @staticmethod
    def from_dict(book_dict):
        return Book(
            title = book_dict.get('title'),
            author = book_dict.get('author'),
            read =  book_dict.get('read'))
    
    def update_from_dict(self, book_dict):
        if 'title' in book_dict:
            self.title = book_dict.get('title')
        if 'author' in book_dict:
            self.author = book_dict.get('author')
        if 'read' in book_dict:
            self.read = book_dict.get('read')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'read': self.read
        }
