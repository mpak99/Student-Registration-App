import student_operations as SO
import os
clear = lambda: os.system("cls")
from pickle import load



# os.chdir("beginner_python_project")
# file = open("ActiveStudents.info", "w")


# active_students=[]

# Graduated_students=[] 



#------------------ Main -------------------------------




try:
    with open("ActiveStudents.info", "rb") as active_students_DB :
        active_students = load(active_students_DB)
except(FileNotFoundError):
    print("created again")
    active_students=[]
    input()
try:
    with open("GraduatedStudents.info", "rb") as Graduated_students_DB :
        Graduated_students = load(Graduated_students_DB)
except(FileNotFoundError):
    print("created again")
    Graduated_students=[] 
    input()

all_students= []       
all_students.extend(active_students) 
all_students.extend(Graduated_students)





while True :
    clear()
    print("------------------------------------")
    print("Press 'A' to add a student")
    print("Press 'F' to find a student")
    print("Press 'D' to (re)move a student")
    print("Press 'C' to change courses")
    print("Press 'L' to list students")
    print("Press 'S' to save students")
    print("Press 'Q' to quit application")
    print("------------------------------------")

    choice = input("Enter your choice :")
    if choice == 'A' or choice == 'a' :
        SO.add_student(active_students)                
    elif choice == 'F' or choice == 'f' :
        SO.find_student(all_students)
    elif choice == 'D' or choice == 'd' :        
        SO.delete_student(active_students,Graduated_students)
    elif choice == 'C' or choice == 'c' :    
        SO.change_courses(active_students)
    elif choice == 'L' or choice == 'l' :    
        SO.list_student(active_students,Graduated_students)


    elif choice == 'S' or choice == 's' : 
        SO.save_student(active_students)
        SO.save_GS(Graduated_students)
    elif choice == 'Q' or choice == 'q' :       
        break
    else:
        print("Wrong Choice !")
    input()
    
