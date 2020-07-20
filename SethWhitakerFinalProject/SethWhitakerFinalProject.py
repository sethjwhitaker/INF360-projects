# INF360 - Programming in Python
# Seth Whitaker
# Final Project
# Transcript Manager
# 07/18/2020

# Goals of this project:
# 1. Get course information as input from user
# 2. Store info in nested dictionary
# 3. Display data to console in a well formatted way



import logging
import sys

# Configure logging
logging.basicConfig(filename="SWFinalProjectLog.txt", level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


try:
    # transcript module that holds transcript class and related functions
    import transcript
except:
    logging.critical("Could not find file: transcript.py")
    print("Could not find file: transcript.py!\nClosing Program")
    sys.exit()

# ---- main function -------------------------------------------------------------------------------------------
def main():

    logging.debug("Main function called")

    # this is the object that will hold all of the data
    transcriptObj = transcript.Transcript()

    # display menu and call appropriate function based on user input
    while True:
        # display menu
        choice = menuPrompt()

        logging.debug("User entered: " + choice)

        # exit loop if user chooses 0
        if choice == "0":
            break
        # if 1, prompt user for grade info and store in transcript object
        elif choice == "1":
            enterGrades(transcriptObj)
        # if 2, print the transcript to the console
        elif choice == "2":
            transcriptObj.print()
        else:
            logging.debug("Invalid choice by user")
            print("Invalid choice. Please try again.")


# ---- end main ------------------------------------------------------------------------------------------------




# ---- menuPrompt function -------------------------------------------------------------------------------------
# displays menu prompt and returns user's choice
def menuPrompt():
    print("-"*27)
    print(" "*11 + "MENU")
    print("-"*27)
    print("1. Enter Transcript Grades")
    print("2. View Full Transcript")
    print("0. Quit")

    logging.debug("Menu displayed")

    return input("\nPlease choose an option: ")
# ---- end menuPrompt ------------------------------------------------------------------------------------------



# ---- enterGrades function ------------------------------------------------------------------------------
#
# handles user input for entering course information
#
# Prompt format:
# Class Name (INF 360): 
# Grade Earned (A): 
# Year (2020):
# Term (Summer):
# Credit Hours (3):
#
def enterGrades(transcriptObj):

    logging.debug("Enter grades function called")

    print("\nEnter course info")
    
    # input variables
    className = ""
    grade = ""
    year = 0
    term = ""
    hours = 0

    while True:

        logging.debug("Get class name from user")

        # get course name info from user
        className = input("Class Name (INF 360): ")

        # make sure length is 11 or less
        if len(className) >= 12:
            logging.debug("User entered a class name that was longer than 11 characters.")
            print("Class Name is too long. Max length is 11 characters.")
        else:
            logging.debug("User entered valid class name")
            break

    while True:

        logging.debug("Get grade from user")

        # get grade from user
        grade = input("Grade Earned (A): ").upper()

        # validate input
        if grade != "A" and grade != "B" and grade != "C" and grade != "D" and grade != "F":
            logging.debug("User entered invalid grade")
            print("Please enter a valid letter grade. (A, B, C, D, F)")
        else:
            logging.debug("User entered valid grade")
            break
        
    
    while True:

        logging.debug("Get year from user")

        # get year from user
        # make sure year is an int
        try: 
             year = int(input("Year (2020): "))
        except: 
            # if error is thrown, repeat loop
            logging.debug("User entered invalid year")

            print("Please enter an integer number of years")
            continue
        # if no error is thrown, exit loop
        logging.debug("User entered valid year")
        break
    


    while True:

        logging.debug("Get term from user")

        # get term from user
        term = input("Term (Summer): ").lower()
        # allow user to enter 1, 2, or 3 for term
        if term == "1":
            term = "spring"
        elif term == "2":
            term = "summer"
        elif term == "3":
            term = "fall"
        # validate input
        if term != "summer" and term != "spring" and term != "fall":
            logging.debug("User entered invalid term")
            print("Please enter a valid term. (Spring, Summer, Fall)")
        else:
            logging.debug("User entered valid term")
            break

    # Capitalize first letter of term
    term = term[0].upper() + term[1:len(term)]

    
    while True:

        logging.debug("Get credit hours from user")
        # get hours from user
        # make sure hours is an int (required for gpa calculations)
        try: 
            hours = int(input("Credit Hours (3): "))
        except: 
            # if error is thrown, repeat loop
            logging.debug("User entered invalid hours")
            print("Please enter an integer number of credit hours")
            continue
        # if no error is thrown, exit loop
        logging.debug("User entered valid hours")
        break

    logging.debug("All grade info successfully entered by user")

    # add grade to transcriptObj
    transcriptObj.addGrade(year, term, className, hours, grade)

# ---- end enterGrades ------------------------------------------------------------------------



# call main
main()