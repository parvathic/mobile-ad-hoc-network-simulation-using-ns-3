# mobile-ad-hoc-network-simulation-using-ns-3

The code for the framework and the default models provided by ns-3 is built as a set of libraries. User simulations are expected to be written as simple programs that make use of these ns-3 libraries.

This project is designed to observe wireless mobile ad-hoc network behavior and understand the different mechanisms associated with it, and uses NS-3 to compare the performance of mobile ad-hoc network routing protocols such as AODV, DSR and DSDV.

Comparison of the three protocols is done with the following aspects in mind: 

1] Delay caused by routing protocols
2] The number of mobile nodes
3] Distance between nodes
4] Speed [Pause Time]

1] Delay

- The average delay for a successful transmission is calculated and compared between the three protocols. A python code is developed from scratch to parse the .flows file created by the File Moniter module in NS-3 [used in the code to run the simulation].

- Delay is calculated while varying the 2] number of transmitters and receivers, 3] distance between nodes, 4] pause time (speed)

PART 1:
1. Running a C++ code on NS-3 simulating a point to point transmission [2 nodes] and observing the throughput.
2. Adding one more node, observing the throughput, observing the delay and what factors determine the delay.
- Throughput decreases with increase in a node, and delay increases due to collisions. Backoff time is the only factor that significantly affects delay.
3. Increasing the distance and observing the change.
- The packets received at the receiver is lesser as the nodes move out of range.
4. Repeat the above with RTS/CTS and observe the change.
- Throughput increases as collisions decrease.
5. Throughput as the number of users increase.
- Individual throughput decreases as the number of users decrease, but net throughput also decreases due to the backoff time, as the channel is essentially idle for long periods of time.

PART 2:
1. Running a C++ code on NS-3 simulating a mobile ad hoc network consisting of 20 transmitting nodes and 5 receiver nodes.
2. Run the code and route using the DSDV ad-hoc protocol.
3. The output files consist of a .txt file [from the FlowMonitor module on NS-3 in the C++ simulation code], a .routes file that contain the routing tables of all the nodes, .tr trace file that contains information of every single transmission [including hops] and .pcap files.
4. This simulation is run again with the routing protocol changed to AODV and DSR.
5. The average delay for all flows in the simulation for each routing protocol is determined by a Python code developed from scratch. In the case of AODV and DSDV, the Python code parses the .txt file to determine the average delay/flow. In case of DSR, another Python code is developed from scratch and parses the .tr file [this is because DSR is an IP level protocol and Flow Monitor only tracks L4 layer protocols].
6. The respective delays are compared.
- DSR has the largest delay as it inserts the entire routing route in the packets header and therefore incurs larger overheads leading to higher delay.
7. Delay is also compared while increasing users, speed for all three protocols.
