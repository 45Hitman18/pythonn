class User:
    def __init__(self, user_id, name, email, phone, address):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Student(User):
    def __init__(self, user_id, name, email, phone, address):
        super().__init__(user_id, name, email, phone, address) #super()__init__ is used to access the main constructor 
        self.list_of_courses = []

    def add_course(self, course_id):
        self.list_of_courses.append(course_id)

    def view_courses(self):
        return self.list_of_courses


class Teacher(User):
    def __init__(self, user_id, name, email, phone, address):
        super().__init__(user_id, name, email, phone, address)
        self.list_of_courses = []
        self.list_of_batches = []

    def assign_course(self, course_id):
        self.list_of_courses.append(course_id)

    def assign_batch(self, batch_id):
        self.list_of_batches.append(batch_id)

    def view_courses_and_batches(self):
        return {
            "courses": self.list_of_courses,
            "batches": self.list_of_batches
        }


class Course:
    def __init__(self, course_id, course_name, description):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description
        self.teacher = None

    def assign_teacher(self, teacher_id):
        self.teacher = teacher_id

    def view_course_details(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "description": self.description,
            "teacher": self.teacher
        }


class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def validate_unique_id(self, user_id):
        for student in self.students:
            if student.user_id == user_id:
                return False
        for teacher in self.teachers:
            if teacher.user_id == user_id:
                return False
        return True

    def validate_unique_course_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return False
        return True

    def add_student(self, user_id, name, email, phone, address):
        if self.validate_unique_id(user_id):
            self.students.append(Student(user_id, name, email, phone, address))
            print(f"Student {name} added successfully.")
        else:
            print("Error: Duplicate ID.")

    def add_teacher(self, user_id, name, email, phone, address):
        if self.validate_unique_id(user_id):
            self.teachers.append(Teacher(user_id, name, email, phone, address))
            print(f"Teacher {name} added successfully.")
        else:
            print("Error: Duplicate ID.")

    def add_course(self, course_id, course_name, description):
        if self.validate_unique_course_id(course_id):
            self.courses.append(Course(course_id, course_name, description))
            print(f"Course {course_name} added successfully.")
        else:
            print("Error: Duplicate course ID.")

    def search_user_by_id(self, user_id):
        for student in self.students:
            if student.user_id == user_id:
                return student
        for teacher in self.teachers:
            if teacher.user_id == user_id:
                return teacher
        return None

    def assign_course_to_user(self, user_id):
        user = self.search_user_by_id(user_id)
        if user:
            print("Available Courses:")
            for idx, course in enumerate(self.courses, 1):
                print(f"{idx}. {course.course_name}")
            course_choice = int(input("Choose a course by number: "))
            if 1 <= course_choice <= len(self.courses):
                selected_course = self.courses[course_choice - 1]
                if isinstance(user, Student):
                    user.add_course(selected_course.course_id)
                    print(f"Course {selected_course.course_name} assigned to student {user.name}.")
                elif isinstance(user, Teacher):
                    user.assign_course(selected_course.course_id)
                    selected_course.assign_teacher(user.user_id)
                    print(f"Course {selected_course.course_name} assigned to teacher {user.name}.")
            else:
                print("Invalid course selection.")
        else:
            print("User not found.")

    def display_all_users(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.user_id}, Name: {student.name}")
        print("Teachers:")
        for teacher in self.teachers:
            print(f"ID: {teacher.user_id}, Name: {teacher.name}")

    def display_all_students(self):
        for student in self.students:
            print(f"ID: {student.user_id}, Name: {student.name}")

    def display_all_teachers(self):
        for teacher in self.teachers:
            print(f"ID: {teacher.user_id}, Name: {teacher.name}")

    def display_user_by_id(self, user_id):
        user = self.search_user_by_id(user_id)
        if user:
            print(f"ID: {user.user_id}, Name: {user.name}, Email: {user.email}, Phone: {user.phone}, Address: {user.address}")
            if isinstance(user, Student):
                print(f"Enrolled Courses: {user.view_courses()}")
            elif isinstance(user, Teacher):
                print(f"Courses: {user.view_courses_and_batches()['courses']}, Batches: {user.view_courses_and_batches()['batches']}")
        else:
            print("User not found.")

    def menu(self):
        while True:
            print("\n1. Add Course")
            print("2. Add Users")
            print("3. Display All Users")
            print("4. Display All Staff")
            print("5. Display All Students")
            print("6. Display User By ID")
            print("7. Assign Course To User")
            print("8. Exit")
            
            choice = int(input("Enter your choice: "))

            if choice == 1:
                course_id = input("Enter Course ID: ")
                course_name = input("Enter Course Name: ")
                description = input("Enter Course Description: ")
                self.add_course(course_id, course_name, description)
            elif choice == 2:
                user_type = input("Enter user type (student/teacher): ").lower()
                user_id = input("Enter User ID: ")
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone: ")
                address = input("Enter Address: ")
                if user_type == "student":
                    self.add_student(user_id, name, email, phone, address)
                elif user_type == "teacher":
                    self.add_teacher(user_id, name, email, phone, address)
                else:
                    print("Invalid user type.")
            elif choice == 3:
                self.display_all_users()
            elif choice == 4:
                self.display_all_teachers()
            elif choice == 5:
                self.display_all_students()
            elif choice == 6:
                user_id = input("Enter User ID: ")
                self.display_user_by_id(user_id)
            elif choice == 7:
                user_id = input("Enter User ID to assign a course: ")
                self.assign_course_to_user(user_id)
            elif choice == 8:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    sms = SchoolManagementSystem()
    sms.menu()
