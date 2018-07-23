# Name: Shors_Generalized.py
# Version: v1
# Description: Shors algorithm implementation for finding one factor 
#              on a 5 qubit local simulator
# Date: 05Jul2018
# Developer: Vaidyanthan Sivasubramanian.

# Check if given Number is prime.  A variant of the classic O(sqrt(N)) 
# algorithm.  It uses the fact that a prime (except 2 and 3) is of 
# form 6k - 1 or 6k + 1 and looks only at divisors of this form.
def Is_Prime ( Number ):

    if Number == 2:
        return True

    if Number == 3:
        return True

    if Number % 2 == 0:
        return False

    if Number % 3 == 0:
        return False

    i = 5
    w = 2
    counter = 1

    while i * i <= Number:

        counter += 1
        if Number % i == 0:
            return False
        i += w
        w = 6 - w

    return True

# Define the fuction to return GCD of two values 
def GCD ( a, b ):

    if ( b == 0 ):
       return ( a )
    else:
       return ( GCD ( b, a % b ) )

# Define the QFT function
def QFT ():
    
    # Import the QISKit SDK
    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
    from qiskit import execute

    # Create a Quantum Register with 5 qubits
    Q = QuantumRegister (5)

    # Create a Classical Register with 5 bits
    C = ClassicalRegister (5)

    # Create a Quantum Circuit
    QC = QuantumCircuit ( Q, C )

    # Add the necessary gates
    QC.u2 ( 0.0, 3.2397674240144743, Q[4] )
    QC.u1 ( 0.196349540849362, Q[3] )
    QC.u2 ( 0.0, 3.5342917352885173, Q[2] )
    QC.u2 ( 0.0, 3.9269908169872414, Q[1] )
    QC.u1 ( 6.283185307179586, Q[0] )
    QC.cx ( Q[0], Q[1] )
    QC.u1 ( 6.283185307179586, Q[1] )
    QC.u3 ( 0.7853981633974485, 1.5707963267948966, 4.71238898038469, Q[0] )
    QC.cx ( Q[0], Q[1] )
    QC.u1 ( 6.283185307179586, Q[1] )
    QC.u3 ( -0.7853981633974485, 1.5707963267948966, 4.71238898038469, Q[0] )
    QC.cx ( Q[0], Q[2] )
    QC.u1 ( 6.283185307179586, Q[2] )
    QC.u3 ( 0.392699081698724, 1.5707963267948966, 4.71238898038469, Q[0] )
    QC.cx ( Q[0], Q[2] )
    QC.u2 ( 0.7853981633974485, 3.141592653589793, Q[2] )
    QC.u2 ( 0.392699081698724, 3.141592653589793, Q[0] )
    QC.cx ( Q[0], Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[0] )
    QC.u2 ( 0.0, 3.141592653589793, Q[2] )
    QC.cx ( Q[0], Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[0] )
    QC.cx ( Q[0], Q[2] )
    QC.cx ( Q[0], Q[1] )
    QC.u1 ( -0.7853981633974485, Q[1] )
    QC.cx ( Q[0], Q[1] )
    QC.u2 ( 0.0, 3.141592653589793, Q[0] )
    QC.u1 ( 0.7853981633974485, Q[1] )
    QC.cx ( Q[0], Q[1] )
    QC.u2 ( 0.0, 3.141592653589793, Q[0] )
    QC.u2 ( 0.0, 3.141592653589793, Q[1] )
    QC.cx ( Q[0], Q[1] )
    QC.u2 ( 0.0, 3.141592653589793, Q[1] )
    QC.u2 ( 0.0, 3.141592653589793, Q[0] )
    QC.cx ( Q[0], Q[1] )
    QC.u2 ( 0.0, 3.141592653589793, Q[0] )
    QC.cx ( Q[3], Q[2] )
    QC.u1 ( -0.196349540849362, Q[2] )
    QC.cx ( Q[3], Q[2] )
    QC.u1 ( 0.392699081698724, Q[3] )
    QC.u1 ( 0.196349540849362, Q[2] )
    QC.cx ( Q[3], Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[3] )
    QC.u2 ( 0.0, 3.141592653589793, Q[2] )
    QC.cx ( Q[3], Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[3] )
    QC.cx ( Q[3], Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[2] )
    QC.cx ( Q[0], Q[2] )
    QC.u1 ( 6.283185307179586, Q[2] )
    QC.u3 ( 0.392699081698724, 1.5707963267948966, 4.71238898038469, Q[0] )
    QC.cx ( Q[0], Q[2] )
    QC.u2 ( 0.7853981633974485, 3.141592653589793, Q[2] )
    QC.u2 ( 0.392699081698724, 3.141592653589793, Q[0] )
    QC.cx ( Q[0], Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[0] )
    QC.u2 ( 0.0, 3.141592653589793, Q[2] )
    QC.cx ( Q[0], Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[0] )
    QC.cx ( Q[0], Q[2] )
    QC.cx ( Q[0], Q[1] )
    QC.u1 ( -0.7853981633974485, Q[1] )
    QC.cx ( Q[0], Q[1] )
    QC.u1 ( 6.283185307179586, Q[0] )
    QC.u2 ( 0.0, 3.9269908169872414, Q[1] )
    QC.u2 ( 0.0, 3.141592653589793, Q[3] )
    QC.cx ( Q[3], Q[4] )
    QC.u1 ( 6.283185307179586, Q[4] )
    QC.u3 ( 0.098174770424681, 1.5707963267948966, 4.71238898038469, Q[3] )
    QC.cx ( Q[3], Q[4] )
    QC.u2 ( 0.196349540849362, 3.141592653589793, Q[4] )
    QC.u2 ( 0.098174770424681, 3.141592653589793, Q[3] )
    QC.cx ( Q[3], Q[4] )
    QC.u2 ( 0.0, 3.141592653589793, Q[3] )
    QC.u2 ( 0.0, 3.141592653589793, Q[4] )
    QC.cx ( Q[3], Q[4] )
    QC.u2 ( 0.0, 3.141592653589793, Q[4] )
    QC.u2 ( 0.0, 3.141592653589793, Q[3] )
    QC.cx ( Q[3], Q[4] )
    QC.cx ( Q[3], Q[2] )
    QC.u1 ( -0.196349540849362, Q[2] )
    QC.cx ( Q[3], Q[2] )
    QC.u1 ( 0.392699081698724, Q[3] )
    QC.u1 ( 0.196349540849362, Q[2] )
    QC.cx ( Q[3], Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[3] )
    QC.u2 ( 0.0, 3.141592653589793, Q[2] )
    QC.cx ( Q[3], Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[3] )
    QC.cx ( Q[3], Q[2] )
    QC.u2 ( 0.0, 3.141592653589793, Q[2] )
    QC.cx ( Q[1], Q[2] )
    QC.u1 ( 6.283185307179586, Q[2] )
    QC.u3 ( 0.392699081698724, 1.5707963267948966, 4.71238898038469, Q[1] )
    QC.cx ( Q[1], Q[2] )
    QC.u3 ( -0.7853981633974485,1.5707963267948966, 4.71238898038469, Q[2] )
    QC.cx ( Q[0], Q[2] )
    QC.u1 ( 6.283185307179586, Q[2] )
    QC.u3 ( 0.7853981633974485,1.5707963267948966, 4.71238898038469, Q[0] )
    QC.cx ( Q[0], Q[2] )
    QC.u1 ( 6.283185307179586, Q[2] )
    QC.u2 ( 0.7853981633974485, 3.141592653589793, Q[0] )
    QC.u2 ( 0.392699081698724, 3.141592653589793, Q[1] )

    # Add the Measure gates
    QC.measure ( Q, C )

    # Compile and run the Quantum circuit on a simulator backend
    Sim_Job = execute ( QC, "local_qasm_simulator" )

    # Get the result and period

    #import json
    Sim_Job_Result = Sim_Job.result ()
    Sim_Job_Counts = Sim_Job_Result.get_counts ( QC )

    Period = 0
    Value_Data = -1 
    for Key, Value in Sim_Job_Counts.items():
        Key_Data = int ( Key, 2 )
        if ( Value_Data < Value ):
           Period = Key_Data
           Value_Data = Value

    return Period

def Print_Factor ( Factor, Attempts ):
    
    End_Time = time.time ()
    Duration = End_Time - Start_Time
    print ( "\n*** Found the factor '", int ( Factor ), "' for Number =", Number, "in", Attempts, "number of attempts and in", round ( Duration, 3 ), "seconds.\n")

# Define the main function
def main ( Number ):

    N = Number
    Attempts = 0
    print ( "\n*** Starting the program\n" )

    print ( "    Checking if given number is Prime")
    End_Time = time.time ()
    Duration = End_Time - Start_Time
    if Is_Prime ( Number ):
       print ( "\n*** Given number", Number, "is a Prime! (took", round ( Duration, 3 ), "seconds to check)\n" )
       return
    else:
       print ( "    Given number is not Prime (took", round ( Duration, 3 ), "seconds to check)...continuing the processs...\n" )

    while True:

       Attempts += 1

       import random
       M = random.randint ( 2, N - 1 )

       # If GCD of ( M, N ) is != 1, that is ( M, N ) are coprime, then we have already have 
       # the non-trivial factor (that is a factor which is not 1 or N itself)!
       Divisor = GCD ( M, N )

       if ( Divisor != 1 ):
          Print_Factor ( Divisor, Attempts )
          break

       # Run the QFT to get the Period 'P' and coeffiennt 'R'
       print ( "\n    Starting the QFT with M =", M )
       P = QFT ()
       if ( P % 2 != 0 ) or ( P == 0 ):
          print ( "    Found an odd period so restarting the process" )
          continue
       else:
          print ( "    Found period P =", P )

       # Get the factor
       try:
           R = M ** ( P / 2 ) - 1
       except OverflowError:
           print ("    R value based on the period found is too big causing overflow so restarting the process...")
           continue

       Factor = GCD ( R, N )
       if ( ( Factor == 1 ) or ( Factor == N ) ):
          print ( "    Found a trivial factor ( 1 or the number itself ) so restarting the process..." )
          continue
       else:   
          Print_Factor ( Factor, Attempts )
          break

# Execute the main function

import time
Start_Time = time.time ()

import sys
Number = 0
if ( ( len ( sys.argv ) == 2 ) and ( sys.argv [1].isdigit () ) and ( len ( sys.argv [1] ) <= 32 ) ):
   Number = int ( sys.argv [1] )

if ( ( __name__ == "__main__" ) and ( Number > 14 ) ):
   main ( Number )
else:
   print ( "*** Usage is: python", sys.argv [0], "<number> where '<number>' should be > 14 and less than 33 digits long!\n" )
