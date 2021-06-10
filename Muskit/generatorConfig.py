#Mutants Generator Configuration Variables
import math
maxNumberOfMutants = 100 # Maximum number of mutants to be generated
operators = ("Add","Replace") # Type of operators to be use to create mutants. Valid values are Add, Replace, Remove
types = ("OneQubit",) # Types of gates the mutation will change, Valid values are OneQubit and ManyQubit
gateNum = (1,3) # Gate number to be replaced and removed.
location = (1, 5) # Location number of the gaps that will be used to add gates.
phases = [0,90,180,270] # Phase degrees that will be used to select one value randomly. A valid value is between 0 and 360.
allMutants = False # If this variable is true, then all the possible mutants will be generated.

