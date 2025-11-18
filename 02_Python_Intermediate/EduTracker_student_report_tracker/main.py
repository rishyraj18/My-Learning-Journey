from modules.student import student
from modules.course import course
from Utility.decorators import validate_input , log_action, performance_check
from Utility.validators import validate_mark, validate_name, validate_roll


print("Hi, Welcome to EduTrack_Student_report_tracker")



inp = None
student_ID = {}
course_ID = {}
while inp != 9:
    print("select One Option from below")
    print("1. Add Student\n"
    "2. Edit Student Name\n"
    "3. Add Course\n"
    "4.Add Topics to a Course\n"
    "5. Update Marks\n"
    "6. Update Attendance\n"
    "7. View Student Details\n"
    "8. View All Students\n"
    "9. Exit")
    inp = int(input("Please the Number: "))

    match inp:
            case 1:
                print("Give the below Details for student registeration")
                std_id = input("Please enter the student ID: ")
                name = input("Please enter student name: ")
                roll_no = int(input("Please enter Roll_no: "))
                course_name = input("Please Enter Course name:")
                student_ID[std_id] = student(name, roll_no, course_name)
            case 2:
                std_id = input("Please the student_ID to change the details: ")
                n_name = input("Please Enter the Name: ")
                if std_id in student_ID:
                    if validate_name(n_name):
                        (student_ID[std_id]).update_name(n_name)
                    else:
                        print("Name Format Missmatch")
                else:
                    print("Please Enter Correct Student ID")

            case 3:
                course_id = input("Please Enter the Course ID: ")
                course_name = input("Please Enter the Course Name: ")
                course_duration = input("Please Enter the Course Duration: ")
                if course_id not in course_ID:
                    course_ID[course_id] = course(course_name, course_duration)
                else:
                    print("Course ID already Exists")

            case 4:
                course_id = input("Please Enter the Course ID: ")
                n_course_name = input("Please Enter your new course name: ")
                if course_id in course_ID:
                    if validate_name(n_course_name):
                        course_ID[course_id].add_topic(n_course_name)
                    else:
                        print("Course Name format Mismatch") 

            case 5:
                std_id = input("Please the student_ID to update Marks: ")
                marks = int(input("Please enter marks: "))
                if std_id in student_ID:
                    student_ID[std_id].update_marks(marks)
                else:
                    print("Please Enter Correct Student ID")
                
            case 6:
                std_id = input("Please the student_ID to update Marks: ")
                attendance = int(input("Please enter attendance: "))
                if std_id in student_ID:
                    student_ID[std_id].update_attendance(attendance)
                else:
                    print("Please Enter Correct Student ID")
            
            case 7:
                std_id = input("Please the student_ID to update Marks: ")
                if std_id in student_ID:
                    student_ID[std_id].display_info()
                else:
                    print("Please Enter Correct Student ID")
                
            case 8:
                for std_id in student_ID:
                    student_ID[std_id].view_name()

            case _:
                print("Please Enter Correct option")
    
print("Exiting EduTracker Module")



