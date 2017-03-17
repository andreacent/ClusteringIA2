#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import numpy as np

class Pixel:
    def __init__(self, coordinates, rgb):
        self.coordinates = coordinates
        self.rgb = rgb

    def rgb():
        return (self.rgb[0],self.rgb[1],self.rgb[2])

class Cluster:
    def __init__(self, pixels):
        self.pixels = pixels
        self.centroid = self.calculate_centroid()
        self.converge = False

    def calculate_centroid(self):        
        sum_coordinates = np.zeros(len(self.pixels[0].rgb))
        for p in self.pixels:
            for i, x in enumerate(p.rgb):
                sum_coordinates[i] += x

        return (sum_coordinates / len(self.pixels)).tolist()

    def update_cluster(self, pixels):
        old_centroid = self.centroid
        self.pixels = pixels
        self.centroid = self.calculate_centroid()
        self.converge = np.array_equal(old_centroid, self.centroid)

##############################################
# Calculate the nearest cluster
# @param clusters: old clusters
# @param pixel: pixel to assign cluster
# @return: index of list cluster
def get_nearest(clusters, pixel):
    dist = np.zeros(len(clusters))
    for i, c in enumerate(clusters):
        _sum = 0
        for k in range(len(pixel.rgb)):
            _sum += ((pixel.rgb[k] - c.centroid[k]) ** 2)
        dist[i] = abs(_sum)
    return np.argmin(dist)

##############################################
# Read file
# @param Int k : number of clusters
# @param [Array[Pixel]] pixels 
def kmeans(k,pixels,iterations):
    # Select k pixels random to initiacize the k Clusters
    initial = random.sample(pixels, k)
    # Create K clusters
    clusters = [Cluster([p]) for p in initial]
    
    while (not all([c.converge for c in clusters])) and (iterations > 0):
        # Lists to save the new pixels of cluster
        new_pixels = [[] for i in range(k)]

        # Assign pixels in nearest centroid
        for p in pixels:
            i_cluster = get_nearest(clusters, p)
            new_pixels[i_cluster].append(p)

        # Set new pixels in clusters and calculate de new centroids
        for i, c in enumerate(clusters):
            c.update_cluster(new_pixels[i])

        iterations -= 1

    # Print final result
    return clusters
