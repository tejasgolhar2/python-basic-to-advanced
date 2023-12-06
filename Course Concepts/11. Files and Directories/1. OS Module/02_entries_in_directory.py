import os


def up_one_directory_level():
    os.chdir("../")             # returns --> None


def printWorkingDirectory():        
    path = os.getcwd()          # returns --> String
    print("Current Working Directory: ",path)


def elements_in_directory():        # Get all the entries present in the Current Working Directory
    items = os.scandir()            # returns --> Iterator

    for element in items:
        print(element.name)


printWorkingDirectory()

up_one_directory_level()        # changes cwd to folder parent to the present
printWorkingDirectory()


elements_in_directory()

'''
NOTE:
1. Likewise, we can use os.list() method 

'''
