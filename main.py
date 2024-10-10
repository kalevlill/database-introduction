import sqlite3

# Verbindung zu sqlite-DB (falls nicht vorhanden ist, dann wird die erstellt.)
conn = sqlite3.connect('studenden.db')

# Erstellung von Cursor um sql-Befehl durchzuführen. 
cursor = conn.cursor()

# Erstellung von Tabellen in studenden.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    age INTEGER NOT NULL, 
    course VARCHAR(32) NOT NULL
    );
''')
# Erste Funktion hinzufügen (CREATE)
def add_student(name, age, course):
    cursor.execute('''
    INSERT INTO Students (name, age, course) VALUES (?, ?, ?)
    ''', (name, age, course))
    conn.commit()
    print(f"{name} wurde hinzugefügt")

# Erstellung von READ funktion
def show_students():
    cursor.execute('SELECT id, name FROM Students')
    students = cursor.fetchall()
    for name in students:
        print(name)

# Update function to update student data
def update_student(id, name, age, course):
    cursor.execute('''
    UPDATE Students SET name = ?, age = ?, course = ?
    WHERE id = ?               
    ''',(name, age, course, id))
    conn.commit()
    print(f"updated student with id {id}")

# Adding a delete function to delete a student

def delete_student(id):
    cursor.execute('''
    DELETE FROM Students WHERE id = ?                
    ''',(id,))
    conn.commit()
    print(f"Student has been deleted with id {id}")

# define main function to get the user input
# user can choose from create, read, update and delete function
def main():
    while True:
        print("\n----- Studentenliste -----")
        print("1. Student  hinzufügen")
        print("2. Studentenliste anzeigen")
        print("3. Student aktualisieren")
        print("4. Student löschen")       
        print("5. Programm beenden")

        choice = input("Bitte wähle eine Option (1,2,3,4 oder 5): ")

        if choice == "1":
            print("Bitte gib die Daten des neuen Studenten ein: ")
            name = input("name: ")
            age = input("age: ")
            course = input("course: ")
            add_student(name, age, course)
        elif choice == "2":
            show_students()
        elif choice == "3":
            print("Bitte gib die aktualisierten Daten mit id ein: ")
            id = input("id: ")
            name = input("name: ")
            age = input("age: ")
            course = input("course: ")
            update_student(id, name, age, course)
        elif choice == "4":
            print("Bitte gib die ID des zu löschenden Studenten ein: ")
            id = input("id: ")
            delete_student(id)
        elif choice == "5":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe! Bitte wähle 1,2,3,4 oder 5")

if __name__ == "__main__":
    main()