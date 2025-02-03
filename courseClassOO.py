#Class: Course
#Purpose: Course objects keep track of grades

class Course(object):

    __courseName=""
    __grade=""

    #Constructor
    def __init__(self, courseName, semester, grade):
        self.__courseName=courseName.lower()
        self.__grade=grade.lower()                      
        self.__semester=semester.lower()

    #Gets courseName
    @property
    def courseName(self):
        return self.__courseName
    
    #Gets grade
    @property
    def grade(self):
        return self.__grade
    
    #Sets course name
    @courseName.setter
    def courseName(self, newName):
        self.__courseName=newName

    #Sets course grade
    @grade.setter
    def grade(self, newGrade):
        self.__grade=self.isValidGrade(newGrade)

    #Gets semester
    @property
    def semester(self):
        return self.__semester
    
    #Function: printCourse
    #Purpose: Prints name of course and grade
    #Parameters: none
    #Return: none
    def printCourse(self):
        print(self.__courseName.title()+" "+self.__semester.title()+": "+self.__grade.title()+"\n")

    #Function: isValidGrade
    #Purpose: checks if letterGrade is one of the following: "A" , "B" , "C" , "D" , "F". If not, gets a new grade from user.
    #Parameters: letterGrade (string)
    #Returns: letterGrade (string)
    def isValidGrade(self, letterGrade):
        letterGrade=letterGrade.lower()
        while letterGrade!="a" and letterGrade!="b" and letterGrade!="c" and letterGrade!="d" and letterGrade!="f":
            letterGrade=input("That grade is not part of the letter grading system. Please enter one of the following: A, B, C, D, F\n")
            letterGrade=letterGrade.lower()
        return letterGrade
