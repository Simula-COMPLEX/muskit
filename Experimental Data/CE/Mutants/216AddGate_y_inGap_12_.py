import qiskit
from qiskit import *
import math

q = QuantumRegister(6)
c = ClassicalRegister(6)
qc = QuantumCircuit(q,c)


qc.x(q[0])
qc.h(q[2])

qc.h(q[4])
qc.p(math.pi/4,q[4])

qc.x(q[1])
qc.cx(q[1],q[2])
qc.x(q[0])
qc.cx(q[0],q[1])
qc.mct([q[0],q[1]],q[2])

qc.mct([q[2],q[3],q[4]],q[5])
qc.mct([q[2],q[3]],q[4])
qc.mct([q[2]],q[3])

qc.mct([q[0],q[1]],q[2])
qc.cx(q[0],q[1])
qc.x(q[0])
qc.cx(q[1],q[2])
qc.y(q[1])
qc.x(q[1])


