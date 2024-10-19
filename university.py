from classes import Classes
from humans import Humans

class University(Humans, Classes):
    def __init__(self):
        super().__init__()

        # List of classes
        self.classes = {}

        # Dictionary where each student is assigned a teacher and class
        # Format: {student: {teacher: ['class', 'time']}}
        self.assigned_classes_and_teachers = {}

    def assign_class_to_student(self, student, teacher, class_name):
        # Check if the class exists
        if class_name not in self.classes:
            print(f"Class '{class_name}' does not exist.")
            return
        
        # Check if the teacher and student exist
        if teacher not in self.teachers:
            print(f"Teacher '{teacher}' is not in the system.")
            return
        if student not in self.students:
            print(f"Student '{student}' is not in the system.")
            return
        
        # Assign class and teacher to the student
        self.assigned_classes_and_teachers[student] = {teacher: [class_name, self.classes[class_name]]}
    
    def show_students(self):
        print("Students:")
        for student in self.students:
            print(f"- {student}")

    def show_teachers(self):
        print("Teachers:")
        for teacher in self.teachers:
            print(f"- {teacher}")
    
    def show_assigned_classes(self):
        print("Assigned Classes:")
        for student, assignment in self.assigned_classes_and_teachers.items():
            for teacher, class_info in assignment.items():
                class_name, time = class_info
                print(f"Student: {student} | Teacher: {teacher} | Class: {class_name} | Time: {time}")

    def students_in_class(self, class_name):
        """
        Show how many students are in the specified class and which teacher is assigned.
        """
        if class_name not in self.classes:
            print(f"Class '{class_name}' does not exist.")
            return
        
        students_list = []
        teacher_assigned = None
        
        for student, assignment in self.assigned_classes_and_teachers.items():
            for teacher, class_info in assignment.items():
                if class_info[0] == class_name:
                    students_list.append(student)
                    teacher_assigned = teacher
        
        if students_list:
            print(f"Class '{class_name} | {self.classes[class_name]} ' has {len(students_list)} students assigned:")
            for student in students_list:
                print(f"- {student}")
            print(f"Teacher assigned: {teacher_assigned}")
        else:
            print(f"No students are assigned to the class '{class_name}'.")



