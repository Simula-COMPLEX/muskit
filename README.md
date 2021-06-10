# Muskit: A Mutation Analysis Tool for Quantum Software Testing

<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/logoblue.png" width="200">

# Description
Quantum software testing is a new area of research. Thus, there is a lack of benchmark programs and bugs repositories to assess the effectiveness of testing techniques. To this end, the quantum mutation analysis focuses on systematically generating a set of faulty versions of quantum programs, called mutants, using mutation operators. Such faulty versions of quantum programs can be used as benchmarks to assess the quality of test cases in a test suite. Here, we host a tool called Muskit -- a quantum mutation analysis tool for quantum programs coded in IBM's Qiskit language. Muskit implements a set of mutation operators on gates of quantum programs and a set of selection criteria to reduce the number of mutants to generate. Moreover, Muskit allows for the execution of test cases on mutants and generation of test results. Muskit is provided as a command line application, a GUI application, and also as a web application. 



# Architecture of Muskit


<!---
your comment goes here
and here
![Architecture](https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/architecture.png)
A preprint of the paper describing Muskit and its features can be download from <a href="">here</a>.
-->

<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/architecture.png" width="500">

# Extension
Muskit can be extended in two ways: 
- Light-weight extension mechanism: directly specifying new gates in the configuration file (QuantumGates.py), which is read by Muskit to generate mutants; 
- One can also checkout the code of Muskit from GitHub and extend it.

# How to use Muskit?
## Assumptions:
- The code has to be structured in a sequential way without any function definition, main, or sub-functions.
- The qubits should be declared once.
- In order to measure all the qubits correctly, an equal number of classical bits must be defined.

A sample circuit for Quantum Random Access Memory (QRAM) is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/Example/QRAM_program.py">here</a>.

### Configuration Files
The main configuration files are described below. Note that within each file, we list the required variables and their possible valid values.

#### QuantumGate.py
QuantumGate.py has two purposes:
1) configuring Muskit to use quantum gates in MutantsGenerator;
2) specifying newly implemented gates to be used by Muskit. A sample file is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/QuantumGates.py">here</a>

One can specify the gates in the following five categories:

- AllGates = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx", "swap", "rzz", "rxx", "cx", "cz", "ccx", "cswap") # All the gates that are currently supported
- OneQubit = ("x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx") # All the supported gates that affect one qubit
- TwoQubits = ("swap", "rzz", "rxx", "cx", "cz") # All the supported gates that affect two qubits
- MoreThanTwoQubits = ("ccx", "cswap") # All the supported gates that affect more than two qubits
- PhaseGates = ("p", "rx", "ry", "rz", "rzz", "rxx") # All the supported gates that affect the phases of qubits. It requires a user to specify exact phase value to be used, i.e., a value between 0.0 to 360.0

A user can consult Qiskit documentation to read the description of each of the gates <a href="https://qiskit.org/documentation/">here</a>. 

#### generatorConfig.py

This configuration file provides instructions to the MutantsGenerator component. A sample file is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/generatorConfig.py">here</a>.

In particular, it allows the user to specify various selection criteria that will be taken into account while generating mutants. Possible options are:
1) selecting all mutants;
2) setting an upper limit on number of mutants to generate;
3) selecting mutants to generate based on the operator types (i.e., add, remove, or delete);
4) selecting mutants to generate based on gate types (one qubit or multiple qubits);
5) selecting exact gates on a circuit for replace and deleting; and
6) selecting particular locations to add new gates.

#### executorConfig.py
- This configuration provides instructions to the MutantsExecutor component that will be taken into account for executing the mutants. A sample file is available <a href=https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/executorConfig.py>here </a>.

In particular, one can specify the number of times a test case must be executed to account for probabilistic nature of quantum programs. Also, a user can set a variable, i.e., allInputs to true, if the user does not have the test cases to be executed. In this case, a mutant will be executed with all possible inputs, i.e., All Input Coverage criteria. If this variable is set to false, then a user must specify test cases in testcase.py file.

#### analyzerConfig.py
This is a configuration file for Test Analyzer. A sample file for the QRAM program is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/Example/analyzerConfig.py">here</a>.

In particular, one needs to specify a chosen significance level for a statistical test, e.g., p-value=0.05. In addition, a user also has to specify the qubits that should be used as inputs and also the qubits that should be measured. 

### Program Specification and Test Cases

#### testCases.py 
In this file, one can specify the test cases to be executed by Muskit on mutants. A test case is simply the initialization of circuit. A sample is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/QuantumMutation/testCases.py">here</a>

For example, the format for a program with three qubits is:
```inputs = ("001","101","110")```
where we have three test case 001, 101, and 110 that will be used for testing.

#### ProgramSpecifications 
This file is required for test analyzer to determine killing of a mutant with a test case. A sample file corresponding to QRAM is available <a href="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/Example/QR_program_specification.txt">here</a>.
Simply, we specify, for each input its corresponding outputs with their associated expected probabilities. 

To determine whether a mutant is killed, Muskit implements two types of test oracles from <a href="https://ieeexplore.ieee.org/abstract/document/9438603">Quito</a>:
1) Whether an observed output is correct according to program specification. If not, the mutant is killed;
2) If all the observed outputs corresponding to an input are valid, then we compare their observed probabilities with the ones specified in the Program Specification file. If the differences are statistically significant (i.e., a p-value lower than the chosen significance level), the mutant is killed.


# Muskit Installation

- For offline installation, you can clone Muskit from this current GitHub repository, and then follow these steps:
  - Install Anaconda. You can download Anaconda for your OS from https://www.anaconda.com/ For example, For macOS
    ```
    wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-MacOSX-x86_64.sh
    bash Anaconda3-5.3.1-MacOSX-x86_64.sh```
  - Create conda environment: ```conda env create -f environments/yourOS.yml```
    - e.g., ```conda env create -f environments/mac.yml```
- Alternatively, Muskit can be installed with pip as follows:
  
  ```pip install Muskit```

# Muskit Implementations

Muskit is available in the following three implementations described below.

For command line and GUI version, you need to activate the conda environment as follows:

```conda activate Muskit```


## Command Line
The command line version has all the features supported and it is more flexible to be used for experimentation. In particular, the following two commands are used.

- Mutants Generation: ```python3 CommandMain.py Create generatorConfig.py ${yourQuantumProgram}```
- Mutants Execution: ```python3 CommandMain.py Execute executorConfig.py testCases.py ${mutant_1} ... ${mutant_n}```

The first command generates mutants for a provided circuit ${yourQuantumProgram}. Note that depending on the location of ${yourQuantumProgram}, one may need to provide the full path of the file. 
The second command executes all the test cases specified in "testcases.py" on mutants ${mutant_1} ... ${mutant_n} provided as input.

Through the configuration files described above, users can configure both mutant generator and mutants executor for their specific needs.

## GUI

The GUI version can be run as follows: ```python3 Muskit/GraphicMain.py```

A screenshot of the GUI is available below:

<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/gui.png" width="600">

When using the GUI, please note that a user has to follow a step-wise process, which will only enable the options valid at that step to avoid crashing the software.  

The GUI has two main panels, one for mutants generation and the second for mutants execution.
- Mutants Generation: A user can:
  1) Specify the quantum program, whose mutants will be generated;
  2) Destination where the generated mutants will be output;
  3) Various selection criteria that can be used by Muskit to generate mutants. Through the GUI, one can select
      - all mutants;
      - set a limit on maximum number of mutants to be generated;
      - selection based on operator types (i.e., add, remove, or delete);
      - selection based on gate types (one qubit or multiple qubit);
      - selection of exact gates on a circuit for replace and deleting,
      - selection a location to add new gates.
- Mutants Execution: A user can
  1) select the mutants to be executed;
  2) specify the location, where the results will be saved;
  3) specify the number of repetitions for each test case;
  4) specify whether all the inputs must be executed, or only those specified in the testCases.py file must be used.

In addition, a user can also specify the gates (e.g., hadmard, CNOT, etc) in the QuantumGate.py file to instruct Muskit, which gates to be used for mutants generation.

## Online
An online version of Muskit is available here: <a href="https://qiskitmutantcreatorsrl.pythonanywhere.com/"> Web Application </a>
The online only allows a user to generate mutants and execution is not supported. For generation, a user can:
1) Specify the quantum program, whose mutants will be generated;
2) Various selection criteria that can be used by Muskit to generate mutants. One can select
    - all mutants;
    - set a limit on maximum number of mutants to be generated;
    - selection based on operator types (i.e., add, remove, or delete);
    - selection based on gate types (one qubit or multiple qubit). 

A screenshot is available here:

<img src="https://github.com/EnautMendi/QuantumMutationQiskit/blob/master/images/web.png" width="600">

# Video Demonstration
Video demo is available <a href=""> here</a>.

# Experimental Data
Experimental data including quantum programs, and program specifications can be downloaded <a href="">here</a>. 



