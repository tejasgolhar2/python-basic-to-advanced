import os

def printWorkingDirectory():
    path = os.getcwd()                          # returns --> String
    print("Current Working Directory: ",path)


# Function returns the path of currently working directory

printWorkingDirectory()