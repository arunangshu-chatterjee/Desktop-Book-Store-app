"""
A program that stores the following information on books:
Title, Year
Author, ISBN

User can:
View all records
Search an entry
Add an entry
Update an entry
Delete an entry
Close the program

To create the executable file of this application,
pip install pyinstaller
From the folder containing frontend.py, open a command window and run the below command:
pyinstaller --onefile --windowed frontend.py

"""

from tkinter import *

import backend

def clear_entries():                  # Function to clear the entry widgets
	e1.delete(0, END)
	e2.delete(0, END)
	e3.delete(0, END)
	e4.delete(0, END)

def get_selected_row(event):          # Function to populate the selected row on the entry widgets
	if list1.size() != 0:
		global selected_tuple
		index = list1.curselection()[0]
		selected_tuple = list1.get(index)
		clear_entries()
		e1.insert(END, selected_tuple[1])
		e2.insert(END, selected_tuple[2])
		e3.insert(END, selected_tuple[3])
		e4.insert(END, selected_tuple[4])
	else:
		pass

def view_command():                   # Function to view the database entries on the Listbox
	list1.delete(0, END)
	for row in backend.view():
		list1.insert(END, row)

def search_command():                 # Function to search a book in the database based on the parameters entered in entry widgets
	list1.delete(0, END)
	for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
		list1.insert(END, row)

def insert_command():                 # Function to insert a new book record in the database
	list1.delete(0, END)
	backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():                 # Function to delete a book record from the database based on the selected entry in the Listbox
	backend.delete(selected_tuple[0])
	clear_entries()
	view_command()

def update_command():                 # Function to update a book record in the database based on the parameters entered in entry widgets
	backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	view_command()

window = Tk()                                  # Opens a window

window.wm_title("Book Store")                  # Sets the title of the window

l1 = Label(window, text = "Title")             # Creates a label for Title
l1.grid(row = 0, column = 0)                   # Sets position of the label

l2 = Label(window, text = "Year")              # Creates a label for Year
l2.grid(row = 1, column = 0)                   # Sets position of the label

l3 = Label(window, text = "Author")            # Creates a label for Author
l3.grid(row = 0, column = 2)                   # Sets position of the label

l4 = Label(window, text = "ISBN")              # Creates a label for ISBN
l4.grid(row = 1, column = 2)                   # Sets position of the label

title_text = StringVar()                       # Initializes a variable of StringVar() type to store data from Entry widget
e1 = Entry(window,textvariable = title_text)   # Creates an entry widget for capturing title of the book
e1.grid(row = 0, column = 1)                   # Sets position of the entry widget

year_text = StringVar()                        # Initializes a variable of StringVar() type to store data from Entry widget
e2 = Entry(window,textvariable = year_text)    # Creates an entry widget for capturing year of publication of the book
e2.grid(row = 1, column = 1)                   # Sets position of the entry widget

author_text = StringVar()                      # Initializes a variable of StringVar() type to store data from Entry widget
e3 = Entry(window,textvariable = author_text)  # Creates an entry widget for capturing the author name of the book
e3.grid(row = 0, column = 3)                   # Sets position of the entry widget

isbn_text = StringVar()                        # Initializes a variable of StringVar() type to store data from Entry widget
e4 = Entry(window,textvariable = isbn_text)    # Creates an entry widget for capturing the isbn details of the book
e4.grid(row = 1, column = 3)                   # Sets position of the entry widget

list1 = Listbox(window, height = 6, width = 35)               # Creates a Listbox for displaying the book records
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)  # Sets position of the Listbox

sb1 = Scrollbar(window)                                       # Creates a vertical scrollbar for the Listbox
sb1.grid(row = 2, column = 2, rowspan = 6, ipady = 30)        # Sets position of the scrollbar
list1.configure(yscrollcommand = sb1.set)                     # Configuring the Listbox for the horizontal scrollbar
sb1.configure(command = list1.yview)                          # Configuring the scrollbar for the Listbox
list1.bind('<<ListboxSelect>>', get_selected_row)             # Binding the Listbox to work with the get_selected_row function

sb2 = Scrollbar(window, orient = 'horizontal')                # Creates a horizontal scrollbar for the Listbox
sb2.grid(row = 7, column = 0, columnspan = 2, ipadx = 70)     # Sets position of the scrollbar
list1.configure(xscrollcommand = sb2.set)                     # Configuring the Listbox for the horizontal scrollbar
sb2.configure(command = list1.xview)                          # Configuring the scrollbar for the Listbox
list1.bind('<<ListboxSelect>>', get_selected_row)             # Binding the Listbox to work with the get_selected_row function


b1 = Button(window, text = "View All", width = 12, command = view_command)          # Creates a button for the viewing all book records
b1.grid(row = 2, column = 3)                                                        # Sets position of the button

b2 = Button(window, text = "Search Entry", width = 12, command = search_command)    # Creates a button for searching book records
b2.grid(row = 3, column = 3)                                                        # Sets position of the button

b3 = Button(window, text = "Add Entry", width = 12, command = insert_command)       # Creates a button for inserting new book records
b3.grid(row = 4, column = 3)                                                        # Sets position of the button

b4 = Button(window, text = "Update Selected", width = 12, command = update_command) # Creates a button for updating existing book records
b4.grid(row = 5, column = 3)                                                        # Sets position of the button

b5 = Button(window, text = "Delete Selected", width = 12, command = delete_command) # Creates a button for deleting existing book records
b5.grid(row = 6, column = 3)                                                        # Sets position of the button

b6 = Button(window, text = "Close", width = 12, command = window.destroy)           # Creates a button for closing the application
b6.grid(row = 7, column = 3)                                                        # Sets position of the button


window.mainloop()
