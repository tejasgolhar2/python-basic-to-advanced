import os


def up_one_directory_level():
    os.chdir("../")             # shift the directory to one level above the mentioned


def original_directory_level():
    os.chdir(r"E:\\Code Material\\python-basic-to-advanced\\Course Concepts\\11. Files and Directories\\1. OS Module")             # shift to the absolute path of the project


def printWorkingDirectory():
    path = os.getcwd()
    print("Current Working Directory: ",path)



printWorkingDirectory()

up_one_directory_level()        # changes cwd to folder parent to the present
printWorkingDirectory()


original_directory_level()        # changes cwd to the base directory of project -- User defined folder
printWorkingDirectory()