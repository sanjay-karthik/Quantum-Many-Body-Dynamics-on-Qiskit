from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

N = 2            # number of qubits
alpha = 0.6         
gamma = 0.4         
beta  = 0.7           
n_periods = 1    # Floquet periods

qc = QuantumCircuit(N)
for _ in range(n_periods):

    qc.h(0)
    qc.h(1)
    qc.cx(0, 1)
    qc.rz(2 * alpha, 1)
    qc.cx(0, 1)
    qc.h(0)
    qc.h(1)

    qc.rz(2 * beta, 0)

    qc.sdg(0)
    qc.sdg(1)
    qc.h(0)
    qc.h(1)
    qc.cx(0, 1)
    qc.rz(2 * gamma, 1)
    qc.cx(0, 1)
    qc.h(0)
    qc.h(1)
    qc.s(0)
    qc.s(1)

qc.measure_all()

filename = f"Floquet_XXZ_2qubit_{n_periods}periods.png"
circuit_drawer( qc,output="mpl", fold=-1, filename=filename)

print(f"Saved circuit as: {filename}")
