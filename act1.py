#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import kmeans as km
import numpy as np

##############################################
# Get point types and print cluster
# @param Cluster cluster: cluster
# @param [Array[Int]] points: all points of data
# @param [String] p_types: types of points 
def print_cluster(cluster,points,p_types):
    map_type = {'Iris-virginica':0,'Iris-setosa':0,'Iris-versicolor':0}
    for cp in cluster.points:
        i=0
        while not np.array_equal(cp, points[i]):
            i+=1
        map_type[p_types[i]] += 1

    print('   Número de puntos:', len(cluster.points))
    print ('   Centroide:',str(cluster.centroid))
    for k,v in map_type.items():
        print('  ',k,v)

##############################################
# Read file
# @param [File] filename : file with data
def readDataFile(filename):
    points = []
    p_types = []

    with open(filename, 'r', encoding="utf-8") as data_file:
        for line in data_file:
            _line =line.split(",")
            p_types.append(_line.pop()[:-1])
            l = [float(li) for li in _line]
            points.append(np.array(l))

    return points,p_types

##############################################
# MAIN
def main(argv):
    MAX_ITERATIONS = 1000
    points,p_types = readDataFile(argv[1])

    for k in range(2,6):
        print('\n---NUMERO DE CLUSTERS---',k)
        clusters = km.kmeans(k,points,MAX_ITERATIONS)

        i=1
        for c in clusters:
            print ('CLUSTER',i)
            print_cluster(c,points,p_types)
            i+=1

if __name__ == "__main__":
    main(sys.argv)