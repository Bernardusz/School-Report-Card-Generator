from allfunctions import Person, Student, Classroom

if __name__ == "__main__":
    Class = Classroom()
    with open("welcome.txt", "r")as f:
        text = f.readlines()
        for line in text:
            print(line)
    print("\n-------------------------------------------------------------\n")
    while True:
        userinput = input("What do you want to do ? : ").lower()
        
        if userinput == "add student": #done
            new_student = input("Input the student's name : ")
            new_data = input("Age, Attendance, Extracurricular : ").split(",")
            try:
                Class.add_student(new_student, int(new_data[0]), int(new_data[1]), int(new_data[2]))
                print(f"Added {new_student} !")
            except:
                print("Invalid input !")
            print("\n-------------------------------------------------------------\n")
        
        elif userinput == "add grade": #done
            studentname = input("Enter the student's name : ")
            subject = input("Enter the subject's name : ")
            try:
                grade = int(input("input the grade : "))
                Class.add_grades(studentname, subject, grade)
            except:
                print("Invalid input !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "show class average": 
            try:
                print(f"The class' average is : {Class.show_average}")
            except:
                print("App's Error !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "return class performance": 
            try:
                print(f"The class' performance is : {Class.return_performance}")
            except:
                print("Unable to show the performance")
            print("\n-------------------------------------------------------------\n")
        
        elif userinput == "top student": 
            try:
                print(Class.top_student)
            except:
                print("App's error !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "save to json":
            jsonfile = input("Enter the file's name [file.json]: ")
            try:
                Class.save_to_json(jsonfile)
            except:
                print("Invalid file's name !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "load from json": 
            jsonfile1 = input("Enter file name [file.json] : ")
            try :
                Class.load_json(jsonfile1)
            except:
                print("Invalid File Name !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "exit": #done
            print("See you ! Don't forget, More study = Bigger brain !")
            break
            
        else: 
            print("Invalid Command !")
            print("\n-------------------------------------------------------------\n")