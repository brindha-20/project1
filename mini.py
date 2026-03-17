students={}
def add_student(name,marks):
    students[name]=marks
    print("student added")
def display_students():
    for name,marks in students.items():
        print(name,":",marks)
add_student("brindha",99)
add_student("loks",90)
display_students()