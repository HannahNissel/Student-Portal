#Class: Student
#Purpose: Student objects keep track of student's academic information

import courseClassOO

class Student(object):
    
    #Constructor
    def __init__(self, studentName, id):
        self.__studentName=studentName.lower()
        self.__courses=[]
        self.__studentId=id

    #Get student name
    @property
    def studentName(self):
        return self.__studentName
    
    #Get student's course objects
    @property
    def courses(self):
        return self.__courses
    
    #Set student name
    @studentName.setter
    def studentName(self, newName):
        self.__studentName=newName

    #Get student ID
    @property
    def studentId(self):
        return self.__studentId

    #Function: addCourse
    #Purpose: Creates a new course object and adds it to this student's courses
    #Parameters: courseName (string), grade (string)
    #Return: None
    '''Creates a new course object and adds it to student's courses'''
    def addCourse(self, courseName, semester, grade):
        newCourse=courseClassOO.Course(courseName, semester, grade)                                          
        self.__courses.append(newCourse)

    #Function: isRegisteredForCourse
    #Purpose: Checks if student is registered for a specific course
    #Parameters: course (string), semester (string)
    #Return: isRegistered (boolean)
    '''checks if student is registered for specific course'''
    def isRegisteredForCourse(self, courseTitle, semester):
        isRegistered=False
        count=0
        for course in self.__courses:
            if course.courseName==courseTitle and course.semester==semester:
                count+=1
        if count>0:
            isRegistered=True
        return isRegistered
    
    #Function: isRegisteredForSemester
    #Purpose: Checks if student is registered for a semester
    #Parameters: semester (string)
    #Return: isRegistered (boolean)
    '''checks if student is registered for a semester'''                
    def isRegisteredForSemester(self, semester):
        isRegistered=False
        count=0
        for course in self.__courses:
            if course.semester==semester:
                count+=1
        if count>0:
            isRegistered=True
        return isRegistered
        
    #Function: hasCourses
    #Purpose: Checks if courses has course objects in it
    #Parameters: None
    #Return: coursesPresent (boolean)
    '''checks if student is registered for any courses'''
    def hasCourses(self):
        if not self.__courses:
            coursesPresent=False
        else:
            coursesPresent=True
        return coursesPresent
    
    #Function: findCourse
    #Purpose: Finds index of a specific course in courses
    #Parameters: courseTitle (string), semester (string)
    #Return: index (int)
    '''finds index of a specific course in list of student's courses'''
    def findCourse(self, courseTitle, semester):
        index=-1
        for num in range (len(self.__courses)):
            if self.__courses[num].courseName==courseTitle and self.__courses[num].semester==semester:
                index=num
        return index
    
    #Function: writeReportCard
    #Purpose: Writes a text file including the student's name, courses, grades, and teachers' comments of  a specific semester
    #Parameters: semester (string)
    #Return: none
    def writeReportCard(self, semester):
        reportCard = open(self.__studentName.title()+semester.title()+"ReportCard.txt", "w")
        reportCard.write("Report Card\n")
        reportCard.write("______________\n")
        reportCard.write("\n"+self.__studentName.title())
        reportCard.write("\nStudent ID: "+str(self.__studentId)+"\n")
        reportCard.write("\nSemester: "+semester.title()+"\n")

        #Only prints courses of this semester
        for course in self.__courses:
            if course.semester==semester:
                reportCard.write("\n"+course.courseName.title()+": "+course.grade.title())

                #Administrator can enter a comment for this course
                comment=input("\nEnter a comment for "+course.courseName.title()+". Type \"none\" to opt out.\n")
                if comment!="none":
                    reportCard.write("\nComment: \n"+comment+"\n")

        reportCard.close()

    #Function: writeTranscript
    #Purpose: Writes a text file including the student's name, courses, and grades
    #Parameters: none
    #Return: none
    def writeTranscript(self):
        transcript = open(self.__studentName.title()+"Transcript.txt", "w")
        transcript.write("Transcript\n")
        transcript.write("_____________\n")
        transcript.write("\n"+self.__studentName.title())
        transcript.write("\nStudent ID: "+str(self.__studentId)+"\n")
        for course in self.__courses:
            transcript.write("\n"+course.courseName.title()+" "+course.semester.title()+": "+course.grade.title())
        transcript.close()
    
    #Function: printStudent
    #Purpose: Prints all of this student's courses and grades
    #Parameters: none
    #Return: none
    def printStudent(self):
        if not self.hasCourses():
            print(self.__studentName.title()+" is not signed up for any courses.")
        else:
            print("\n"+self.__studentName.title()+"'s grades:\n")
            for course in self.__courses:
                course.printCourse()





