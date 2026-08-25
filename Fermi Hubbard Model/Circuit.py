from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

# Parameters
t = 0.6
u = 0.3
dt = 1.0

# 2-Qubit Fermi–Hubbard Circuit
# H = -t(XX + YY) + U ZZ
qc = QuantumCircuit(2)

# XX term
qc.h(0)
qc.h(1)

qc.cx(0, 1)
qc.rz(-2 * t * dt, 1)
qc.cx(0, 1)

qc.h(0)
qc.h(1)

# YY term
qc.sdg(0)
qc.sdg(1)
qc.h(0)
qc.h(1)

qc.cx(0, 1)
qc.rz(-2 * t * dt, 1)
qc.cx(0, 1)

qc.h(0)
qc.h(1)
qc.s(0)
qc.s(1)

# ZZ term
qc.cx(0, 1)
qc.rz(-2 * u * dt, 1)
qc.cx(0, 1)

qc.measure_all()

circuit_drawer(qc, output="mpl", fold=-1, filename="fermi_hubbard_2qubit.png")
print(f"Saved circuit as: {filename}")
