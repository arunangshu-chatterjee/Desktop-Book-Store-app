# Desktop-Book-Store-app
A desktop application written in Python to store and manage collection of books based on tkinter and SQLite


#### A program that stores the following information on books:
Title

Year

Author

ISBN


#### User can:
View all records

Search an entry

Add an entry

Update an entry

Delete an entry

Close the program


#### Files in the repository:
frontend.py - To design the interface of the application

backend.py - To create, manage and interact with the database

books.db - sample database file for the books. If books.db doesnot exist in the directory from where app runs, it creates the db.

BookStore App.exe - The application executable file. Can be downloaded and used directly.


#### To create the executable file of this application,
pip install pyinstaller

From the folder containing frontend.py, open a command window and run the below command:

pyinstaller --onefile --windowed frontend.py
