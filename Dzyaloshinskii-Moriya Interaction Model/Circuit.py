from qiskit import QuantumCircuit
from qiskit.circuit import Gate
from qiskit.visualization import circuit_drawer

D = "D Interaction Value"
t = "Time duration for interaction"

qc = QuantumCircuit(2)

qc.h(0)
qc.sdg(1)
qc.h(1)

qc.cx(0,1)

rz_gate = Gate(name="Rz", num_qubits=1, params=[])
qc.append(rz_gate, [1])

qc.cx(0,1)
qc.h(0)
qc.h(1)
qc.s(1)

qc.sdg(0)
qc.h(0)
qc.h(1)
qc.cx(0,1)

rz_gate2 = Gate(name="Rz", num_qubits=1, params=[])
qc.append(rz_gate2, [1])

qc.cx(0,1)
qc.h(0)
qc.s(0)
qc.h(1)

qc.measure_all()

circuit_drawer(qc, output="mpl", filename="circuit.png", scale=2)
circuit_drawer(qc, output="mpl", filename="circuit.pdf")
