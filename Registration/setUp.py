# from student import Student
# from student import store
# from faceDetection import capture_face_with_countdown
# import os
# import pickle
# import shelve

# student_dict = {}

# def getStudentDetails(studentName,studentImage, studentAttendance ):
#         return {
#             "name": studentName,
#             "image": studentImage,
#             "attendance": studentAttendance
#         }

# def addStudentToDatabase(student):
#     student_dict[student.studentName] = student
#    # save_Students(student_dict)

# def main():
#     #load_students()
#     print("Welcome to the Student Registration System")
#     name = input("Enter name: ")
#     file_path = capture_face_with_countdown(face_id=0, countdown_seconds=5)
#     #store(name, file_path, None)

#     if file_path:
#          student = Student(name, file_path, None)
#          addStudentToDatabase(student)
#          with open('/Users/janvi/hello/Authentication/keys.txt', 'a') as file:
#             file.write(str(student) + '\n')
        
#          with open('/Users/janvi/hello/Authentication/keys.txt', 'r') as file:
#               for line in file:
#                    print(line)


#     #student = Student(name, file_path, None)

#     #with shelve.open('studentDB.db') as db:
#         # db[name] = student
#         #print(db["janvi"].__str__)

#     #db.close()



#     # if file_path:
#     #     student = Student(name, file_path, None)
#     #     addStudentToDatabase(student)
#     #     with open('/Users/janvi/hello/Authentication/keys.txt', 'a') as file:
#     #         file.write(str(student) + '\n')
#     #     # folder_path = 'my_folder'
#     #     # file_path = os.path.join(folder_path, 'object.pkl')

#     #     # # Create the folder if it doesn't exist
#     #     # os.makedirs(folder_path, exist_ok=True)

#     #     # # Check if the object file already exists
#     #     # if os.path.exists(file_path):
#     #     #     # Load the existing object
#     #     #     with open(file_path, 'rb') as file:
#     #     #         student = pickle.load(file)
#     #     #     print('Object loaded from disk:', student)
#     #     # else:
#     #     #     # Define your object
           
#     #     #     # Save the object to disk
#     #     #     with open(file_path, 'wb') as file:
#     #     #         pickle.dump(student, file)
#     #     #     print('Object saved to disk:', student)
#     #     # print(student)
             
#     # else:
#     #     print("Failed to capture and save face.")

#     # # File location for permanent storage
#     # """ FILE_PATH = "/Users/janvi/hello/Authentication/stored_students.pkl"

#     # # Load existing students from file
#     # def load_students():
#     #     if os.path.exists(FILE_PATH):
#     #         with open(FILE_PATH, "rb") as f:
#     #             return pickle.load(f)
#     #     return {}  # return empty dict if no file yet

#     # # Save students to file
#     # def save_students(students_dict):
#     #     with open(FILE_PATH, "wb") as f:
#     #         pickle.dump(students_dict, f)

#     # # Load existing students (persistent)
#     # students = load_students()

#     # # Print to verify
#     # for s in students.values():
#     #     print(s) """

# if __name__ == "__main__":
#     main()










