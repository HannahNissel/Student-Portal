#Class: Roster
#Purpose: Roster objects keep track of groups of students

import studentClassOO
import pickle
import os
import random

class Roster(object):


    #Constructor
    def __init__(self, studentList):

        #List of student objects
        self.__masterStudentList=studentList
        self.__studentIds=[]

    #Gets masterStudentList
    @property
    def masterStudentList(self):
        return self.__masterStudentList
    
    #Set masterStudentList
    @masterStudentList.setter
    def masterStudentList(self, newList):
        self.__masterStudentList=newList

    #Gets studentIds
    @property
    def studentIds(self):
        return self.__studentIds

    #Function: dumpData
    #Purpose: Saves masterStudentList to StudentInfo.dat
    #Parameters: None
    #Return: None
        '''Saves masterStudentList to StudentInfo.dat'''
    def dumpData(self):
        with open("StudentInfo.dat", "wb") as studentInfo:
            pickle.dump(self.__masterStudentList, studentInfo)
            pickle.dump(self.__studentIds, studentInfo)

    #Function: loadData
    #Purpose: Loads masterStudentList from StudentInfo.dat into __masterStudentList
    #Parameters: None
    #Return: None
    '''loads data from StudentInfo.dat into masterStudentList'''
    def loadData(self):

        #Create data file if it doesn't yet exist
        if not(os.path.exists("StudentInfo.dat")):
            studentInfo=open("StudentInfo.dat", "wb")
        
        #Load data to studentList and gradesList
        else:
            with open("StudentInfo.dat", "rb") as studentInfo:
                self.__masterStudentList=pickle.load(studentInfo)
                self.__studentIds=pickle.load(studentInfo)

    #Function: addStudent
    #Purpose: Creates and adds a student object with a student ID to this roster
    #Parameters: student (Student)
    #Return: none
    '''creates and adds a student object to this roster'''
    def addStudent(self, name):
        newNum=True
        while newNum==True:

            #Generates random student ID
            num=random.randint(1000, 9999)
            index=0
            numFound=False
            while index<len(self.__studentIds) and numFound==False:
                if self.__studentIds[index]==num:
                    numFound=True
                index+=1
            if numFound==False:
                newNum=False
        self.__studentIds.append(num)

        #Creates new student object and adds to masterStudentList
        newStudent=studentClassOO.Student(name, num)                            
        self.__masterStudentList.append(newStudent)

    #Function: addStudentsFromFile
    #Purpose: Creates new student objects, each with a name from the administrator's text file, and appends each object to masterStudentList
    #Parameters: none
    #Return: none
    '''adds students to roster based on names in admin's text file'''
    def addStudentsFromFile(self):

        fileExists=False
        while not fileExists:
            try:
                #Load names into adminStudentList variable
                adminFileName=input("\nEnter the name of your file (ending in .txt):\n\n")
                adminFile=open(adminFileName,"r")
                adminStudentList=[line.strip() for line in adminFile]
                adminFile.close()
                fileExists=True

                #Adds all students who are not yet registered to masterStudentList
                count=0
                for student in adminStudentList:
                    student=student.lower()
                    if not self.isStudentRegistered(student):
                        self.addStudent(student)
                
                #Ouput to user
                    else:
                        print("\n"+student+" is already registered and will not be added from "+adminFileName+"\n")
                        count+=1
                if count==0:
                    print("\nAll students were added from "+ adminFileName+"\n")

            except:
                print("\nThat file doesn't exist.")

    #Function: isStudentRegistered
    #Purpose: Checks if this roster has a student with the name sent as a parameter.
    #Parameters: name (string)
    #Return: found (boolean)
    """ensures name is in studentList"""
    def isStudentRegistered(self, name):
        found=False
        for student in self.__masterStudentList:

            #name is found
            if student.studentName==name or student.studentName.lower()==name:
                found=True
            
        return found

    #Function: findStudent
    #Purpose: Returns the index of a student in masterStudentList. Returns -1 if the student wasn't found.
    #Parameters: name (string)
    #Return: index (int)
    '''returns index of student in masterStudentList'''
    def findStudent(self, name):
        name=name.lower()
        index=-1
        for index in range (len(self.__masterStudentList)):
            if self.__masterStudentList[index].studentName==name:
                break
        return index

    #Function: isEmpty
    #Purpose: Returns True if there are no student objects in masterStudentList
    #Parameters: none
    #Return: boolean
    '''returns True if there are no students registered on this roster'''
    def isEmpty(self):
        if not self.__masterStudentList:
            return True
        return False

    #Function: printRoster
    #Purpose: Prints all students' courses and grades
    #Parameters: none
    #Return: none
    def printRoster(self):
        for student in self.__masterStudentList:
            student.printStudent()

            
        

        
            


