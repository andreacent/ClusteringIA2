#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import sys
import kmeans_image as km


##############################################
# Load image
# @param [File] imagename : Picture
def loadImage(imagename):

    picture = Image.open(imagename)
    pix = picture.load()
    x,y = picture.size
    rgb_size = len(pix[0,0])

    pixels = []
    for i in range(int(x)):
        for j in range(int(y)):
            rgb = [int(pix[i,j][c]) for c in range(rgb_size)]
            pixels.append(km.Pixel([i,j],rgb))

    picture.close()
    return pixels

##############################################
# Compress image
# @param [File] imagename : Picture
def compressImage(imagename, clusters,k):

    picture = Image.open(imagename)
    pix = picture.load()

    for cluster in clusters:
        for pixel in cluster.pixels:

            pix[pixel.coordinates[0],pixel.coordinates[1]] = cluster.centroid_rgb()

    name = imagename.split('.')
    picture.save(name[0]+'_K'+str(k)+"."+name[1])

    picture.close()

##############################################
# MAIN
def main(argv):
    MAX_ITERATIONS = 1000
    pixels = loadImage(argv[1])
    k = int(argv[2])

    clusters = km.kmeans(k,pixels,MAX_ITERATIONS)

    compressImage(argv[1],clusters,k)

if __name__ == "__main__":
    main(sys.argv)