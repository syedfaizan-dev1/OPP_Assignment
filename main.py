from university import University



uni = University()
uni.add_teacher('Mr. Smith')
uni.add_teacher('Ms. Johnson')
uni.add_student('Alice')
uni.add_student('Bob')
uni.add_student('Charlie')
uni.add_class('Python', '10:00 - 12:00')
uni.add_class('Java', '14:00 - 16:00')
uni.add_class('C++', '16:00 - 18:00')

uni.assign_class_to_student('Alice', 'Mr. Smith', 'Python')
uni.assign_class_to_student('Bob', 'Ms. Johnson', 'Java')
uni.assign_class_to_student('Charlie', 'Mr. Smith', 'Python')

uni.show_students()
uni.show_teachers()
uni.show_assigned_classes()


uni.students_in_class('Python')
uni.students_in_class('Java')
uni.students_in_class('C++')