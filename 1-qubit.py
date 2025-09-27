# Simple Qiskit program demonstrating a 1-qubit quantum circuit

from qiskit import QuantumCircuit, Aer, execute

def main():
    # Create a 1-qubit, 1-classical-bit quantum circuit
    qc = QuantumCircuit(1, 1)

    # Apply Hadamard gate to put the qubit in superposition
    qc.h(0)

    # Measure the qubit
    qc.measure(0, 0)

    # Run on QASM simulator
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=10)
    result = job.result()

    # Get measurement results
    counts = result.get_counts(qc)
    print("Quantum Circuit Result:", counts)

if __name__ == "__main__":
    main()
