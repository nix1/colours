from __future__ import division
import utils
import csv


with open('colours/lazurowy.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            rgb = row[0][1:]
        except IndexError:
            continue
        r = int(rgb[0] + rgb[1], 16)
        g = int(rgb[2] + rgb[3], 16)
        b = int(rgb[4] + rgb[5], 16)

        hls = utils.rgb_to_hls(r, g, b)
        print "%s\t%s\t%s" % (hls[0] * 360, hls[1] * 100, hls[2] * 100)

