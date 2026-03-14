import board
import neopixel
from time import sleep

# Designed for Waveshare RP2040-One
# Should also work on RP2040-Zero, RP2350-Zero, RP250-One

# ----- Constants ------
BLACK = (  0,   0,   0)
RED   = (  0, 255,   0)
GREEN = (255,   0,   0)
BLUE  = (  0,   0, 255)
WHITE = (255, 255, 255)

# ----- Init -----
pixels = neopixel.NeoPixel(board.GP16, 1, brightness=0.05, auto_write=True)

while True:
    pixels[0] = RED
    sleep(1.0)
    pixels[0] = GREEN
    sleep(1.0)
    pixels[0] = BLUE
    sleep(1.0)