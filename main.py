from __future__ import division
import utils
import csv
import sys
import os

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def rgb_string_to_denormalized_hls(row):
    rgb = row[0][1:]
    r = int(rgb[0] + rgb[1], 16)
    g = int(rgb[2] + rgb[3], 16)
    b = int(rgb[4] + rgb[5], 16)
    hls = utils.rgb_to_hls(r, g, b)
    return hls[0], hls[1], hls[2]


def processFile(filename, **kwargs):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                hls = rgb_string_to_denormalized_hls(row)
            except IndexError:
                continue
            # print "%s\t%s\t%s" % (hls[0], hls[1], hls[2])
            yield hls


if __name__ == '__main__':
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    figure = plt.figure()
    axes = figure.add_subplot(111, projection='3d')

    for file, color in [(file1, 'r'), (file2, 'b')]:
        for hls in processFile(file):
            axes.scatter(hls[0], hls[1], hls[2], c=color)

    axes.set_xlabel('Hue')
    axes.set_xlim3d(0, 360)
    axes.set_ylabel('Lightness')
    axes.set_ylim3d(0, 100)
    axes.set_zlabel('Saturation')
    axes.set_zlim3d(0, 100)

    plt.show()
