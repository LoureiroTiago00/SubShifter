from SetupDir import *
from Shift import *
import sys

print("Welcome to SubShifter\n")

createDir()
createConfigFile()

listDirectories = readMovieDirectories()

listSubs = []
for x in os.listdir("./subs"):
    if (x != '' and (str(x).endswith(".srt") or str(x).endswith(".txt"))):
        listSubs.append(x)

if (len(listSubs) >= 1):
    counter = 1
    for y in listSubs:
        print(str(counter) + " - " + y)
        counter += 1

    validChoice = False

    while (not validChoice):
        choice = input("Select a subtitle file to shift:\n")
        try:
            choice = int(choice)
            if (choice >= 1 and choice <= len(listSubs)):
                validChoice = True
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid choice")

        else:
            pass

    shiftedFile = shiftSub(listSubs[choice-1])
    print("Subtitles successfully shifted")
    print("\n")
    moveToDir = input("Would you like to apply the subtitles to a file present in one of your directories?[Y/N]\n")
    moveToDir = str(moveToDir)
    listFiles = []
    fileCounter = 1
    if (moveToDir == "Y" and listDirectories != None):
        for dir in listDirectories:
            if (os.path.isdir(dir)):
                for path, subdirs, files in os.walk(dir):
                    for file in files:
                        print(str(fileCounter) + " - " + file)
                        listFiles.append(path+"/"+file)
                        fileCounter += 1

        print(str(fileCounter) + " - " + "Exit")
        fileChoice = input("Select one of the files or exit:\n")

        try:
            fileChoice = int(fileChoice)

        except ValueError:
            print("Invalid choice\n")
            print("File placed in subs folder\n")

        else:
            if (fileChoice != fileCounter):
                moveShiftedSubs(shiftedFile, listFiles[fileChoice-1])
            else:
                print("Operation cancelled. File placed in subs folder\n")
    else:
        if (moveToDir == "N"):
            print("File placed in subs folder\n")
        else:
            print("No directories in user.txt. Please insert at least one directory to use this feature")
else:
    print("There are no subtitles in the subs folder. Please place some there")
