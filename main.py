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
        print()
        print(color_name_from_filename(filename))
        print()
        for row in reader:
            try:
                hls = rgb_string_to_denormalized_hls(row)
            except IndexError:
                print("")
                continue
            print("%s\t%s\t%s" % (hls[0], hls[1], hls[2]))
            yield hls


def color_name_from_filename(path):
    return os.path.splitext(os.path.basename(path))[0]

if __name__ == '__main__':
    """
    Example usage:
    python main.py /path/to/data/series1.csv [/path/do/data/series2.csv]
    """
    files = sys.argv[1:]
    figure = plt.figure()
    axes = figure.add_subplot(111, projection='3d')

    for idx, file in enumerate(files):
        series_color = 'r' if idx % 2 == 0 else 'b'
        hls_averages = [0, 0, 0]
        hls_count = 0

        # calculate sums and draw the scatterplot
        for h, l, s in processFile(file):
            hls_averages = map(operator.add, hls_averages, (h, l, s))
            axes.scatter(h, l, s, c=series_color)
            hls_count += 1

        # convert sums to averages
        hls_averages = map(operator.truediv, hls_averages, [hls_count]*3)

        # round it a bit
        hls_averages = map(round, hls_averages, [2]*3)

        print(color_name_from_filename(file),  # filename without extension
              hls_averages[0],  # hue
              hls_averages[1],  # lightness
              hls_averages[2],  # saturation
              sep='\t')


    axes.set_xlabel('Hue')
    axes.set_xlim3d(0, 360)
    axes.set_ylabel('Lightness')
    axes.set_ylim3d(0, 100)
    axes.set_zlabel('Saturation')
    axes.set_zlim3d(0, 100)

    plt.show()
