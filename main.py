from __future__ import division
import utils
import csv

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()
axes = figure.add_subplot(111, projection='3d')


def rgb_string_to_denormalized_hls(row):
    rgb = row[0][1:]
    r = int(rgb[0] + rgb[1], 16)
    g = int(rgb[2] + rgb[3], 16)
    b = int(rgb[4] + rgb[5], 16)
    hls = utils.rgb_to_hls(r, g, b)
    return hls[0] * 360, hls[1] * 100, hls[2] * 100


def processFile(filename, **kwargs):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                hls = rgb_string_to_denormalized_hls(row)
            except IndexError:
                continue

            # print "%s\t%s\t%s" % (hls[0], hls[1], hls[2])
            axes.scatter(hls[0], hls[1], hls[2], **kwargs)


processFile('colours/azzurro.csv', c='r')
processFile('colours/lazurowy.csv', c='b')

axes.set_xlabel('Hue')
axes.set_xlim3d(0, 360)
axes.set_ylabel('Lightness')
axes.set_ylim3d(0, 100)
axes.set_zlabel('Saturation')
axes.set_zlim3d(0, 100)

plt.show()
