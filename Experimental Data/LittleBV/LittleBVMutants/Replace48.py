import qiskit
from qiskit import *


q = QuantumRegister(6, 'q')
c = ClassicalRegister(6, 'c')
qc = QuantumCircuit(q, c)


qc.h(q[3])
qc.h(q[4])
qc.h(q[5])

qc.cz(q[0],q[3])
qc.cz(q[1],q[4])
qc.cz(q[2],q[5])

qc.p(1.5707963267948966,q[3])
qc.h(q[4])
qc.h(q[5])
