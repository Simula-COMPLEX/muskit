
import sys
import functionalities
import math


mode = str(sys.argv[1])

if mode == "Execute":
    importfile = str(sys.argv[2])
    f = open(importfile)
    line = f.readline()
    while line != "":
        if "numShots" in line:
            var = line.split("= ")
            var = var[1].split(" #")
            numShots = int(var[0])
        if "allInputs" in line:
            var = line.split("= ")
            var = var[1].split(" #")
            if "True" in var[0]:
                allInputs = True
            else:
                allInputs = False

        line = f.readline()
    f.close()

    importfile = str(sys.argv[3])
    f = open(importfile)
    line = f.readline()
    while line != "":
        if "inputs" in line:
            var = line.split("= ")
            var = var[1].split(" #")
            var = var[0]
            var = var[1:(len(var) - 1)]
            var = var.split(",")
            inputs = ["", ]
            x = var[0]
            inputs[0] = str(x[1:len(x)-1])
            for x in var[1:len(var)]:
                inputs.append(str(x[1:len(x)-1]))
        line = f.readline()
    f.close()
    files = sys.argv[4:len(sys.argv)]
    splitChar = "\\"
    if splitChar not in files[0]:
        splitChar = chr(47)
    path = files[0].split(splitChar)
    savePath = path[0]
    x = 1
    while x < len(path) - 1:
        savePath = savePath + splitChar + path[x]
        x = x + 1
    functionalities.executeMutants(files, savePath, numShots, allInputs, inputs)
elif mode == "Create":

    importfile = str(sys.argv[2])
    f = open(importfile)
    line = f.readline()
    while line != "":
        if "maxNumberOfMutants" in line:
            var = line.split("= ")
            var = var[1].split(" #")
            maxNumberOfMutants = int(var[0])
        if "operators" in line:
            var=line.split("= ")
            var = var[1].split(" #")
            operators = var[0]
        if "types" in line:
            var = line.split("= ")
            var = var[1].split(" #")
            types = var[0]
        if "gateNum" in line:
            var = line.split("= ")
            var = var[1].split(" #")
            var = var[0]
            var = var[1:(len(var)-1)]
            var = var.split(",")
            gateNum =["",]
            gateNum[0] = int(var[0])
            for x in var[1:len(var)]:
                gateNum.append(int(x))
        if "location" in line:
            var = line.split("= ")
            var = var[1].split(" #")
            var = var[0]
            var = var[1:(len(var)-1)]
            var = var.split(",")
            location =["", ]
            location[0] = int(var[0])
            for x in var[1:len(var)]:
                location.append(int(x))
        if "phases" in line:
            var = line.split("= ")
            var = var[1].split(" #")
            var = var[0]
            var = var[1:(len(var)-1)]
            var = var.split(",")
            phases=["",]
            phases[0] = math.radians(float(var[0]))
            for x in var[1:len(var)]:
                phases.append(math.radians(float(x)))

        if "allMutants" in line:
            var = line.split("= ")
            var = var[1].split(" #")
            if "True" in var[0]:
                allMutants = True
            else:
                allMutants = False

        line = f.readline()
    f.close()

    file = str(sys.argv[3])

    splitChar = 92
    if chr(splitChar) not in file:
        splitChar = 47

    path = file.split(chr(splitChar))
    savePath = path[0]
    x = 1
    while x < len(path) - 1:
        savePath = savePath + chr(splitChar) + path[x]
        x = x + 1
    functionalities.createMutants(maxNumberOfMutants, operators, types, gateNum, location, file, savePath, allMutants, phases)
else:
    print("The command was not okay")