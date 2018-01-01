import sqlite3

def connect():                                              # Connect to the books database or create if does not exist
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
	conn.commit()
	conn.close()

def insert(title, author, year, isbn):                      # Insert book details in to the DB based on book details
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
	conn.commit()
	conn.close()

def search(title = "", author = "", year = "", isbn = ""):  # Search book details in the DB based on certain inputs
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR ISBN = ?", (title, author, year, isbn))
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(id):                                             # Delete current book detail from the DB based on id
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM book WHERE item = ?",(id,))
	conn.commit()
	conn.close()

def update(id, title, author, year, isbn):                  # Update current book details in the DB based on one or more parameters
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("UPDATE book SET title = ?, author = ?, year = ?, ISBN = ? WHERE id = ?", (title, author, year, isbn, id))
	conn.commit()
	conn.close()

def view():                                                 # View current book details from the DB
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM book")
	rows = cur.fetchall()
	conn.close()
	return rows

connect()                                                   # Establishes a connection and creates books.db if not exists.