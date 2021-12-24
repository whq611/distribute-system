import numpy
import pandas as pd
import matplotlib.pyplot as plt


nodenums,time = 3,100

l = []
for node in range(nodenums):
    with open("s1/node" + str(node) +".txt","r") as fs:
        for line in fs:
            l.append(line)

Delays = []
Bandwidths = []
for i in range(time):
    Delays.append([])
    Bandwidths.append([])


start = float((l[0].split()[3]))
for line in l:
    for sec in range(time):
        if start + sec <= float(line.split()[3]) < start + sec + 1:
            Delays[sec].append(float(line.split()[3]) - float(line.split()[1]))
            Bandwidths[sec].append(float(line.split()[4]))
            break

plt.subplots(figsize = (15, 10)) 
plt.subplots_adjust(hspace = 0.5)
dy = plt.subplot(211)
timeRange = range(time)
dy.plot(timeRange, pd.DataFrame(Delays).T.min(), marker='o')
dy.plot(timeRange, pd.DataFrame(Delays).T.max(), marker='*')
dy.plot(timeRange, pd.DataFrame(Delays).T.median(), marker='v')
dy.plot(timeRange, pd.DataFrame(Delays).T.quantile(0.9), marker='^')
dy.legend(['Min', 'Max', 'Mid', '90th Percentile'])
dy.set(xlabel='time(second)', ylabel='delay(second)', title='Evaluation Delay S1')


bd = plt.subplot(212, sharex = dy)
bd.plot(timeRange, pd.DataFrame(Bandwidths).T.sum(), marker='o')
bd.legend(['Sum'])
bd.set(xlabel='time(second)', ylabel='bandwidth(byte/second)', title='Evaluation Bandwidth S1')

plt.savefig('s1.jpg')
#plt.show()