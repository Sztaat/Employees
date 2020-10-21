from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Employees database')
root.geometry("400x400")


conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE IF NOT EXISTS employees(Name text, Surname text, Role text, Shift text)""")

# Add employee
def addemp():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Input record
    c.execute("INSERT INTO Employees VALUES (:name, :surname, :role, :shift)", {
        'name': name.get(),
        'surname': surname.get(),
        'role': role.get(),
        'shift': shift.get()
        })


    # Save changes
    conn.commit()
    # Close connection
    conn.close()

    # Clearing boxes
    name.delete(0, END)
    surname.delete(0, END)
    role.delete(0, END)
    shift.delete(0, END)

# List records
def listemp():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM Employees")
    records = c.fetchall()

    print_rec = ''
    for rec in records:
        print_rec += str(rec[4]) + ".  " + str(rec[0]) + "  " + str (rec[1]) + "  " + str(rec[2]) + "  " + str(rec[3]) +"\n"

    rec_label = Label(root, bg="white", justify=LEFT, text=print_rec)
    rec_label.grid(row=7, column=0, columnspan=2)
        

    # Save changes
    conn.commit()
    # Close connection
    conn.close()

# Record boxes
name = Entry(root, width=30)
name.grid(row=1, column=1,)
surname = Entry(root, width=30)
surname.grid(row=2, column=1)
role = Entry(root, width=30)
role.grid(row=3, column=1)
shift = Entry(root, width=30)
shift.grid(row=4, column=1)

# Box labels
name_label = Label(root, text="First Name")
name_label.grid(row=1, column=0)
surname_label = Label(root, text="Second Name")
surname_label.grid(row=2, column=0)
role_label = Label(root, text="Position")
role_label.grid(row=3, column=0)
shift_label = Label(root, text="Shift")
shift_label.grid(row=4, column=0)

# Submit button
submit_btn = Button(root, text="Add record to Database", command=addemp) 
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Search button
search_btn = Button(root, text="Show Database", command=listemp)
search_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=122)

# Close connection
conn.close()

root.mainloop()
