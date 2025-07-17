# student.py

from file_ops import read_file, write_file, append_to_file

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    year = input("Enter Year: ")
    record = f"{roll},{name},{course},{year}"
    append_to_file(record)
    print("Student added successfully!\n")

def view_students():
    data = read_file()
    if not data:
        print("No records found.\n")
    else:
        print("\n--- Student Records ---")
        for line in data:
            roll, name, course, year = line.strip().split(",")
            print(f"Roll: {roll}, Name: {name}, Course: {course}, Year: {year}")
        print()

def search_student():
    roll_search = input("Enter Roll Number to search: ")
    data = read_file()
    for line in data:
        roll, name, course, year = line.strip().split(",")
        if roll == roll_search:
            print(f"Found -> Roll: {roll}, Name: {name}, Course: {course}, Year: {year}\n")
            return
    print("Student not found.\n")

def update_student():
    roll_update = input("Enter Roll Number to update: ")
    data = read_file()
    new_lines = []
    updated = False

    for line in data:
        roll, name, course, year = line.strip().split(",")
        if roll == roll_update:
            print("Enter new details:")
            name = input("New Name: ")
            course = input("New Course: ")
            year = input("New Year: ")
            new_lines.append(f"{roll},{name},{course},{year}\n")
            updated = True
        else:
            new_lines.append(line)
    
    write_file(new_lines)
    print("Student record updated successfully.\n" if updated else "Student not found.\n")

def delete_student():
    roll_delete = input("Enter Roll Number to delete: ")
    data = read_file()
    new_lines = []
    deleted = False

    for line in data:
        roll, name, course, year = line.strip().split(",")
        if roll == roll_delete:
            deleted = True
            continue
        new_lines.append(line)
    
    write_file(new_lines)
    print("Student record deleted successfully.\n" if deleted else "Student not found.\n")
