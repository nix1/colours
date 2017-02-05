import unittest
import colorsys

class TestConversion(unittest.TestCase):

    def test_hsv_values(self):
        values = [
            # rgb, hsv
            ((0.0, 0.0, 0.0), (0, 0.0, 0.0)),  # black
            ((0.0, 0.0, 1.0), (4. / 6., 1.0, 1.0)),  # blue
            ((0.0, 1.0, 0.0), (2. / 6., 1.0, 1.0)),  # green
            ((0.0, 1.0, 1.0), (3. / 6., 1.0, 1.0)),  # cyan
            ((1.0, 0.0, 0.0), (0, 1.0, 1.0)),  # red
            ((1.0, 0.0, 1.0), (5. / 6., 1.0, 1.0)),  # purple
            ((1.0, 1.0, 0.0), (1. / 6., 1.0, 1.0)),  # yellow
            ((1.0, 1.0, 1.0), (0, 0.0, 1.0)),  # white
            ((0.5, 0.5, 0.5), (0, 0.0, 0.5)),  # grey
        ]
        for (rgb, hsv) in values:
            self.assertEqual(hsv, colorsys.rgb_to_hsv(*rgb))
            self.assertEqual(rgb, colorsys.hsv_to_rgb(*hsv))

    def test_hls_values(self):
        values = [
            # rgb, hls
            ((0.0, 0.0, 0.0), (0, 0.0, 0.0)),  # black
            ((0.0, 0.0, 1.0), (4. / 6., 0.5, 1.0)),  # blue
            ((0.0, 1.0, 0.0), (2. / 6., 0.5, 1.0)),  # green
            ((0.0, 1.0, 1.0), (3. / 6., 0.5, 1.0)),  # cyan
            ((1.0, 0.0, 0.0), (0, 0.5, 1.0)),  # red
            ((1.0, 0.0, 1.0), (5. / 6., 0.5, 1.0)),  # purple
            ((1.0, 1.0, 0.0), (1. / 6., 0.5, 1.0)),  # yellow
            ((1.0, 1.0, 1.0), (0, 1.0, 0.0)),  # white
            ((0.5, 0.5, 0.5), (0, 0.5, 0.0)),  # grey
        ]
        for (rgb, hls) in values:
            self.assertEqual(hls, colorsys.rgb_to_hls(*rgb))
            # self.assertEqual(rgb, colorsys.hls_to_rgb(*hls))

if __name__ == '__main__':
    unittest.main()