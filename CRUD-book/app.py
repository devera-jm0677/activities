from flask import Flask, render_template, request, jsonify
import pymysql
from contextlib import closing

app = Flask(__name__)

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '',
    'db': 'bookdb2'
}

def get_db_connection():
    """Create and return a database connection"""
    return pymysql.connect(**DB_CONFIG)

def init_db():
    """Initialize database with sample data if empty"""
    try:
        with closing(get_db_connection()) as conn:
            with closing(conn.cursor()) as cursor:
                # CHECK TABLE 
                cursor.execute("SELECT COUNT(*) FROM book")
                count = cursor.fetchone()[0]
                
                if count == 0:
                    # SAMPLE DATA
                    sample_books = [
                        (1001, 'James (Pulitzer Prize Winner): A Novel', 'Doubleday', 'Fiction'),
                        (1002, 'Light and Color', 'Wiley', 'Art & Painting'),
                        (1003, 'The Art of War', 'Penguin Books', 'History')
                    ]
                    
                    cursor.executemany(
                        "INSERT INTO book (isbn, title, publisher, category) VALUES (%s, %s, %s, %s)",
                        sample_books
                    )
                    conn.commit()
                    print("Sample data inserted successfully")
    except pymysql.Error as e:
        print(f"Database initialization error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/books', methods=['GET'])
def get_books():
    try:
        with closing(get_db_connection()) as conn:
            with closing(conn.cursor(pymysql.cursors.DictCursor)) as cursor:
                cursor.execute("SELECT isbn, title, publisher, category FROM book ORDER BY isbn")
                books = cursor.fetchall()
                return jsonify(books)
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/books', methods=['POST'])
def add_book():
    try:
        data = request.json
        
        with closing(get_db_connection()) as conn:
            with closing(conn.cursor()) as cursor:
                # CHECK EXISTING ISBN 
                cursor.execute("SELECT isbn FROM book WHERE isbn = %s", (data['isbn'],))
                if cursor.fetchone():
                    return jsonify({'error': 'ISBN already exists'}), 400
                
                # INSERT NEW BOOK
                cursor.execute(
                    "INSERT INTO book (isbn, title, publisher, category) VALUES (%s, %s, %s, %s)",
                    (data['isbn'], data['title'], data['publisher'], data['category'])
                )
                conn.commit()
                
                return jsonify({
                    'isbn': data['isbn'],
                    'title': data['title'],
                    'publisher': data['publisher'],
                    'category': data['category']
                }), 201
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/books/<int:isbn>', methods=['PUT'])
def update_book(isbn):
    try:
        data = request.json
        
        with closing(get_db_connection()) as conn:
            with closing(conn.cursor()) as cursor:
                # CHECK EXISTING BOOK
                cursor.execute("SELECT isbn FROM book WHERE isbn = %s", (isbn,))
                if not cursor.fetchone():
                    return jsonify({'error': 'Book not found'}), 404
                
                # UPDATE BOOK
                cursor.execute(
                    "UPDATE book SET title = %s, publisher = %s, category = %s WHERE isbn = %s",
                    (data['title'], data['publisher'], data['category'], isbn)
                )
                conn.commit()
                
                return jsonify({
                    'isbn': isbn,
                    'title': data['title'],
                    'publisher': data['publisher'],
                    'category': data['category']
                })
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    try:
        with closing(get_db_connection()) as conn:
            with closing(conn.cursor()) as cursor:
                # CHECK EXISTING BOOK
                cursor.execute("SELECT isbn FROM book WHERE isbn = %s", (isbn,))
                if not cursor.fetchone():
                    return jsonify({'error': 'Book not found'}), 404
                
                # DELETE BOOK
                cursor.execute("DELETE FROM book WHERE isbn = %s", (isbn,))
                conn.commit()
                
                return jsonify({'message': 'Book deleted successfully'})
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
