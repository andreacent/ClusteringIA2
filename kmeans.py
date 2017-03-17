#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Pseudocodigo https://jarroba.com/k-means-python-scikit-learn-ejemplos/
#
import numpy as np
import random

class Cluster:
    def __init__(self, points):
        self.points = points
        self.centroid = self.calculate_centroid()
        self.converge = False

    def calculate_centroid(self):        
        sum_coordinates = np.zeros(len(self.points[0]))
        for p in self.points:
            for i, x in enumerate(p):
                sum_coordinates[i] += x

        return (sum_coordinates / len(self.points)).tolist()

    def update_cluster(self, points):
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculate_centroid()
        self.converge = np.array_equal(old_centroid, self.centroid)

##############################################
# Calculate the nearest cluster
# @param clusters: old clusters
# @param point: point to assign cluster
# @return: index of list cluster
def get_nearest(clusters, point):
    dist = np.zeros(len(clusters))
    for i, c in enumerate(clusters):
        _sum = 0
        for k in range(len(point)):
            _sum += ((point[k] - c.centroid[k]) ** 2)
        dist[i] = abs(_sum)
    return np.argmin(dist)

##############################################
# Read file
# @param Int k : number of clusters
# @param [Array[Int]] points 
def kmeans(k,points,iterations):
    # Select k points random to initiacize the k Clusters
    initial = random.sample(points, k)
    # Create K clusters
    clusters = [Cluster([p]) for p in initial]
    
    while (not all([c.converge for c in clusters])) and (iterations > 0):
        # Lists to save the new points of cluster
        new_points = [[] for i in range(k)]

        # Assign points in nearest centroid
        for p in points:
            i_cluster = get_nearest(clusters, p)
            new_points[i_cluster].append(p)

        # Set new points in clusters and calculate de new centroids
        for i, c in enumerate(clusters):
            c.update_cluster(new_points[i])

        iterations -= 1

    # Print final result
    return clusters
