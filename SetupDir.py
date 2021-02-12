import os

# Creates a directory for the subtitles to be placed in
def createDir():
    path = "./subs"
    if (not os.path.isdir(path)):
        try:
            os.mkdir(path)
        
        except OSError:
            print("Creation of the subs folder failed")
            return False

        else:
            print("Directory successfully created")
            return True

def createConfigFile():
    if (os.path.isfile("./user.txt")):
        # r+ will read the file if it already exists
        userCfg = open("user.txt","r+")
    else:
        # w+ will create a new file if it doesn't exist
        userCfg = open("user.txt", "w+")

    numLines = numLinesFile(userCfg.name)
    print("NUMLINES: ",numLines)
    if (numLines == 0):
        userCfg.write("MOVIE DIRECTORIES:\n")


    userCfg.close()


# Reads the directories present in user.txt
def readMovieDirectories():
    directoriesFile = open("user.txt","r+")
    numLines = numLinesFile(directoriesFile.name)
    if (numLines >= 2):
        # Ignore the first line
        directories = directoriesFile.read().split("\n")
        directories.pop(0)
        directoriesFile.close()
        return directories
    else:
        directoriesFile.close()
        return None
    

def numLinesFile(fileName):

    fileToRead = open(fileName,"r+")
    fileContent = fileToRead.read()
    listLines = fileContent.split("\n")
    numLines = 0
    for x in listLines:
        # split includes the empty char. We have to verify that the column isn't empty  
        if x != '':
            numLines += 1 

    return numLines
        