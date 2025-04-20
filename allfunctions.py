import json
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    @abstractmethod
    def introduce(self):
        return f" Hi, I'm {self.name}, age {self.age}"
    
class Student(Person):
    def __init__(self, name, age, attendance, extra_curricular_point):
        super().__init__(name, age)
        self.__grades = {}
        self.__grades["grades"] = {}
        self.attendance = attendance #No using percentage bruh, it throws more bug
        self.extracurricular = extra_curricular_point
        self.total = 0
        self.subjects = 0

    @property
    def introduce(self):
        return f"Hi ! I'm a student, my name is {self.name} and I'm {self.age} years old !"
    
    @property
    def return_grades(self):
        return self.__grades
    
    def average(self):
        self.total = 0
        self.subjects = 0
        for subject in self.__grades["grades"]:
            self.total += self.__grades["grades"][subject]
            self.subjects += 1
        self.total /= self.subjects

    @property
    def get_average(self):
        self.average()
        return self.total
        

    def add_grades(self, subject , grade):
        self.__grades["grades"][subject] = grade
        

    @property
    def is_average(self):
        if self.total >= 75 and self.attendance >= 0.75 and self.extracurricular >= 10:
            return True
        else:
            return False
    
    @property
    def is_excellent(self):
        if self.total >= 90 and self.attendance >= 0.9 and self.extracurricular >= 10:
            return True
        else:
            return False

class Classroom:
    def __init__(self):
        self.students = {}
        self.average = 0
        self.divider = 0
        self.top_students = {}

    def add_student(self, name, age, attendance, extracurricular):
        self.students[name] = Student(name, age, attendance, extracurricular)
        print(self.students[name].introduce)
        

    def add_grades(self, name, subject, grades):
        if name in self.students:
            self.students[name].add_grades(subject, grades)
            print("Grades updated!")
        else:
            print("Student not found!") 


    @property
    def show_average(self):
        for student in self.students:
            self.average += self.students[student].get_average
            self.divider += 1
        self.average /= self.divider
        return self.average
    
    @property
    def return_performance(self):
        student_performance = {}
        for student in self.students:
            placeholder = self.students[student]
            name = placeholder.name
            age = placeholder.age
            attendance = placeholder.attendance
            extracurricular = placeholder.extracurricular
            is_average = placeholder.is_average
            is_excellent = placeholder.is_excellent

            student_performance[name] = {"Age" : age,
                                         "Grades" : {},
                                         "Attendance" : attendance,
                                         "Extracurricular_points" : extracurricular,
                                         "Average" : is_average,
                                         "Excellent" : is_excellent}

            grades = placeholder.return_grades
            
            for subject in grades:
                student_performance[name]["Grades"][subject] = grades[subject]
        
        return student_performance

    @property
    def top_student(self):
        if not self.students:
            return "No students in the class."
        top = max(self.students.values(), key=lambda s: s.get_average)
        return f"Top student is {top.name} with average {top.get_average:.2f}"


    def save_to_json(self, file):
        data = {}
        data["students"] = {}

        for name in self.students:
            data["students"][name] = {}
            data["students"][name] = {
                "Name": self.students[name].name,
                "Age": self.students[name].age,
                "Grades": self.students[name].return_grades,
                "Attendance": self.students[name].attendance,
                "Average" : self.students[name].is_average,
                "Excellent" : self.students[name].is_excellent,
                "Exreacurricular Point": self.students[name].extracurricular,
                "Average Grade": self.students[name].total,
                "Subjects Total" : self.students[name].subjects
                }

        with open(file, "w") as f:
            json.dump(data, f, indent=4)
        print("Saved !\n")
    
    def load_json(self, file):
        with open(file, "r") as f:
            data = json.load(f)
            for student in data["students"]:
                name = student
                age = data["students"][student]["Age"]
                grades = data["students"][student]["Grades"]["grades"]
                attendance = data["students"][student]["Attendance"]
                extracurricular = data["students"][student]["Exreacurricular Point"]
                total = data["students"][student]["Average"]
                subjects = data["students"][student]["Subjects Total"]
                self.students[name] = Student(name, age, attendance, extracurricular)
                
                for grade in grades:  
                    self.students[name].add_grades(grade, grades[grade])
                self.students[name].total = total
                self.students[name].subjects = subjects
        print("Loaded !\n")

                
                
            


        



        
        
    

        
            
