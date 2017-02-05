import colorsys


def rgb_to_hls(r, g, b):
    """Takes rgb 0-255 values and returns hls 0-1 values"""
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255
    return colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)