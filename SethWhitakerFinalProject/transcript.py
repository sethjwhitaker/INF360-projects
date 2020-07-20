# transcript.py

# This module contains the transcript class as well as
# related functions and classes

import logging
logger = logging.getLogger("transcript")

# ---- Transcript Class --------------------------------------------------------------------------------------------
class Transcript:

    # list to hold all of the year objects
    years = []


    def __init__(self):
        self.years = []
        logging.debug("Transcript object successfully created")
        

    # ---- addGrade Method ----------------------------------------------------------------
    # Adds course info to term in transcript object
    def addGrade(self, yearNum, term, courseName, hours, grade):
        
        logging.debug("addGrade method called")

        yearObj = None
        # Search for yearNum in years list
        for y in self.years:
            if y.year == yearNum:
                logging.debug("Year " + str(yearNum) + " was found in transcript")
                yearObj = y
                break

        # If year does not exist, create new year and add it to transcript
        if yearObj is None:
            logging.debug("Year " + str(yearNum) + " was not found in transcript")
            logging.debug("Creating year " + str(yearNum))
            yearObj = Year(yearNum)
            self.years.append(yearObj)
       
        # Add course to year
        yearObj.addGrade(term, courseName, hours, grade)

        logging.debug("Grade successfully added")
    # ---- end addGrade --------------------------------------------------------------------



    # ---- print function ------------------------------------------------------------------
    # Display transcript in the following format:
    # 
    # -------------------------------------------
    #     Year
    # -------------------------------------------
    # | Spring      | Summer      | Fall        |
    # | ClassName G | ClassName G | ClassName G |
    # | ClassName G | ClassName G | ClassName G |
    # | ClassName G |             | ClassName G |
    # | GPA    0.00 | GPA    0.00 | GPA    0.00 |
    #
    #  Overall 0.00
    # -------------------------------------------
    #     Year
    # -------------------------------------------
    # | Spring      | Summer      | Fall        |
    # | ClassName G | ClassName G |             |
    # | ClassName G | ClassName G |             |
    # | ClassName G |             |             |
    # | GPA    0.00 | GPA    0.00 |             |
    # 
    # Overall 0.00
    # -------------------------------------------
    #
    # Cumulative GPA 0.00
    #
    def print(self):
        # for cumulative gpa
        totalCourses = []

        # output new line
        print()

        # iterate through all years in transcriptObj sorted chronologically
        for year in sorted(self.years):

            # output header
            # -------------------------------------------
            #     Year
            # -------------------------------------------
            print("-"*49)
            print("    " + str(year.year))
            print("-"*49)
        
            # length of each course row (used for whitespace)
            rowLength = 14

            # Output term names
            # | Spring      | Summer      | Fall        |
            print("|", end = " ")
            for term in year.terms:
                print(term + " "*(rowLength-len(term)), end = "| ")
            print()

            # Output courses
            # | ClassName G | ClassName G | ClassName G |
            # | ClassName G | ClassName G | ClassName G |
            # | ClassName G |             | ClassName G |

            # find longest term (used to find num of rows in term)
            maxNumRows = len(year.terms["Spring"])
            if len(year.terms["Summer"]) > maxNumRows: maxNumRows = len(year.terms["Summer"])
            if len(year.terms["Fall"]) > maxNumRows: maxNumRows = len(year.terms["Fall"])

            # Because the course lists are being output vertically, I used a technique similar to Project 3
            # Iterate through num of rows (rows)
            for i in range(0, maxNumRows):
                print("|", end = " ")
                # Go through each term for each row (columns)
                for term in year.terms:
                    # make sure to keep index in range
                    if len(year.terms[term]) > i:
                        # output course info if in range
                        currentCourse = year.terms[term][i]
                        print(currentCourse.courseName + " "*(rowLength-len(currentCourse.courseName)-2) + currentCourse.grade, end = " | ")
                    else:
                        # otherwise print "blank" line
                        print(" "*rowLength, end = "| ")
                print()

            # Output gpa
            # | GPA    0.00 | GPA    0.00 | GPA    0.00 |
            #
            #  Overall 0.00

            # for gpa calc
            yearCourses = []

            print("|", end = " ")
            # go through terms
            for term in year.terms:
                # add courses to yearly courses (for gpa calc)
                yearCourses.extend(year.terms[term])

                if len(year.terms[term]) > 0:
                    # print gpa for current term if more than one course
                    print("GPA" + " "*(rowLength-8) + "%3.2f"% (calculateGPA(year.terms[term])), end = " | ")
                else:
                    # blank line if 0 courses in term
                    print(" "*rowLength, end = "| ")
            print("\n")
        
            # print year gpa
            print(" Overall " + "%3.2f"% (calculateGPA(yearCourses)))

            # add year to total
            totalCourses.extend(yearCourses)

        print("-"*49 + "\n")
        print(" Cumulative GPA " + "%3.2f"% (calculateGPA(totalCourses)) + "\n")
    # ----- end print ----------------------------------------------------------------------------------------------

# ---- end Transcript ----------------------------------------------------------------------------------------------


# ---- Course Class ------------------------------------------------------------------------------------------------
# course class that holds basic course info
class Course:

    courseName = "INF 360"
    creditHours = 3
    grade = "A"
    
    def __init__(self, courseName, creditHours, grade):
        self.courseName = courseName
        self.creditHours = creditHours
        self.grade = grade
        logging.debug("Course " + courseName + " successfully created")

# ---- end Course --------------------------------------------------------------------------------------------------


# ---- Year Class --------------------------------------------------------------------------------------------------
# year class that holds term lists
class Year:

    year = 2020

    terms = {}

    def __init__(self, year):
        self.terms = {
            "Spring": [],
            "Summer": [],
            "Fall": []
        }
        self.year = year
        logging.debug("Year " + str(year) + " successfully created")

    # overload < for sorting
    def __lt__(self, other):
        if self.year < other.year:
            return True
        else:
            return False

    def addGrade(self, termName, courseName, hours, grade): 
        term = self.terms[termName]
        # create new course
        course = Course(courseName, hours, grade)
        # add course to term
        term.append(course)

# ---- end Year ----------------------------------------------------------------------------------------------------


# ---- gradeValue Function -----------------------------------------------------------------------------------------
#
# returns the value of each letter grade in points
def gradeValue(letter):

    if   letter == "A": return 4
    elif letter == "B": return 3
    elif letter == "C": return 2
    elif letter == "D": return 1
    else:               return 0

# ---- end gradeValue ------------------------------------------------------------------------------------------------


# ---- calculateGPA function -----------------------------------------------------------------------------------------
#
# takes in a list of courses and returns a grade point average
#
def calculateGPA(courses):
    # total number of credit hours
    totalHours = 0
    # total points earned 
    pointsEarned = 0

    # go through list 
    for course in courses:
        # add hours of each course
        totalHours += course.creditHours
        # add points earned from each course
        pointsEarned += gradeValue(course.grade) * course.creditHours

    # make sure not to divide by 0
    if totalHours == 0:
        logging.warning("Tried to calculate gpa with 0 total credit hours!")
        return 0
    else:
        # calculate gpa
        return pointsEarned / totalHours

# ---- end calculateGPA ---------------------------------------------------------------------------------------------