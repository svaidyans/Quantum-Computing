# Name: Shors_Factor_91.py
# Version: v1
# Description: Shors algorithm implementation for finding one factor of 91 
#              on a 7 qubit local simulator
# Date: 05Jul2018
# Developer: Vaidyanthan Sivasubramanian.

# Define the fuction to return GCD of two values 
def GCD ( a, b ):
    if ( b == 0 ):
       return ( a )
    else:
       return ( GCD ( b, a % b ) )

# Define the QFT function for 62mod91
def QFT ():
    # Import the QISKit SDK
    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
    from qiskit import available_backends, execute

    # Create a Quantum Register with 7 qubits
    q = QuantumRegister (7)

    # Create a Classical Register with 7 bits
    c = ClassicalRegister (7)

    # Create a Quantum Circuit
    qc = QuantumCircuit ( q, c )

    # Add the X gates
    qc.x ( q[1] );
    qc.x ( q[2] );
    qc.x ( q[3] );
    qc.x ( q[4] );
    qc.x ( q[5] );

    qc.x ( q[0] );
    qc.x ( q[2] );
    qc.x ( q[3] );
    qc.x ( q[5] );
    qc.x ( q[6] );

    # Add the CX gates
    qc.cx ( q[3], q[2] );
    qc.cx ( q[2], q[3] );
    qc.cx ( q[3], q[2] );
    qc.cx ( q[2], q[1] );
    qc.cx ( q[1], q[2] );
    qc.cx ( q[2], q[1] );
    qc.cx ( q[4], q[1] );
    qc.cx ( q[1], q[4] );
    qc.cx ( q[4], q[1] );

    # Add the Measure gates
    qc.measure ( q[1], c[1] );
    qc.measure ( q[2], c[2] );
    qc.measure ( q[3], c[3] );
    qc.measure ( q[4], c[4] );

    # Compile and run the Quantum circuit on a simulator backend
    sim_job = execute ( qc, "local_qasm_simulator" )

    # Get the result and period

    import json

    sim_job_result = sim_job.result ()
    sim_job_counts = sim_job_result.get_counts ( qc )

    period = 0
    for key, value in sim_job_counts.items():
        key_data = int ( key, 2 )
        if ( period < key_data ):
            period = key_data

    return period

# Define the main function
def main ():

    # Initial values
    N = 91
    M = 3
    print ( "*** Starting the program" )
    print ( "    N =", N, "and M =", M )

    print ( "    Starting the QFT" )
    P = QFT ()
    r = int ( M ** ( P / 2 ) - 1 )
    print ( "    Period from QFT =", P, "and r =", r )

    factor = GCD ( r, N )
    print ( "*** Factor found =", factor )

main ()