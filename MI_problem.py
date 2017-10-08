###############################################################################################################
#Rule 1: if the string ends in I, you can add a U to it. e.g. MI --> MIU ## LINE: 7
#Rule 2: you can double what comes after the M. e.g. MIU --> MIUIU ######## LINE: 22
#Rule 3: you can turn III into a U. e.g. MIII --> MU ###################### LINE: 38
#Rule 4: you can drop UU anywhere in a string. e.g. MIIUUI --> MIII ####### LINE: 56
##############################################################################################################
#Rule 1: if the string ends in I, you can add a U to it. e.g. MI --> MIU
def rule1(miArray, methodStart, methodEnd):
    for looper in range (methodStart, methodEnd):
        stringCheck = miArray[looper]
        if stringCheck[-1] == "I":
            stringCheck = stringCheck + "U"
            duplicateCheck = 0
            arrayLength = len(miArray)
            for counter in range(0, arrayLength):
                if stringCheck == miArray[counter]:
                    duplicateCheck = 1
            if duplicateCheck == 0:
                miArray.append(stringCheck)
    return miArray

#Rule 2: you can double what comes after the M. e.g. MIU --> MIUIU
def rule2(miArray, methodStart, methodEnd):
    for looper in range (methodStart, methodEnd):
        stringDouble = miArray[looper]
        stringDouble = stringDouble[1:]
        stringDouble = stringDouble * 2
        stringDouble = "M" + stringDouble
        duplicateCheck = 0
        arrayLength = len(miArray)
        for counter in range(0, arrayLength):
            if stringDouble == miArray[counter-1]:
                 duplicateCheck = 1
        if duplicateCheck == 0:
            miArray.append(stringDouble)
    return miArray

#Rule 3: you can turn III into a U. e.g. MIII --> MU
def rule3(miArray, methodStart, methodEnd):
    for looper in range (methodStart, methodEnd):
        stringCheck = miArray[looper]
        length = len(stringCheck)
        for counter in range(0, (length - 3)):
            stringThing = stringCheck[(counter+1):(counter+4)]
            if stringThing == "III":
                newEntry = (stringCheck[:(counter+1)] + "U" + stringCheck[(counter+4):])
                duplicateCheck = 0
                arrayLength = len(miArray)
                for counter in range(0, arrayLength):
                    if newEntry == miArray[counter-1]:
                        duplicateCheck = 1
                if duplicateCheck == 0:
                    miArray.append(newEntry)
    return miArray

##Rule 4: you can drop UU anywhere in a string. e.g. MIIUUI --> MIII
def rule4(miArray, methodStart, methodEnd):
    for looper in range (methodStart, methodEnd):
        stringCheck = miArray[looper]
        length = len(stringCheck)
        for counter in range(0, (length - 2)):
            stringThing = stringCheck[(counter+1):(counter+3)]
            if stringThing == "UU":
                newEntry = (stringCheck[:(counter+1)] + stringCheck[(counter+3):])
                duplicateCheck = 0
                arrayLength = len(miArray)
                for counter in range(0, arrayLength):
                    if newEntry == miArray[counter-1]:
                        duplicateCheck = 1
                if duplicateCheck == 0:
                    miArray.append(newEntry)
    return miArray


target = raw_input("Please enter the target combination in all caps.")
maxTries = int(raw_input("How many entries should the program find before giving up"))
miArray = ["MI"]
arrayLength = 1
loopEndCheck = 0
methodStart = 0
methodIncrease = 1
methodEnd = 1
loopCount = 0

while loopEndCheck == 0:
    loopCount = loopCount + 1
    print miArray
    arrayLength = len(miArray)
    for looper in range(methodStart, methodEnd):
        if miArray[looper] == target:
            loopEndCheck = 1
            lastDigit = int(str(loopCount)[-1])
            if loopCount == 11 or loopCount == 12:
                print "Successfully found the target string on the " + str(loopCount) + "th line of the tree!"
            elif lastDigit == 1:
                print "Successfully found the target string on the " + str(loopCount) + "st line of the tree!"
            elif lastDigit == 2:
                print "Successfully found the target string on the " + str(loopCount) + "nd line of the tree!"
            elif lastDigit == 3:
                print "Successfully found the target string on the " + str(loopCount) + "rd line of the tree!"
            else:
                print "Successfully found the target string on the " + str(loopCount) + "th line of the tree!"
    numberOfTries = len(miArray)
    if numberOfTries >= maxTries:
        if loopEndCheck == 0:
            loopEndCheck = 1
            print "I gave up!"
    rule1(miArray, methodStart, methodEnd)
    rule2(miArray, methodStart, methodEnd)
    rule3(miArray, methodStart, methodEnd)
    rule4(miArray, methodStart, methodEnd)
    methodStart = methodStart + methodIncrease
    methodIncrease = (len(miArray) - arrayLength)
    methodEnd = methodEnd + methodIncrease
    numberOfTries = len(miArray)

