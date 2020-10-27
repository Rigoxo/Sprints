###Rigoberto Diaz###
#This program is basically a math study application, The user will select a specific subject in math and the program will send the users question till the user masters the subject.#
#The user masters a subject once they get at least 7 question right without hitting the limit of wrongs, the user only has 3 freebies before the whole progress is reseted#
###Citations###
import math
import random

def main():
    userName = input("Please enter your name to begin: ")
    print("Hello " + userName + " Welcome to GURU\nThis program will help you improve your skills in math in no time.")
    subjectSelection(userName)
   

def subjectSelection(userName):
     print("Please pick a subject in math you'd like to work on: ")
     subjectArray = ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Multiplication by exponents', 'Even or Odd', 'Between the numbers'] #This Array will carry all of the subjects that the user can be tested on#
 #This for function lists off all of the subjects for the user#
     for x in range(7):
        print(str(x + 1) + '. ' + str(subjectArray[x]))  #The + string operator concatenates two strings together#
     subjectChoice = int(input())
 #These if statements lead the user to different defined functions that will test the user until mastery#
     if(subjectChoice == 1): #The relational operators == checks if the two variables are equal and if so, the condition becomes true#
        print("You chose addition!")
        addition(userName)
     elif(subjectChoice == 2):
        print("You chose subtraction!")
        subtraction(userName)
     elif(subjectChoice == 3):
        print("You chose multiplication!")
        multiplication(userName)
     elif(subjectChoice == 4):
        print("You chose division!")
        print("This suject can include decimals, Please round to the nearest hundredth.")
        division(userName)
     elif(subjectChoice == 5):
        print("You chose multiplication by exponents!")
        mbe(userName)
     elif(subjectChoice == 6):
        print("You chose Even or Odd!")
        print("This suject will ask you if the given number is even or odd.")
        eoo(userName)
     elif(subjectChoice == 7):
        print("You chose Between the numbers!")
        print("This suject will ask you to give a number between the given numbers")
        btn(userName)
    
#This function will task the user to answer addition problems till mastery#
def addition(userName):
    wrongs = 0
    for progression in range(10):
        var1 = random.randint(1,100)
        var2 = random.randint(1,100)
        sumOfEquation = var1 + var2
        print("Question " + str(progression + 1) + ": " + str(var1) + " + " + str(var2) + " = ?") #The + numeric operator adds two variables together getting the sum#
        userAnswer = int(input("Answer: "))
        if(sumOfEquation == userAnswer):
            print("Good job!")
        else:
            wrongs = wrongs + 1 #everytime the user gets the answer wrong, the number goes up by 1 till it resets back to 0 if it hits 3#
            print('incorrect, strike #' + str(wrongs))
            if(wrongs == 3): #this resets the progress by stopping the for loop and calling the function again#
                print("Progression reseted")
                addition(userName)   
    print("Congratulations " + userName + " you have mastered this subject\nReturning to Suject Selection...")
    subjectSelection(userName)
#This function will task the user to answer subtraction problems till mastery#
def subtraction(userName):
    wrongs = 0
    for progression in range(10):
        var1 = random.randint(1,100)
        var2 = random.randint(1,100)
        sumOfEquation = var1 - var2
        print("Question " + str(progression + 1) + ": " + str(var1) + " - " + str(var2) + " = ?") #The - numeric operator subtracts the second variable from the first variable#
        userAnswer = int(input("Answer: "))
        if(sumOfEquation == userAnswer):
            print("Good job!")
        else:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if(wrongs == 3):
                print("Progression reseted")
                subtraction(userName)   
    print("Congratulations " + userName + " you have mastered this subject\nReturning to Suject Selection...")
    subjectSelection(userName)
#This function will task the user to answer multiplication problems till mastery#
def multiplication(userName):
    wrongs = 0
    for progression in range(10):
        var1 = random.randint(1,100)
        var2 = random.randint(1,100)
        sumOfEquation = var1 * var2
        print("Question " + str(progression + 1) + ": " + str(var1) + " * " + str(var2) + " = ?") #The * numeric operator multiples both of the variables#
        userAnswer = int(input("Answer: "))
        if(sumOfEquation == userAnswer):
            print("Good job!")
        else:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if(wrongs == 3):
                print("Progression reseted")
                multiplication(userName)   
    print("Congratulations " + userName + " you have mastered this subject\nReturning to Suject Selection...")
    subjectSelection(userName)
#This function will task the user to answer division problems till mastery#
def division(userName):
    wrongs = 0
    for progression in range(10):
        var1 = random.randint(1,100)
        var2 = random.randint(1,100)
        sumOfEquation = round((var1 / var2),2) #This rounding function will round the number to the hundredth decimal#
        print("Question " + str(progression + 1) + ": " + str(var1) + " / " + str(var2) + " = ?") #The / numeric operator divides the first variable by the second variable#
        userAnswer = float(input("Answer: "))
        if(sumOfEquation == userAnswer):
            print("Good job!")
        else:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if(wrongs == 3):
                print("Progression reseted")
                division(userName)   
    print("Congratulations " + userName + " you have mastered this subject\nReturning to Suject Selection...")
    subjectSelection(userName)
#This function will task the user to answer multiplication by exponents till mastery#
def mbe(userName):
    wrongs = 0
    for progression in range(10):
        var1 = random.randint(1,12)
        var2 = random.randint(2,3)
        sumOfEquation = (var1 ** var2) 
        print("Question " + str(progression + 1) + ": " + str(var1) + " to the power of " + str(var2) + " = ?") #The ** numeric operator multiplies the first variable number to the power of the second variable#
        userAnswer = int(input("Answer: "))
        if(sumOfEquation == userAnswer):
            print("Good job!")
        else:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if(wrongs == 3):
                print("Progression reseted")
                mbe(userName)  
    print("Congratulations " + userName + " you have mastered this subject\nReturning to Suject Selection...")
    subjectSelection(userName)
#This function will ask the user if the given number is even or odd till mastery#
def eoo(userName):
    wrongs = 0
    for progression in range(10):
        var1 = random.randint(1,1000)
        if(var1 % 2 != 0): #The numeric operator % divides the first variable by the second variable and returns the remainder#
            #The relational operators != checks if the values of both sides are equal, and if not equal, it'll return as true#
            sumOfEquation = 'odd'
        else:
            sumOfEquation = 'even'
        print("Question " + str(progression + 1) + ": Is " + str(var1) + " even or odd?") #The ** numeric operator multiplies the first variable number to the power of the second variable#
        userAnswer = input("Answer: ")
        if(sumOfEquation == userAnswer):
            print("Good job!")
        else:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if(wrongs == 3):
                print("Progression reseted")
                mbe(userName)  
    print("Congratulations " + userName + " you have mastered this subject\nReturning to Suject Selection...")
    subjectSelection(userName)
#This function will ask the user if the given number is even or odd till mastery#
def btn(userName):
    wrongs = 0
    for progression in range(10):
        var1 = random.randint(1,500)
        var2 = random.randint(1,500)
        while var2 > var1:
            var2 = random.randint(1,500)
        print("Question " + str(progression + 1) + ": Enter a number that's greater than " + str(var2) + " and less than " + str(var1)) #The ** numeric operator multiplies the first variable number to the power of the second variable#
        userAnswer = int(input("Answer: "))
        if(userAnswer <= var1 and userAnswer >=var2): #This checks if the number given by the user is actually between both of them
            print("Good job!")
        else:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if(wrongs == 3):
                print("Progression reseted")
                btn(userName)  
    print("Congratulations " + userName + " you have mastered this subject\nReturning to Suject Selection...")
    subjectSelection(userName)
#This starts the program calling the main function#
main()