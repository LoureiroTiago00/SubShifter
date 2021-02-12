from SetupDir import *

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
    else:
        print("There are not subtitles in the subs folder. Please place some there")
else:
    print("Please insert some directories in the file named user.txt")