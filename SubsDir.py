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
