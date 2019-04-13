import numpy as np
your_file = open('dsdv.txt')

flow = your_file.readlines()
flow

#mean delay
j=0
m3 = []
for i in range(3, 483, 4):
    m1 = flow[i].split()
    m2 = m1[2:3]
    #print(m2)
    m3.insert(j, m2)
    j+=1
print(m3, "\n")

#packets
q=0
p3 = []
for w in range(1, 480, 4):
    p1 = flow[w].split()
    p2 = p1[5:6]
    p3.insert(q, p2)
    q+=1
print(p3, "\n")

b=np.array(p3)
b2 = [list(map(float, x)) for x in b]

a=np.array(m3)
a2 = [list(map(float, x)) for x in a]
a2=np.array(a2)

c = a2*b2
c2 = np.multiply(a2, b2)

c3 = [list(map(float, x)) for x in c2]
c3 = np.array(c3)

float_formatter = lambda x: "%.2f" % x
float_formatter(1.6556848e+02)
np.set_printoptions(formatter={'float_kind':float_formatter})

s=0
i=0
for i in range(0, 120, 1):
    temp = c3[i]
    s+=temp

p3= [list(map(float, x)) for x in p3]
p4 = np.array(p3)
tpackets =0
for i in range(0, 120, 1):
    temp = p4[i]
    tpackets+=temp
print(tpackets)

#final delay
totaldelay = s/tpackets
print(totaldelay)
