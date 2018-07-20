# Name: Grover_N_3_A111.py
# Version: v1
# Description: Grover's Algorithm implementing with 3 Qubits for A=111 on local device
# Date: 05Jul2018
# Developer: Vaidyanthan Sivasubramanian.

# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute

# Create a Quantum Register with 3 Qubits
q = QuantumRegister ( 3 )
# Create a Classical Register with 3 bits
c = ClassicalRegister ( 3 )
# Create a Quantum Circuit
qc = QuantumCircuit ( q, c )

# Add H gates on the Qubits
qc.h ( q[0] )
qc.h ( q[1] )
qc.h ( q[2] )

# Add a CX (CNOT) gate on Control Qubit 1 and Target Qubit 2, for
# putting the Qubits in a Bell State
qc.cx ( q[1], q[2] )

# Add a transposed conjugate T gate on Target Qubit
qc.tdg ( q[2] )

# Add a CX (CNOT) gate on Control Qubit 0 and Target Qutbit 2, for
# putting the Qubits in a Bell State
qc.cx ( q[0], q[2] )

# Add a T gate on Target Qubit 2
qc.t ( q[2] )

# Add a CX (CNOT) gate on Control Qubit 1 and Target Qutbit 2, for
# putting the Qubits in a Bell State
qc.cx ( q[1], q[2] )

# Add a transposed conjugate T gate on Target Qubit
qc.tdg ( q[2] )

# Add a CX (CNOT) gate on Control Qubit 0 and Target Qutbit 2, for
# putting the Qubits in a Bell State
qc.cx ( q[0], q[2] )

# Add a T gate on Target Qubit 1
qc.t ( q[1] )

# Add a T gate on Target Qubit 2
qc.t ( q[2] )

# Add a CX (CNOT) gate on Control Qubit 0 and Target Qutbit 1, for
# putting the Qubits in a Bell State
qc.cx ( q[0], q[1] )

# Add a transposed conjugate T gate on Target Qubit
qc.tdg ( q[1] )

# Add a CX (CNOT) gate on Control Qubit 0 and Target Qutbit 1, for
# putting the Qubits in a Bell State
qc.cx ( q[0], q[1] )

# Add a T gate on Target Qubit 0
qc.t ( q[0] )

# Add H gates on the Qubits
qc.h ( q[0] )
qc.h ( q[1] )
qc.h ( q[2] )

# Add X gates on the Qubits
qc.x ( q[0] )
qc.x ( q[1] )
qc.x ( q[2] )

# Add a CX (CNOT) gate on Control Qubit 1 and Target Qutbit 2, for
# putting the Qubits in a Bell State
qc.cx ( q[1], q[2] )

# Add a transposed conjugate T gate on Target Qubit
qc.tdg ( q[2] )

# Add a CX (CNOT) gate on Control Qubit 0 and Target Qutbit 2, for
# putting the Qubits in a Bell State
qc.cx ( q[0], q[2] )

# Add a T gate on Target Qubit 2
qc.t ( q[2] )

# Add a CX (CNOT) gate on Control Qubit 1 and Target Qutbit 2, for
# putting the Qubits in a Bell State
qc.cx ( q[1], q[2] )

# Add a transposed conjugate T gate on Target Qubit
qc.tdg ( q[2] )

# Add a CX (CNOT) gate on Control Qubit 0 and Target Qutbit 2, for
# putting the Qubits in a Bell State
qc.cx ( q[0], q[2] )

# Add T gates on Qubits 1 and 2
qc.t ( q[1] )
qc.t ( q[2] )

# Add a CX (CNOT) gate on Control Qubit 0 and Target Qutbit 1, for
# putting the Qubits in a Bell State
qc.cx ( q[0], q[1] )

# Add a transposed conjugate T gate on Target Qubit
qc.tdg ( q[1] )

# Add a CX (CNOT) gate on Control Qubit 0 and Target Qutbit 1, for
# putting the Qubits in a Bell State
qc.cx ( q[0], q[1] )

# Add X and H gates on Qubits
qc.x ( q[0] )
qc.x ( q[1] )
qc.x ( q[2] )

qc.h ( q[0] )
qc.h ( q[1] )
qc.h ( q[2] )

# Add a Measure gates to see the States
qc.measure ( q[0], c[0] )
qc.measure ( q[1], c[1] )
qc.measure ( q[2], c[2] )

# See a list of available local simulators
print ( "Local backends: ", available_backends ( { 'local': True } ) )

# Compile and run the Quantum circuit on a simulator backend
job_sim = execute( qc, "local_qasm_simulator" )
sim_result = job_sim.result ()

# Show the results
print ( "simulation: ", sim_result )
print ( sim_result.get_counts ( qc ) )
