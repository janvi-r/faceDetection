import shelve
from faceDetection import capture_face_with_countdown

class Student:
    def __init__(self, studentName, studentImage, studentAttendance):
        self.studentName = studentName
        self.studentImage = studentImage
        self.studentAttendance = studentAttendance
    
    def __str__(self):
        return f"Student(name={self.studentName}, image={self.studentImage}, attendance={self.studentAttendance})"

    def setstudentName(self, name):
         self.studentName = name
    
    def setstudentImage(self, file_path):
         self.studentImage = file_path
    
    def setstudentAttendance(self, attendance):
         self.studentAttendance = attendance
    
    def getstudentName(self):
         return self.studentName
        
    def getstudentImage(self):
         return self.studentImage
    
    def getstudentAttendance(self):
         return self.studentAttendance

         # print("runnign from student.py")
def intro():
     name = input("Enter student name: ")
     file_path = capture_face_with_countdown(face_id=0, countdown_seconds=5)
     students = Student(name, file_path, None)

     with shelve.open('studentInfo.db') as db:
          db[file_path] = students
               #print(db['/Users/janvi/hello/Registration/stored-faces/0_1749071106.jpg'].getstudentName())
               #print(db["/Users/janvi/hello/Registration/stored-faces/0_1749061249.jpg"].getstudentName())
     db.close()

#   with open('classList.txt', 'w') as file:
# # #     file.write(name + '\n')
    






# def store(name, file_path, attendance):
#     student = Student(name, file_path, attendance)
#     with shelve.open('studentInfo.db') as db:
#         db[name] = student
#                         # print(db["janvi"].__str__)

#     db.close()




# def main():
#     name = input("Enter name: ")
#     file_path = capture_face_with_countdown(face_id=0, countdown_seconds=5)

#     if file_path:
#         student = Student(name, file_path, None)
#         print(student)
#         student.setstudentName()
#         #print(f"Student created: {student.getstudentName()} with image {student.getstudentImage()}")
#     else:
#         print("Failed to capture and save face.")

# if __name__ == "__main__":
#     main()

