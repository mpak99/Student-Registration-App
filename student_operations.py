import datetime
from logging import exception
# from tkinter import Y
# from tracemalloc import start

# from numpy import average, gradient, number 

import os

from pyrsistent import b
clear = lambda : os.system("cls")

# import statistics
import sys

os.chdir("beginner_python_project")

# active_students=[]
# Graduated_students=[]  
class RSC(Exception):
    pass



#============================================ **ADD STUDENTS FUNCTION** ============================================

def add_student(active_students,) :
    clear()
    student = dict()
    from pickle import load
    with open("GraduatedStudents.info", "rb") as Graduated_students_DB :
        Graduated_students = load(Graduated_students_DB)
#----------------------------------- first name -------------------------------------------------   
    student["first_name"] = input("Enter first name  :")
#----------------------------------- last name -------------------------------------------------    
    student["last_name"] = input("Enter last name :")
#----------------------------------- birth day -------------------------------------------------
    while True :
        try :    
            student["birthday"] = (input("Enter birthday (yyyy/mm/dd) :"))
            time = datetime.datetime.strptime(student["birthday"], "%Y/%m/%d")
            break
        except(ValueError):
            print("birthday shoul be in this format : (yyyy/mm/dd) ") 
            input("Press Enter to try again")
#----------------------------------- code meli -------------------------------------------------    
    class RCM(Exception) :
        pass
    class CMD(Exception):
        pass
    
    while True :
        try:
            student["code_meli"] = int(input("Enter code meli :"))
            for user in active_students :
                if  user["code_meli"] == student["code_meli"]  : raise RCM                  
            for user in Graduated_students :
                if  user["code_meli"] == student["code_meli"]  : raise RCM
            if len(str((student["code_meli"]))) !=10 : raise CMD
            break
        except(ValueError) :
            print("code meli is a number")
            input("Press Enter to try again")
        except(RCM) :
              print("This code meli already exists")
              input("Press Enter to try again")
        except(CMD) :
             print("code meli must be 10 digits")
             input("Press Enter to try again")      
#------------------------------------- student code -----------------------------------------------
    class SCD(Exception):
        pass                
    while True :
        try:        
            student["student_code"] = int(input("Enter student code :"))
            for user in active_students :
                if  user["student_code"] == student["student_code"]  : raise RSC
            for user in Graduated_students :
                if  user["student_code"] == student["student_code"]  : raise RSC
            if len(str(student["student_code"])) !=5 : raise SCD
            for user in Graduated_students :
                if  user["student_code"] == student["student_code"]  : raise RSC
            if len(str(student["student_code"])) !=5 : raise SCD
            break
        except(ValueError) :
            print("student code is a number")
            input("Press Enter to try again")
        except(RSC):
                print("This student code already exists")
                input("Press Enter to try again")  
        except(SCD) :
              print("student code must be 5 digits")
              input("Press Enter to try again")          
#------------------------------------- courses and grades -----------------------------------------------            
    class CWC(Exception):
        pass          
    while True :
        try:
            course = input("Enter course :")
            grade = int(input("Enter grade :"))
            student["courses"] = [course]
            student["grades"] = [grade]
            choice=input("Do you want to add another course? Y/N :")
            while choice == 'Y' or choice == 'y' :
                course = input("Enter course :")
                grade = int(input("Enter grade :"))
                student["courses"].append(course)
                student["grades"].append(grade)
                choice=input("Do you want to add another course? Y/N :")
            
            if choice == 'N' or choice == 'n' :
                print("press Enter to continue")
                break
            if choice != 'y' or choice != 'Y' or choice != 'n' or choice != 'N' : raise CWC    
        except(CWC) :
            student["courses"].append(course)
            student["grades"].append(grade)
            print("Wrond Choice !")
            print("Progress has been deleted")
            input("Press Enter to try again")
        except(ValueError) :
            print("grade is a number")
            input("Press Enter to try again")    
            
    active_students.append(student) 
    return True       


            
#============================================ **FIND STUDENTS FUNCTION** ============================================            
class studentNF(Exception):
    pass
def find_student(all_students) :

    from pickle import load

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

    clear()

    student_search = int(input(" Enter student code :"))
    for student in all_students  :         
        if student["student_code"] == student_search :
            print(f"student first name : {student['first_name']}")
            print(f"student last name : {student['last_name']}")
            print(f"student code meli : {student['code_meli']}")
            print(f"student student code : {student['student_code']}")
            import datetime
            today = datetime.datetime.today()
            time = datetime.datetime.strptime(student["birthday"], "%Y/%m/%d")
            birthday = datetime.datetime.strptime(student["birthday"],"%Y/%m/%d") 
            age = today.year - birthday.year
            print(f"student age : {age}")
            print(f"student courses : {student['courses']}")
            print(f"student grades : {student['grades']}")
            average = sum(student['grades'])/len(student['grades'])
            print(f"student average score : {average}")
            max_score = max(student['grades'])
            print(f"student max score : {max_score}")
            min_score = min(student['grades'])
            print(f"student min score : {min_score}")
            print("-----------------------------------------------------------")
            return True
            break
    else :
        print("student NOT found !")    




#============================================ **DELETE STUDENTS FUNCTION** ============================================
def delete_student(active_students,Graduated_students) :
    clear()
    student_search = int(input(" Enter student code :"))
    for student in active_students :
        if student["student_code"] == student_search :
            print(f"student first name : {student['first_name']}")
            print(f"student last name : {student['last_name']}")
            print(f"student code meli : {student['code_meli']}")
            print(f"student student code : {student['student_code']}")
            import datetime
            today = datetime.datetime.today()
            time = datetime.datetime.strptime(student["birthday"], "%Y/%m/%d")
            birthday = datetime.datetime.strptime(student["birthday"],"%Y/%m/%d") 
            age = today.year - birthday.year
            print(f"student age : {age}")
            print(f"student courses : {student['courses']}")
            print(f"student grades : {student['grades']}")
            average = sum(student['grades'])/len(student['grades'])
            print(f"student average score : {average}")
            max_score = max(student['grades'])
            print(f"student max score : {max_score}")
            min_score = min(student['grades'])
            print(f"student min score : {min_score}")
            print("--------------------------------------------")
            choice = input("Press R to remove or M to move the student to graduated list : ")
            if choice == 'R' or choice == 'r' :
                active_students.remove(student)
                print("removed successfully.")
                break
            elif choice == 'M' or choice == 'm' :
                Graduated_students.append(student)
                # list_student_G(Graduated_students)
                active_students.remove(student)
                print("moved successfully")
                break
            else:
                print("Wrong choice")
                print("press Enter to continue")
                break
    else :
        print("student was not found !")
        print("press Enter to continue")
        
    return True
    

#============================================ **CHANGE FUNCTION** ============================================
            
# class CWC(Exception):
#     pass
def change_courses(active_students) :
    clear()
    student_search = int(input(" Enter student code :"))
    for student in active_students  :         
        if student["student_code"] == student_search :
            print(f"student courses : {student['courses']}")
            print(f"student grades : {student['grades']}")


            student_courses=[]
            student_grades=[]      

            choice = input("Press A to add course or R to remove course :")
            if choice == 'a' or choice == 'A' :
                course = input("Enter course :")
                grade = int(input("Enter grade :"))
                student_courses.append(course)
                student_grades.append(grade)
                print(student_courses)
                print(student_grades)

                student["courses"].extend(student_courses)
                student["grades"].extend(student_grades)
                print("course was added successfully.")
                print("press Enter to continue")
                return True

            elif choice == 'r' or choice == 'R' :
                course = input("Enter course :")

                grade_index = int(input("grade index:"))


                if course in student["courses"] :

                    student["courses"].remove(course)
                    student["grades"].pop(grade_index)

                    print("course was removed successfully")
                    print("press Enter to continue")
                    return True
            else:
                print("wrong choice")
                return False
    else :
        print("student NOT found !") 
        return False 













 


#============================================ **LIST STUDENTS FUNCTION** ============================================           
def list_student(active_students,Graduated_students) :
    clear()
    print("---------Active Students---------")
    for student in active_students :
        print("Active Student : ")
        print(f"student first name : {student['first_name']}")
        print(f"student last name : {student['last_name']}")
        print(f"student code meli : {student['code_meli']}")
        print(f"student student code : {student['student_code']}")
        import datetime
        today = datetime.datetime.today()
        time = datetime.datetime.strptime(student["birthday"], "%Y/%m/%d")
        birthday = datetime.datetime.strptime(student["birthday"],"%Y/%m/%d") 
        age = today.year - birthday.year
        print(f"student age : {age}")
        print(f"student courses : {student['courses']}")
        print(f"student grades : {student['grades']}")
        average = sum(student['grades'])/len(student['grades'])
        print(f"student average score : {average}")
        max_score = max(student['grades'])
        print(f"student max score : {max_score}")
        min_score = min(student['grades'])
        print(f"student min score : {min_score}")
        print("--------------------------------------------")
        
        
    

    print("---------Graduated Students---------")    
    for student in Graduated_students :
        print("Graduated Student : ")
        print(f"student first name : {student['first_name']}")
        print(f"student last name : {student['last_name']}")
        print(f"student code meli : {student['code_meli']}")
        print(f"student student code : {student['student_code']}")
        import datetime
        today = datetime.datetime.today()
        time = datetime.datetime.strptime(student["birthday"], "%Y/%m/%d")
        birthday = datetime.datetime.strptime(student["birthday"],"%Y/%m/%d") 
        age = today.year - birthday.year
        print(f"student age : {age}")
        print(f"student courses : {student['courses']}")
        print(f"student grades : {student['grades']}")
        average = sum(student['grades'])/len(student['grades'])
        print(f"student average score : {average}")
        max_score = max(student['grades'])
        print(f"student max score : {max_score}")
        min_score = min(student['grades'])
        print(f"student min score : {min_score}")
        print("--------------------------------------------")
        
    print("Press Enter to continue")
    return True
#============================================ **SAVE STUDENTS FUNCTION** ============================================
def save_student(active_students) :
    from pickle import dump
    with open("ActiveStudents.info", "wb") as active_students_DB :
        dump(active_students,active_students_DB)
def save_GS(Graduated_students) :    
    from pickle import dump
    with open("GraduatedStudents.info", "wb") as Graduated_students_DB :
        dump(Graduated_students,Graduated_students_DB)
        print("saved.")
        print("Press Enter")
#============================================ **QUIT APPLICATION FUNCTION** ============================================        
def quit_application() :
    sys.exit()
    
        

        
        

           




            

    

                       

            
                
    

    
    
    
    
        
        
                
          
            
                          

    
    
            



        
               
                
            
            
        
       

        






            

               
                    
    
            
            



            
            
            


                   
            
                
        

    

    
    
    
    
    
    
    
    
    
                    
            
                    




                   







                
                

    
             
                    
                    
           
                
                




              
                
              

            
       

         
                
                  
            
           

            
                    
            
            
            
            
            
            
            


   
    
    
    
    
    
    
    
    
    
    
    
                    
                   




            

        
        
            
    
        
    
       
    
   

        
    
    
        
    
    
           
        
        
        
                   
            
