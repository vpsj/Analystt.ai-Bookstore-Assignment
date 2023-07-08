from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="vpsjdon",
    password="onlinebookstore",
    database="bookstore"
)


@app.route('/books', methods=['GET'])
def get_books():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    books_list = []

    for book in books:
        book_data = {
            'id': book[0],
            'title': book[1],
            'author': book[2],
            'description': book[3],
            'cover_image': book[4],
            'price': book[5],
            'rating': book[6],
            'category': book[7]
        }
        books_list.append(book_data)

    return jsonify(books_list)

@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s OR category LIKE %s", (f'%{query}%', f'%{query}%', f'%{query}%'))
    books = cursor.fetchall()
    search_results = []

    for book in books:
        book_data = {
            'id': book[0],
            'title': book[1],
            'author': book[2],
            'description': book[3],
            'cover_image': book[4],
            'price': book[5],
            'rating': book[6],
            'category': book[7]
        }
        search_results.append(book_data)

    return jsonify(search_results)

if __name__ == '__main__':
    app.run()
