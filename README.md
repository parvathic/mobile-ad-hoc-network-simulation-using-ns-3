# mobile-ad-hoc-network-simulation-using-ns-3

Using NS-3 to compare the performance of mobile ad-hoc network routing protocols such as AODV, DSR and DSDV.

Comparison of the three protocols is done with the following aspects in mind: 

1] Delay caused by routing protocols
2] The number of mobile nodes
3] Distance between nodes
4] Speed [Pause Time]

1] Delay

- The average delay for a successful transmission is calculated and compared between the three protocols. A python code is developed from scratch to parse the .flows file created by the File Moniter module in NS-3 [used in the code to run the simulation].

- Delay is calculated while varying the 2] number of transmitters and receivers, 3] distance between nodes, 4] pause time (speed)

