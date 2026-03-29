import board
import neopixel
from time import sleep

# Designed for Waveshare RP2040-One
# Should also work on RP2040-Zero, RP2350-Zero, RP250-One

# ----- Init -----
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.05, auto_write=True)

def wheel(hue):
    if hue < 85:
        r = int(hue * 3)
        g = int(255 - hue * 3)
        b = 0
    elif hue < 170:
        hue -= 85
        r = int(255 - hue * 3)
        g = 0
        b = int(hue * 3)
    else:
        hue -= 170
        r = 0
        g = int(hue * 3)
        b = int(255 - hue * 3)
    return (r, g, b)

while True:
    for hue in range(255):
        pixels[0] = wheel(hue)
        sleep(0.01)