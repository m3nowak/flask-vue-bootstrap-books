from datetime import datetime
import uuid

from flask import render_template, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from custom_flask import Flask
from local_store import BOOKS
from data_model import Book

app = Flask(__name__)

engine = create_engine("sqlite:///sqlite3_database.db")
Session = sessionmaker(bind=engine)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/api/tiem")
def api_time():
    return jsonify({"tiem":datetime.now().isoformat(sep=" ")})

@app.route('/api/books', methods=['GET'])
def all_books():
    session = Session()
    book_list = [book.to_dict() for book in session.query(Book).all()]
    session.close()
    return jsonify({
        'status': 'success',
        'books': book_list
    })

@app.route('/api/books', methods=['POST'])
def add_book():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    new_book = Book.from_dict(post_data)
    session = Session()
    session.add(new_book)
    session.commit()
    session.close()
    response_object['message'] = 'Book added!'
    return jsonify(response_object)

@app.route('/api/books/<book_id>', methods=['PUT'])
def single_book(book_id):
    response_object = {'status': 'success'}
    post_data = request.get_json()
    session = Session()
    book_to_edit = session.query(Book).filter(Book.id == book_id).one()
    book_to_edit.update_from_dict(post_data)
    session.commit()
    session.close()
    response_object['message'] = 'Book updated!'
    return jsonify(response_object)

@app.route('/api/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    response_object = {'status': 'success'}
    session = Session()
    session.query(Book).filter(Book.id == book_id).delete()
    session.commit()
    session.close()
    return jsonify(response_object)
