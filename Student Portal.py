#Student Portal
#Allows the user to add students and look up or change students' courses and grades
#Developer: Chana Leah Nissel
#Last Updated: 11/24/2024

import os
import pickle

#Function: loadData
#Purpose: Loads studentList and gradesList with most recent data from StudentInfo.dat
#Parameters: None
#Return: None
'''loads data from StudentInfo.dat into studentList and gradesList'''
def loadData():
    global studentList
    global gradesList

    #Create data file if it doesn't yet exist
    if not(os.path.exists("StudentInfo.dat")):
        studentInfo=open("StudentInfo.dat", "wb")
    
    #Load data to studentList and gradesList
    else:
        with open("StudentInfo.dat", "rb") as studentInfo:
            studentList=pickle.load(studentInfo)
            gradesList=pickle.load(studentInfo)

#Function: dumpData
#Purpose: Saves studentList and gradesList to StudentInfo.dat
#Parameters: None
#Return: None
'''Saves studentList and gradesList to StudentInfo.dat'''
def dumpData():
    with open("StudentInfo.dat", "wb") as studentInfo:
        pickle.dump(studentList, studentInfo)
        pickle.dump(gradesList, studentInfo)

#Function: addStudentName
#Purpose: appends studentName to studentList and appends empty dictioary to gradesList
#Parameters: None
#Return: None
"appends studentName to studentList"
def addStudent():
    global studentList
    
    #Gets name from user
    studentName=input("Enter student's name: \n")
    studentName=studentName.lower()
    
    if studentName not in studentList:

        #Appends to the global variables
        studentList.append(studentName)
        gradesList.append({})
    
    #If that student is already registered
    else:
        print(studentName +" is already registered.")

#Function: addStudentsFromFile
#Purpose: Reads student names from a text file provided by the user and adds all names that are not yet in student list (and adds corresponding amount of dictionaries to gradesList)
#Parameters: None
#Return: None
'''reads from user's text file, and adds names to studentList'''
def addStudentsFromFile():
    global studentList
    global gradesList

    fileExists=False
    while not fileExists:
        try:
            #Load names into adminStudentList variable
            adminFileName=input("\nEnter the name of your file (ending in .txt):\n\n")
            adminFile=open(adminFileName,"r")
            adminStudentList=[line.strip() for line in adminFile]
            adminFile.close()
            fileExists=True

            #Adds all students who are not yet in studentList to studentList
            count=0
            for student in adminStudentList:
                student=student.lower()
                if student not in studentList:
                    studentList=studentList+[student]
                    gradesList=gradesList+[{}]
            
            #Ouput to user
                else:
                    print("\n"+student+" is already registered and will not be added from "+adminFileName+"\n")
                    count+=1
            if count==0:
                print("\nAll students were added from "+ adminFileName+"\n")
            dumpData()
        except:
            print("\nThat file doesn't exist.")

#Function: checkNums
#Purpose: If the value of parameter #1 is not the same as parameter #2 or parameter #3, asks user for a new value
#Parameters: userNum (string), num1 (string), num2 (string)
#Return: number (string)
"""checks if value of parameter #1 is same as parameter #2 or parameter #3"""
def checkNum(userNum, num1, num2):
    while userNum!=num1 and userNum!=num2:
        userNum=input("Sorry, that was not one of the options. Press "+num1+" or "+num2+".\n")
    return userNum

#Function: checkForYes
#Purpose: If the value of yesOrNo is not "yes", asks the user for a new value
#Parameters:yesOrNo (string)
#Return: yesOrNo (string)
'''checks if value of yesOrNo is "yes"'''
def checkForYes(yesOrNo):
    while yesOrNo!="yes" and yesOrNo!="no":
        yesOrNo=input("Sorry, that was not one of the options. Please type \"yes\" or \"no\".")
    return yesOrNo

#Function: isStudentRegistered
#Purpose: Checks if name is in studentList. If not, asks user for a new name.
#Parameters: name (string)
#Return: name (string)
"""checks if name is in studentList"""
def isStudentRegistered(name):
    global studentInfo
    global studentList
    
    tryAgain=True
    while name not in studentList and tryAgain:
        name=input("That student is not registered. Please enter another name or press 5 to return to the main menu.\n")
        name=name.lower()
        if name=="5":
            tryAgain=False
    return name
    
#Function: printCourseOptions
#Purpose: interates through courses and prints each course 
#Parameters: courses (list)
#Return: None
"""prints course options"""
def printCourseOptions(courses):
    print("Courses offered: \n")
    for course in courses:
        print(course.title())

#Function: isRegisteredForCourse
#Purpose: Checks if student is already registered for that course. If not, get a new course name as input.
#Parameters: name (string), index (integer), course (string)
#Returns: course (string)
"""if this course is not in this student's dictionary, asks the user for a new course name"""
def isRegisteredForCourse(name, index, course):
    while course not in gradesList[index]:
        course=(input(name.title()+" is not registered for that course. Please choose a different one:\n")).lower()
    return course

#Function: isValidGrade
# Purpose: checks if letterGrade is one of the following: "A" , "B" , "C" , "D" , "F". If not, gets a new grade from user.
#Parameters: letterGrade (string)
#Returns: letterGrade (string)
"""makes sure letterGrade is A, B, C, D, or E"""
def isValidGrade(letterGrade):
    lettergrade=letterGrade.lower()
    while letterGrade!="a" and letterGrade!="b" and letterGrade!="c" and letterGrade!="d" and letterGrade!="f":
        letterGrade=input("That grade is not part of the letter grading system. Please enter one of the following: A, B, C, D, F\n")
        letterGrade=letterGrade.lower()
    return letterGrade

def main():
    global studentList
    global gradesList
    global studentInfo

    #Changes current directory to where this python file is
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    #Initial load (of data)
    loadData()

    backToMenu=True
    while backToMenu:
        
        #Main Menu
        menuChoice=input("Hello, please enter a number corresponding to one of the following options:\n1) Add a student\n2) Manage a student's courses and grades\n3) Look up a student's courses and grades\n4) List all students' grades\n5) Quit\n\n")
        while menuChoice!="1" and menuChoice!="2" and menuChoice!="3" and menuChoice!="4" and menuChoice!="5":
            menuChoice=input("That was not one of the options. Please enter 1, 2, 3, 4 or 5\n\n")

        #**********************main menu option 1************************
        #User can add students
        if menuChoice=="1":
            readText=input("\nDo you want to load a list of student names from a text file?\n\n") #LOCAL VARIABLE
            readText=readText.lower()
            print("\n")
            readText=checkForYes(readText)

            #Reads student's names from administrator's text file
            if readText=="yes":
                addStudentsFromFile()
            
            else:
                again=True
                while again:
                    #Add student name
                    addStudent()

                    #Option to add another name or return to main menu
                    hasAnotherName=input("\nPress 1 to add another name or 0 to go back to the main menu. \n")
                    hasAnotherName=checkNum(hasAnotherName, "1", "0")
                    if hasAnotherName=="0":
                        again=False
                dumpData()

        if menuChoice=="2" or menuChoice=="3":
            newStudent=True
            while newStudent:

                #Finds student (For options 2 and 3)
                studentName=input("\nEnter student's name: \n\n")
                studentName=studentName.lower()
                studentName=isStudentRegistered(studentName)     #WARNING: This method is written differently in Roster class than it is above

                #Quit studen lookup
                if studentName=="5":
                    break

                studentIndex=studentList.index(studentName)           

                #*********************main menu option 2***********************
                #Adds courses and grades to student record

                #Gets course name from user
                if menuChoice=="2":
                    sameStudent=True
                    while sameStudent:
                        
                        #Option to add a new course or change the grade of an existing course
                        addOrChange=input("\nEnter 1 to add a new course and grade.\nEnter 2 to change the grade of a current course.\n")
                        addOrChange=checkNum(addOrChange, "1","2")

                        #Add a new course
                        if addOrChange=="1":
                            subject=input("\nChoose a subject to add to "+studentName.title()+"'s record.\n")
                            
                            subject=subject.lower()

                            #Checks if student is already registered for that course
                            if subject in gradesList[studentIndex]:
                                subject=(input(studentName.title()+" is already registered for that course. Please choose a different one:\n")).lower()
                            
                        
                        #Change grade of current course
                        else:

                            #Makes sure the subject matches one of the subjects that the student is registered for
                            subject=input("\nChoose a course to update:\n")
                            subject=subject.lower()
                            subject=isRegisteredForCourse(studentName, studentIndex, subject)

                        #Gets grade from user
                        grade=input("\nEnter "+studentName.title()+"'s letter grade for "+subject.title()+":\n")
                        grade=grade.lower()
                        grade=isValidGrade(grade)

                        #Adds course and grade to student dictionary
                        gradesList[studentIndex][subject]=grade 
                        dumpData()

                        #Options: 1)Add another course and grade for that student 2)Add course and grade for different student 3)Menu
                        again=input("\n"+subject.title()+" was added to "+studentName.title()+"'s record.\nPress 1 to manage another one of "+studentName.title()+"'s grades.\nPress 2 to manage a different student's grades.\nPress 3 to go back to the main menu.\n\n")
                        while again!="1" and again!="2" and again!="3":
                            again=input("That was not one of the options. Please press 1, 2, or 3")
                        if again=="2" or again=="3":
                            sameStudent=False
                        if again=="3":
                            newStudent=False

                #************************main menu option 3**********************
                #User can look up a student's grade in a specific course
                option3Again=True
                while option3Again and menuChoice=="3":

                    #Notifies user if student is not registered for any courses and returns to menu
                    if not gradesList[studentIndex]:
                        print("\n"+studentName+" is not registered for any courses.\n")
                        newStudent=False
                        break

                    else:
                        inSubject=input("\nEnter a course name:\n\n")
                        inSubject=inSubject.lower()

                        #Checks if input matches one of that student's courses
                        inSubject=isRegisteredForCourse(studentName, studentIndex, inSubject)

                        #Prints student's grade
                        print("\n"+studentName.title()+"'s grade in "+inSubject.title()+" is:")
                        singleStudentsGrades=gradesList[studentIndex]
                        print(singleStudentsGrades[inSubject].upper())

                        #Options:Look up another grade or return to main menu
                        again=input("\nPress 1 to look up another one of "+studentName+"'s grades.\nPress 0 to return to the main menu\n")
                        again=checkNum(again, "1", "0")
                        if again=="0":
                            option3Again=False
                            newStudent=False

        #*******************main menu option 4***********************    
        #View all students' grades
        print(" ")
        if menuChoice=="4":

            #If there are no students registerd                     use isRosterEmpty
            if len(studentList)<1:
                print("There are no students registered.\n")

            #Prints students' courses and grades
            else:
                count=0
                while count<len(gradesList):

                    #Tells user if student isn't registered for any courses                 use hasCourses
                    if not gradesList[count]:
                        print(studentList[count].title()+" is not signed up for any courses.")

                    #Print all of that student's grades
                    else:
                        print(studentList[count].title()+"'s grades:")
                        for course in gradesList[count]:
                            print(course.title()+": "+gradesList[count][course].upper())
                    print()
                    count+=1
            quit=input("Press 1 to quit.\nPress 0 to return to the main menu.\n")
            quit=checkNum(quit, "1", "0")
            
            #User wants to quit
            if quit=="1":
                backToMenu=False
                print("Have a gread day!")

            #User wants to return to menu
            else:
                newStudent=False

        #*******************main menu option 5************************
        #Quit
        if menuChoice=="5":
            newStudent=False
            backToMenu=False
            print("Have a great day!")

studentInfo=0       ######################################################################################## WHICH CLASS SHOULD THIS GO IN?

#student names, course names, and letter grades are all stored in the lists in all lowercase
studentList=[]

#Each student has a dictionary within this list with his/her grades. 
# The name in studentList has the same index of that student's dictionary in gradesList.
gradesList=[]

main()

