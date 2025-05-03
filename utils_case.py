"""
File: utils_case.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Advanced: This version requires a working .venv with loguru and pyttsx3 installed.
It includes a function to read the byline aloud using pyttsx3.

Author: Denise Case
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# Learn more: https://docs.python.org/3/library/

import statistics 

# Import packages from requirements.txt
# Learn more: https://pypi.org/project/loguru/ 
# Learn more:  https://pypi.org/project/pyttsx3/
import loguru   # Easy logging
import pyttsx3  # Text-to-speech engine

#####################################
# Configure Logger and Verify
#####################################

# Assign loguru.logger object to a local variable named `logger` to improve readability.
logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Module loaded.")

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
has_international_clients: bool = True

# declare an integer variable 
years_in_operation: int = 10

# declare a floating point variable
average_client_satisfaction: float = 4.7

# declare a list of strings
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# declare a list of numbers so we can illustrate statistics skills
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Calculate basic statistics using built-in Python functions and the statistics module
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score: {mean_score:.2f}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''
    return byline


# Read the byline aloud (requires pyttsx3)

def read_byline_aloud():
    engine = pyttsx3.init()
    engine.say(get_byline())
    engine.runAndWait()


#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_case.py")
    loguru.logger.info("START main() in utils_case.py")

    print(get_byline())
    loguru.logger.info("Byline:\n" + get_byline())

    read_byline_aloud()

    print("END main() in utils_case.py")
    loguru.logger.info("END main() in utils_case.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()
