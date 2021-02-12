import time
import datetime


# Creates a new file with the subtitles shifted according to the desired value input by the user 
def shiftSub(subtitleName):
    shiftValue = input("How many seconds do you wish to shift? (Either positive or negative):\n")

    try:
        shiftValue = int(shiftValue)
    except ValueError:
        print("Invalid value")

    else:

        # Necessary encoding to be able to read the files is ISO-8859-1
        subFile = open("./subs/"+subtitleName,"r+",encoding = "ISO-8859-1")
        shiftedSubFile = open("./subs/"+subtitleName+"_SHIFTED","w+", encoding = "ISO-8859-1")
        fileInfo = subFile.read()
        lines = fileInfo.split("\n")

        # Converting every line corresponding to a timestamp to datetime, adding the seconds chosen and then writing them to a second file
        for x in lines:
            if (x != "" and str(x).find("-->") != -1):
                timestamp1 = x.split("-->")[0]
                timestamp2 = x.split("-->")[1]
                timestamp1 = datetime.datetime.strptime(str(timestamp1).strip(),"%H:%M:%S,%f")
                timestamp2 = datetime.datetime.strptime(str(timestamp2).strip(),"%H:%M:%S,%f")
                timestamp1 += datetime.timedelta(seconds=shiftValue)
                timestamp2 += datetime.timedelta(seconds=shiftValue)

                # [:-3] removes the last 3 characters from the strings  
                shiftedSubFile.write(str(timestamp1.strftime("%H:%M:%S,%f"))[:-3]+" --> "+str(timestamp2.strftime("%H:%M:%S,%f"))[:-3]+"\n")
            else:
                shiftedSubFile.write(x+"\n")


        subFile.close()
        shiftedSubFile.close()

    