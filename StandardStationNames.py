def createNewDict(aDict):
    with open("output.txt", "a") as myFile:
        log = []
        ct = 0
        for key, val in aDict.items():
            for key2, val2 in aDict.items():
                ct += 1
                if val[0] == val2[0] and key != key2:
                    #print(3)
                    if val[1] >= val2[1]:
                        if "Change '" + key2 + "' (" + str(val2[1]) + ") to '" + key + "' (" + str(val[1]) + ")" not in log:
                            log.append("Change '" + key2 + "' (" + str(val2[1]) + ") to '" + key + "' (" + str(val[1]) + ")")
                            changeDict[key2] = key
                    else:
                        if "Change '" + key + "' (" + str(val[1]) + ") to '" + key2 + "' (" + str(val2[1]) + ")" not in log:
                            log.append("Change '" + key + "' (" + str(val[1]) + ") to '" + key2 + "' (" + str(val2[1]) + ")")
                            changeDict[key] = key2
        for message in log:
            myFile.write(message + "\n")


def createDictionary(index):
    #TESTING VARIABLES
    fourCt = 0 #Test
    sixCt = 0 #Test
    elseCt = 0 #Test
    line = file.readline()[:-1]
    while line:
        lineList = line.split(",")
        if line != '': #ensures last line is not read
            lineList[index] = lineList[index].strip('\"')
            lineList[index+2] = lineList[index+2].strip('\"')
            if lineList[index] not in startDict: #if the start station name is not in dictionary
                startDict[lineList[index]] = [lineList[index+1],1] #adds station name to dict, assigns ID as value, 1 is counter
            else:
                startDict[lineList[index]][1] += 1 #adds 1 to counter
            if lineList[index+2] not in startDict: #if the start station name is not in dictionary
                startDict[lineList[index+2]] = [lineList[index+3],1] #adds station name to dict, assigns ID as value, 1 is counter
            else:
                startDict[lineList[index+2]][1] += 1 #adds 1 to counter
            #testing
            if lineList[index] == "Cottage Grove Ave & 87th St":
                #print("4:", line)
                fourCt += 1
            elif lineList[index+2] == "Cottage Grove Ave & 87th St":
                #print("6:", line)
                sixCt += 1
            elif "Cottage Grove Ave & 87th St" in line:
                #print("Etc:", line)
                elseCt += 1
            line = file.readline()[:-1] #reads line minus newline character
    #print(fourCt, sixCt, elseCt)

def createNewFiles():
    monthCt = 1
    for f in files:
        file = open(f)
        fileStr = file.read()
        with open("Month_" + str(monthCt) + "_.txt", "w") as new_file:
            for old, new in changeDict.items():
                fileStr.replace(old, new)
            new_file.write(fileStr)
        monthCt += 1
        file.close()

#data to be transformed
files = ["202201-divvy-tripdata.csv", "202202-divvy-tripdata.csv", "202203-divvy-tripdata.csv", "202204-divvy-tripdata.csv",\
        "202205-divvy-tripdata.csv", "202206-divvy-tripdata.csv", "202207-divvy-tripdata.csv", "202208-divvy-tripdata.csv",\
        "202209-divvy-publictripdata.csv", "202210-divvy-tripdata.csv", "202211-divvy-tripdata.csv", "202212-divvy-tripdata.csv"]


startDict = {}
changeDict = {}
for f in files:
    file = open(f)
    createDictionary(4)
    file.close()
createNewDict(startDict)
createNewFiles()


