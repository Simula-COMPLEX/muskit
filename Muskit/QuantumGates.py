# This file has two purposes 
# Mutation Selection: A user can specify the gates to be used for generation of mutants
# Extension: A user can specify the new gates here and the tool will also use them for mutation generation
# The default file contains all the current supported gates
# Note: One must specify a gate in multiple sets. For example, a one qubit gate must be specified both in AllGates and also in OneQubit
AllGates = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx", "swap", "rzz", "rxx", "cx", "cz", "ccx", "cswap") #All gates that are implemented
OneQubit = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx") #Gates that only affect one qubit
TwoQubit = ("swap", "rzz", "rxx", "cx", "cz") #Gates that affect two qubit
MoreThanTwoQubit = ("ccx", "cswap") #Gates that affect more than two qubit
PhaseGates = ("p", "rx", "ry", "rz", "rzz", "rxx") #Gates that affect the phase and needs to specify a phase

