from tkinter.filedialog import askopenfilename, askdirectory
import math
from scipy.stats import chisquare
import analizerConfig as conf




def validation(observedFile, expectedFile):
    tmp = observedFile.split(chr(47))
    tmp2 = ""
    for x in range(len(tmp)-1):
        tmp2 = tmp2 + tmp[x] + chr(47)
    saveDirectory = tmp2 + "testResults.txt"
    ef = open(expectedFile, "r+")
    of = open(observedFile, "r+")
    g = open((saveDirectory), "w")
    num = "0,1,2,3,4,5,6,7,8,9"
    expectedDic = {"": []}
    observedDic = {"": []}
    for x in ef:
        splited = x.split(":")
        tmp = splited[1]
        if tmp[5] in num:
            expectedDic[splited[0]] = float(tmp[1:5])
        else:
           expectedDic[splited[0]] = float(tmp[1:4])

    expectedDic.pop("")

    first = True
    for x in of:
        if ".py" not in x:
            splited = x.split(":")
            tmp = splited[1]

            observedDic[splited[0]] = float(tmp[1:len(tmp)-1])

        else:
            if first == False:
                y = 0
                expectedList = list(expectedDic)
                observedList = list(observedDic)
                while y < 32:
                    expectedArray = ["", ]
                    observedArray = ["", ]
                    n = 0
                    while n <= 2**conf.inputQubits:
                        n = n + 1
                        expectedArray.append("")
                        observedArray.append("")
                    expectedArray2 = []
                    for z in expectedList:
                        tmp = z.split(", ")
                        num = tmp[1].split(")")
                        input = tmp[0].split("(")
                        if int(input[1]) == y:
                            expectedArray[int(num[0])] = expectedDic[z]
                            expectedArray2.append(num[0])
                    observedArray2 = []
                    for z in observedList:
                        tmp = z.split(", ")
                        num = tmp[1].split(")")
                        input = tmp[0].split("(")
                        if int(input[1]) == y:
                            observedArray[int(num[0])] = observedDic[z]
                            observedArray2.append(num[0])

                    while "" in expectedArray:
                        expectedArray.remove("")
                    while "" in observedArray:
                        observedArray.remove("")
                    expectedArray2.sort()
                    observedArray2.sort()
                    if observedArray2 == expectedArray2:
                        result = chisquare(expectedArray, observedArray)

                        if result[1] < conf.p_value:
                            g.write("FILE: " + str(filename[0]) + " with input [" + str(y) + "]" + " FAILED WITH P-Value " + str(result[1]))
                            g.write("\n")
                        else:
                            if math.isnan(result[1]):
                                 p_value = 1
                            else:
                                p_value = result[1]
                            g.write("FILE: " + str(filename[0]) + " with input [" + str(y) + "]" + " VALID WITH P-Value " + str(p_value))
                            g.write("\n")
                    else:
                        inside = True
                        for z in observedArray2:
                            if z not in expectedArray2:
                                inside = False
                        if inside == False:
                            g.write("File: " + str(filename[0]) + " with input [" + str(y) + "]" + "FAILED DIRECTLY without checking P-Value ")
                            g.write("\n")
                        else:
                            i = 0
                            filedObservedArray = []
                            for z in expectedArray2:
                                if z not in observedArray2:
                                    filedObservedArray.append(0)
                                else:
                                    filedObservedArray.append(observedArray[i])
                                    i = i + 1
                            result = chisquare(expectedArray, filedObservedArray)
                            if result[1] < conf.p_value:
                                g.write("FILE: " + str(filename[0]) + " with input [" + str(
                                    y) + "]" + " FAILED WITH P-Value " + str(result[1]))
                                g.write("\n")
                            else:
                                if math.isnan(result[1]):
                                    p_value = 1
                                else:
                                    p_value = result[1]
                                g.write("FILE: " + str(filename[0]) + " with input [" + str(
                                    y) + "]" + " VALID WITH P-Value " + str(p_value))
                                g.write("\n")
                    y = y + 1
            else:
                first = False
            filename = x.split(".py")
            observedDic.clear()
    return