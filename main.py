from __future__ import division
import utils
import os
import sys

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from colorthief import ColorThief


def pick_color(filename):
    color_thief = ColorThief(filename)
    return color_thief.get_color(quality=1)


if __name__ == '__main__':
    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    figure = plt.figure()
    axes = figure.add_subplot(111, projection='3d')

    for dir, color in [(dir1, 'r'), (dir2, 'b')]:
        progress = 0
        for filename in os.listdir(dir):
            if progress % 10 == 0:
                print progress
            progress += 1
            rgb = pick_color(os.path.join(dir, filename))
            hls = utils.rgb_to_hls(*rgb)
            axes.scatter(hls[0], hls[1], hls[2], c=color)

    axes.set_xlabel('Hue')
    axes.set_xlim3d(0, 360)
    axes.set_ylabel('Lightness')
    axes.set_ylim3d(0, 100)
    axes.set_zlabel('Saturation')
    axes.set_zlim3d(0, 100)

    plt.show()
