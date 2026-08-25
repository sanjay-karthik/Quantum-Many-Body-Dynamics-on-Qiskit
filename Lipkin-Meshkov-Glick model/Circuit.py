from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
from math import pi

N =             # number of qubits
lam =           # interaction strength
gamma =         # anisotropy
h =             # transverse field
dt =            # trotter step

theta_xx = 2 * lam * dt / N
theta_yy = 2 * lam * gamma * dt / N
theta_z  = 2 * h * dt

qc = QuantumCircuit(N)

for i in range(N):
    for j in range(i + 1, N):
        qc.h(i)
        qc.h(j)
        qc.cx(i, j)
        qc.rz(theta_xx, j)
        qc.cx(i, j)
        qc.h(i)
        qc.h(j)

for i in range(N):
    for j in range(i + 1, N):
        qc.sdg(i)
        qc.sdg(j)
        qc.h(i)
        qc.h(j)
        qc.cx(i, j)
        qc.rz(theta_yy, j)
        qc.cx(i, j)
        qc.h(i)
        qc.h(j)
        qc.s(i)
        qc.s(j)

for i in range(N):
    qc.rz(theta_z, i)

qc.measure_all()

filename = f"LMG_{N}qubit.png"
circuit_drawer(qc, output="mpl", filename=filename, fold=-1)

print(f"Saved circuit as: {filename}")
