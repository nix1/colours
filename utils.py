import colorsys


def rgb_to_hls(r, g, b):
    """Takes rgb 0-255 values and returns hls 0-360, 0-100, 0-100 values"""
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255
    hls = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    return hls[0] * 360, hls[1] * 100, hls[2] * 100