from SetupDir import *
from Shift import *
import sys

print("Welcome to SubShifter\n")

createDir()
createConfigFile()

listDirectories = readMovieDirectories()
if (listDirectories != None):

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

        shiftSub(listSubs[choice-1])
        print("Subtitles successfully shifted")

    else:
        print("There are not subtitles in the subs folder. Please place some there")
else:
    print("Please insert some directories in the file named user.txt")