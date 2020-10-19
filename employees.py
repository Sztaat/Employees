import sqlite3
conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS employees(
	Id INTEGER PRIMARY KEY ASC,
	Name varchar(30) NOT NULL,
	Surname varchar(30) NOT NULL,
	Role varchar(15) NOT NULL,
	Shift varchar(15) NOT NULL)''')


def disemp():
    c.execute("""SELECT id, name, surname, role, shift FROM employees""")
    lista = c.fetchall()
    for i in lista:
        print(i['id'], i['name'], i['surname'], i['role'], i['shift'])
    ret = input("Press any key to return to main menu")
    mainmenu()
    

def addemp():
    print("Add employee:")
    id = "NULL"
    name = str(input("Name:"))
    surname = str(input("Surname:"))
    role = str(input("Role (Reception, Driver, Supervisor):"))
    shift = str(input("Shift AM/PM:"))

    # Input record
    c.execute("INSERT INTO Employees VALUES("+ id +", '"+ name +"', '"+ surname +"', '"+ role +"', '"+ shift +"')")
    # Save change
    conn.commit()

    rep = input("More employee? Y/N")
    if rep == "Y":
                addemp()
    else:
        ret = input("Press ENTER to return to main menu")
        mainmenu()

def delemp():
    print("WARNING: This process is irreversible")
    ident = input("Enter employee's ID")
    c.execute("DELETE FROM Employees WHERE id = ("+ ident +")")
    # Save change
    conn.commit()
    print("Employee with ID ", ident, " has been deleted")
    rep = input("More employee? Y/N")
    if rep == "Y":
                addemp()
    else:
        ret = input("Press ENTER to return to main menu")
        mainmenu()

def mainmenu():                
    print("Employee's database")
    print("Show all employees - 1")
    print("Search database - 2")
    print("Add new employee - 3")
    print("Delete employee - 4")
    print("Exit - 0")
    opt = input("Choose one of the options above: ")
    if opt == "1":
        disemp()
    elif opt == "2":
        searemp()
    elif opt == "3":
        addemp()
    elif opt == "4":
        delemp()
    else:
        print("Good bye")

mainmenu()

# Close connection
conn.close()


