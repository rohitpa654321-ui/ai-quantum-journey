# Day 1: Quantum Basics
from qiskit import QuantumCircuit

# Create a simple 1-qubit quantum circuit
qc = QuantumCircuit(1)
qc.h(0)  # Apply Hadamard gate
qc.measure_all()
print(qc)
