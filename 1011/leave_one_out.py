#!/usr/bin/env python

import matplotlib.pyplot as plt

def main():
    x = []
    for line in open('iris.dat', 'r'):
        _x = line[:-1].split('\t')
        x.append(_x)

    for _x in x:
        for i in range(4):
            _x[i] = float(_x[i])

    rate = []
    for k in range(1, 31):
        rate.append(leave_one_out(x, k))

    plt.plot(range(1,31), rate)
    plt.show()

def leave_one_out(x, k):
    rate = 0
    for i in range(len(x)):
        
        dist_list = []
        
        for j in range(len(x)):
            if j != i:
                dist_list.append([distance(x[i], x[j]), x[j][4]])
        dist_list.sort()

        setosa = 0; versicolor = 0; virginica = 0;
        
        for l in range(k):
            if dist_list[l][1] == 'I. setosa':
                setosa += 1
            if dist_list[l][1] == 'I. versicolor':
                versicolor += 1
            if dist_list[l][1] == 'I. virginica':
                virginica += 1
                
        list = [setosa, versicolor, virginica]
        
        if x[i][4] == 'I. setosa':
            if setosa == max(list):
                rate += 1
        if x[i][4] == 'I. versicolor':
            if versicolor == max(list):
                rate += 1
        if x[i][4] == 'I. virginica':
            if virginica == max(list):
                rate += 1

    rate /= 148.0
    return rate

def distance(a, b):
    d = 0
    for i in range(len(a)-1):
        d += (a[i]-b[i])**2
    return d
    
main();

