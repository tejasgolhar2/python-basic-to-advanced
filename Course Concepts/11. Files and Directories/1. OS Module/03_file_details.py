import os

def getMetaData():
    entries = os.scandir()
    for entry in entries:
        data = entry.stat()             # Use of stat function -- Metadata about the entry
        print(data)

def displayWorkingDirectory():
    path = os.getcwd()
    print("Current Working Directory: ",path)

def oneLevelUp():
    os.chdir("../")


displayWorkingDirectory()
oneLevelUp()
print()
displayWorkingDirectory()
print()
getMetaData()



