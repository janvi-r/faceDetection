import faceDetection

dictionary = {}

class Student:    
    def __init__(self,studentName,studentImage,studentAttendance):
        self.studentName = studentName
        self.studentImage = studentImage
        self.studentAttendance = studentAttendance

#student1 = Student("Janvi", "/Users/janvi/hello/Photo on 2025-06-02 at 12.57 PM.jpg", None)
#student2 = Student("Dhvanay", "/Users/janvi/hello/Photo on 2025-06-02 at 12.57 PM.jpg", None)

    def addStudentToRecords(self):
        dictionary[self.studen] = self

    def changeStudentAttendanceInDictionary(self, studentAttendance):
        self.studentAttendance = studentAttendance
        dictionary[self.studentName] = self



    def setStudentName(self, studentName):
        self.studentName = studentName

    def getImage(self, studentImage):
        pass

    def add_student(studentName, studentImage, studentAttendance):
        student1 = Student(studentName, studentImage, studentAttendance)
        dictionary[studentName] = student1


    def get_student(studentName):
        if studentName in dictionary:
            return dictionary[studentName]
        else:
            return None


    def setImage(studentName, studentImage):
        if studentName in dictionary:
            dictionary[studentName].studentImage = faceDetection #gets the img from faceDetection
            return # updates the image in the dictionary
        else:
            return None

#JUST DO A DICTIONARY OF STUDENTS and Images INSTEAD OF A CLASS