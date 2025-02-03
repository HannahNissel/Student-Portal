#Chana Leah Nissel
#Main
#Drives Roster, Student, and Course classes

import rosterClassOO
import studentClassOO
import courseClassOO
import os
import pickle

#Function: checkForYes
#Purpose: If the value of yesOrNo is not "yes", asks the user for a new value
#Parameters:yesOrNo (string)
#Return: yesOrNo (string)
'''checks if value of yesOrNo is "yes"'''
def checkForYes(yesOrNo):
    while yesOrNo!="yes" and yesOrNo!="no":
        yesOrNo=input("Sorry, that was not one of the options. Please type \"yes\" or \"no\".")
    return yesOrNo

#Function: checkNum
#Purpose: If the value of parameter #1 is not the same as parameter #2 or parameter #3, asks user for a new value
#Parameters: userNum (string), num1 (string), num2 (string)
#Return: number (string)
"""checks if value of parameter #1 is same as parameter #2 or parameter #3"""
def checkNum(userNum, num1, num2):
    while userNum!=num1 and userNum!=num2:
        userNum=input("Sorry, that was not one of the options. Press "+num1+" or "+num2+".\n")
    return userNum

#Function: isValidGrade
#Purpose: checks if letterGrade is one of the following: "A" , "B" , "C" , "D" , "F". If not, gets a new grade from user.
#Parameters: letterGrade (string)
#Returns: letterGrade (string)
def isValidGrade(letterGrade):
    letterGrade=letterGrade.lower()
    while letterGrade!="a" and letterGrade!="b" and letterGrade!="c" and letterGrade!="d" and letterGrade!="f":
        letterGrade=input("That grade is not part of the letter grading system. Please enter one of the following: A, B, C, D, F\n")
        letterGrade=letterGrade.lower()
    return letterGrade

def main():
    roster=rosterClassOO.Roster
    course=courseClassOO.Course
    student=studentClassOO.Student

    #Changes current directory to where this python file is
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    #Initial load (of data)
    roster1=roster([])                                       
    roster1.loadData()
                              
    backToMenu=True
    while backToMenu:
        
        #Main Menu
        menuChoice=input("Hello, please enter a number corresponding to one of the following options:\n1) Add a student\n2) Manage a student's courses and grades\n3) Look up a student's courses and grades\n4) List all students' grades \n5) Create report card \n6) Create transcript\n7) Quit\n\n")
        while menuChoice!="1" and menuChoice!="2" and menuChoice!="3" and menuChoice!="4" and menuChoice!="5" and menuChoice!="6" and menuChoice!="7":
            menuChoice=input("That was not one of the options. Please enter a number 1-7\n\n")

        #**********************main menu option 1************************
        #User can add students
        if menuChoice=="1":
            readText=input("\nDo you want to load a list of student names from a text file?\n\n") 
            readText=readText.lower()
            print("\n")
            readText=checkForYes(readText)

            #Reads student's names from administrator's text file
            if readText=="yes":
                roster1.addStudentsFromFile()
            
            else:
                again=True
                while again:
                    #Add student name
                    name=input("Enter student's name:\n")
                    roster1.addStudent(name)

                    #Option to add another name or return to main menu
                    hasAnotherName=input("\nPress 1 to add another name or 0 to go back to the main menu. \n")
                    hasAnotherName=checkNum(hasAnotherName, "1", "0")
                    if hasAnotherName=="0":
                        again=False
                

        if menuChoice=="2" or menuChoice=="3":
            newStudent=True
            while newStudent:

                #Finds student (For options 2 and 3)
                studentName=input("\nEnter student's name: \n\n")
                studentName=studentName.lower()
                if studentName!="5":
                    isRegistered=roster1.isStudentRegistered(studentName)
                    while not isRegistered:
                        studentName=input("That student is not registered. Please enter a different name: \n").lower()
                        isRegistered=roster1.isStudentRegistered(studentName)     
                else:

                    #Quit student lookup
                    break

                studentIndex=roster1.findStudent(studentName) 
                thisStudent=roster1.masterStudentList[studentIndex]

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
                            semester=input("\nEnter the semester: \n")

                            #Checks if student is already registered for that course
                            while thisStudent.isRegisteredForCourse(subject, semester):
                                subject=(input(studentName.title()+" is already registered for that course. Please choose a different one:\n")).lower()
                                semester=input("\nEnter the semester: \n")

                            #Gets grade from user
                            grade=input("\nEnter "+studentName.title()+"'s letter grade for "+subject.title()+":\n")
                            grade=grade.lower()
                            grade=isValidGrade(grade)

                            thisStudent.addCourse(subject, semester, grade) 
                            print("\n"+subject.title()+" "+semester+" was added to "+studentName.title()+"'s record.")
                        
                        #Change grade of current course
                        else:
                            
                            if not thisStudent.hasCourses():
                                print("\n"+thisStudent.studentName.title()+" is not registered for any courses.\n")

                            else:
                                #Makes sure the subject matches one of the subjects that the student is registered for
                                subject=input("\nChoose a course to update:\n")
                                subject=subject.lower()
                                semester=input("\nEnter the semester: \n").lower()
                                while not thisStudent.isRegisteredForCourse(subject, semester):
                                    subject=(input(studentName.title()+" is not registered for that course. Please choose a different one:\n")).lower()
                                    semester=input("\nEnter the semester:\n").lower()

                                #Gets grade from user
                                newGrade=input("\nEnter "+studentName.title()+"'s letter grade for "+subject.title()+":\n")
                                newGrade=newGrade.lower()
                                newGrade=isValidGrade(newGrade)

                                #Updates grade
                                courseIndex=thisStudent.findCourse(subject, semester)                  
                                thisStudent.courses[courseIndex].grade=newGrade

                        #Options: 1)Add another course and grade for that student 2)Add course and grade for different student 3)Menu
                        again=input("\nPress 1 to manage another one of "+studentName.title()+"'s grades.\nPress 2 to manage a different student's grades.\nPress 3 to go back to the main menu.\n\n")
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
                    if not thisStudent.hasCourses():
                        print("\n"+studentName+" is not registered for any courses.\n\n")
                        newStudent=False
                        break

                    else:
                        inSubject=input("\nEnter a course name:\n\n")
                        inSubject=inSubject.lower()
                        semester=input("\nEnter the semester:\n").lower()

                        #Checks if input matches one of that student's courses
                        while not thisStudent.isRegisteredForCourse(inSubject, semester):
                                inSubject=(input(studentName.title()+" is not registered for that course. Please choose a different one:\n")).lower()
                                semester=input("\nEnter the semester:\n").lower()
                            
                        #Prints student's grade in that course
                        print("\n"+studentName.title()+"'s grade:\n")
                        courseIndex=thisStudent.findCourse(inSubject, semester)
                        roster1.masterStudentList[studentIndex].courses[courseIndex].printCourse()

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

            #If there are no students registerd                  
            if roster1.isEmpty():
                print("There are no students registered.\n")

            #Prints students' courses and grades
            else:
                roster1.printRoster()
            quit=input("Press 1 to quit.\nPress 0 to return to the main menu.\n")
            quit=checkNum(quit, "1", "0")
            
            #User wants to quit
            if quit=="1":
                backToMenu=False
                print("Have a gread day!")

            #User wants to return to menu
            else:
                newStudent=False

        #*******************main menu option 5***********************
        #Writes a semester report card for a specific student
        if menuChoice=="5":
            studentName=input("Enter a student's name: \n").lower()
            isRegistered=roster1.isStudentRegistered(studentName)

            #Ensures that student is registered
            while not isRegistered:
                studentName=input("That student is not registered. Please enter a different name: \n").lower()
                isRegistered=roster1.isStudentRegistered(studentName)     
            index=roster1.findStudent(studentName)

            semester=input("\nEnter a semester: ").lower()

            #Ensures student is registered for that semester
            while not roster1.masterStudentList[index].isRegisteredForSemester(semester):
                semester=input(roster1.masterStudentList[index].studentName+" is not registered for "+semester+" semester. Please enter a different semester: \n")

            #Calls function to write report card
            roster1.masterStudentList[index].writeReportCard(semester)
            print()
            print(roster1.masterStudentList[index].studentName.title()+"'s report card was created.\n")

        #*******************main menu option 6***********************
        #Writes a transcript for a specific student
        if menuChoice=="6":
            studentName=input("Enter a student's name: \n").lower()

            #Esures that student is registered
            isRegistered=roster1.isStudentRegistered(studentName)
            while not isRegistered:
                studentName=input("That student is not registered. Please enter a different name: \n").lower()
                isRegistered=roster1.isStudentRegistered(studentName)   
            index=roster1.findStudent(studentName)

            #Calls function to write transcript
            roster1.masterStudentList[index].writeTranscript()
            print()
            print(roster1.masterStudentList[index].studentName.title()+"'s transcript was created.\n")

        #*******************main menu option 7************************
        #Quit
        if menuChoice=="7":
            newStudent=False
            backToMenu=False
            print("Have a great day!")
    roster1.dumpData()

main()