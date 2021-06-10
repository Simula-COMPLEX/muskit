from tkinter.filedialog import askopenfilename, askdirectory
import analizerConfig as conf
import chiSquare


def resultCleaner(filename, saveDirectory):
  f = open(filename, "r+")
  saveDirectory = saveDirectory + chr(47) + "cleanResults.txt"
  g = open((saveDirectory), "w")
  prefile = ""
  preinput = ""
  for x in f:
    splited = x.split(" ",8)
    tmp = splited[6]
    path = splited[3].split(chr(47))
    executedFile = path[len(path)-1]
    input = tmp[1:conf.inputQubits+1]
    tmp = splited[8]
    tmp = tmp[1:len(tmp)-2]
    output = tmp.split(", ")
    itsIn= False
    cleanOutput=[]
    for y in range(len(output)):
      outputMeasure = ""
      bin = output[y]
      for n in conf.measureQubits:
        outputMeasure = outputMeasure + str(bin[n+1])
      output[y] = outputMeasure + ":" + bin[conf.inputQubits+4:len(bin)]

    for y in output:
      itsIn = False
      tmp= y.split(":")
      for z in range(len(cleanOutput)):
        tmp2 = cleanOutput[z].split(":")
        if tmp[0] == tmp2[0]:
          itsIn = True
          cleanOutput[z] = tmp2[0] + ":" + str(int(tmp[1]) + int(tmp2[1]))
      if itsIn == False:
        cleanOutput.append(y)



    for y in range(len(cleanOutput)):
      tmp = cleanOutput[y].split(":")
      cleanOutput[y] = str(int(tmp[0],2))+":"+str(int(tmp[1])/100)

    if executedFile != prefile:
      prefile = executedFile
      g.write(executedFile+"------------------------------------------------------------------")
      g.write("\n")

    if input != preinput:
      for y in cleanOutput:
        tmp = y.split(":")
        g.write("("+str(int(input,2))+", "+tmp[0]+"): " + tmp[1])
        g.write("\n")
      preinput = input
  return saveDirectory

def main():
  print("Select mutants results file: ")
  results = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
  print("Select the expected outputs file: ")
  expectedFile = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
  print("Select the directory where the validation will save: ")
  saveDirectory = askdirectory()

  observedFile = resultCleaner(results, saveDirectory)
  chiSquare.validation(observedFile, expectedFile)

if __name__ == "__main__":
  main()

