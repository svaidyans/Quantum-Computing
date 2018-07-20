//Name of Experiment: Shor's 62mod91 
//Version: v2 
//Date: 11Jul2018 
//Developer:  Vaidyanathan Sivasubramanian

include "qelib1.inc";
qreg q[7];
creg c[7];

x q[1];
x q[2];
x q[3];
x q[4];
x q[5];

x q[0];
x q[2];
x q[3];
x q[5];
x q[6];

cx q[3],q[2];
cx q[2],q[3];
cx q[3],q[2];
cx q[2],q[1];
cx q[1],q[2];
cx q[2],q[1];
cx q[4],q[1];
cx q[1],q[4];
cx q[4],q[1];

measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
measure q[4] -> c[4];