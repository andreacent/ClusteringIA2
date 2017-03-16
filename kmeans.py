#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np

#Split data
def split(data,percentage):
    rows=len(data)
    trainRows=int(round((percentage*rows)/float(100)))
    trainD = data[:trainRows]
    testD = data[trainRows:]
    return trainD,testD

##############################################
# Read file
# @param [File] filename : file with data
def readDataFile(filename):
    inputs,target, data = [],[],[]

    with open(filename, 'r', encoding="utf-8") as data_file:
        for line in data_file:
            l =line.split(",")

            #Iris-setosa: 0,0
            if (l[-1][:-1] == "Iris-setosa"):
                data.append([ float(l[0]), float(l[1]), float(l[2]), float(l[3]), float(0), float(0) ])

            #Iris-versicolor: 0,1
            elif(l[-1][:-1] == "Iris-versicolor"):
                data.append([ float(l[0]), float(l[1]), float(l[2]), float(l[3]), float(0), float(1)])

            #Iris-virginica: 1,0
            elif(l[-1][:-1] == "Iris-virginica"):
                data.append([ float(l[0]), float(l[1]), float(l[2]), float(l[3]), float(1), float(0) ])


        np.random.shuffle(data)
            
        for d in data:
            inputs.append([ d[0], d[1], d[2], d[3] ])
            target.append([ d[4], d[5] ])

    return inputs, target

##############################################
# Read file
# @param Int k : number of clusters
# @param [Int] dataset 
#https://jarroba.com/k-means-python-scikit-learn-ejemplos/
def kmeans(k,dataset):
    #Iniciar K clustering con sus centroides u
    while True:
        sum_x = 0
        for i in range(len(dataset)):
            #argmin
            sum_x += x[i]
        for j in range(k):
            u[j] = sum_x/n 

##############################################
# MAIN
def main(argv):
    inputs, target = readDataFile(argv[1])
