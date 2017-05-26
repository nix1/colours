from __future__ import division, print_function
import utils
import csv
import sys
import os
import operator
import math

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def rgb_string_to_denormalized_hls(row):
    rgb = row[0][1:]
    r = int(rgb[0] + rgb[1], 16)
    g = int(rgb[2] + rgb[3], 16)
    b = int(rgb[4] + rgb[5], 16)
    h, l, s = utils.rgb_to_hls(r, g, b)
    return h, l, s


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
    files = sys.argv[1:]
    figure = plt.figure()
    axes = figure.add_subplot(111, projection='3d')

    for idx, file in enumerate(files):
        series_color = 'r' if idx % 2 == 0 else 'b'
        hls_averages = [0, 0, 0]
        hls_count = 0

        # first pass - calculate sums
        for h, l, s in processFile(file):
            hls_averages = map(operator.add, hls_averages, (h, l, s))
            hls_count += 1

        # convert them to averages
        hls_averages = map(operator.truediv, hls_averages, [hls_count]*3)

        # second pass - calculate the standard deviations and draw the scatterplot
        deviations_acc = [0, 0, 0]
        for h, l, s in processFile(file):
            diffs = map(operator.sub, hls_averages, (h, l, s))
            # square them
            diffs2 = map(operator.mul, diffs, diffs)
            # add to the acc
            deviations_acc = map(operator.add, deviations_acc, diffs2)
            axes.scatter(h, l, s, c=series_color)

        # variances
        deviations_acc = map(operator.truediv, deviations_acc, [hls_count] * 3)

        # deviations
        deviations_acc = map(math.sqrt, deviations_acc)

        # round it a bit
        hls_averages = map(round, hls_averages, [2]*3)
        deviations_acc = map(round, deviations_acc, [2]*3)

        print(os.path.splitext(os.path.basename(file))[0], # filename without extension
              hls_averages[0], deviations_acc[0], # hue
              hls_averages[1], deviations_acc[1], # lightness
              hls_averages[2], deviations_acc[2], # saturation
              sep='\t')


    axes.set_xlabel('Hue')
    axes.set_xlim3d(0, 360)
    axes.set_ylabel('Lightness')
    axes.set_ylim3d(0, 100)
    axes.set_zlabel('Saturation')
    axes.set_zlim3d(0, 100)

    plt.show()
