import board
import usb_hid
import neopixel
import random
from adafruit_hid.mouse import Mouse
from time import sleep

# Designed for Waveshare RP2040-One
# Should also work on RP2040-Zero, RP2350-Zero, RP2350-One

# ----- LED colors ------
BLACK = (  0,   0,   0)
RED   = (  0, 255,   0)
GREEN = (255,   0,   0)
BLUE  = (  0,   0, 255)
WHITE = (255, 255, 255)

# ----- Init -----
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.05, auto_write=True)
mouse = Mouse(usb_hid.devices)

def jiggle(ampli, maxMoves):
    # Start at (0,0)
    currentX = 0
    currentY = 0
    # Generate N+1 moves
    n = random.randint(1, maxMoves)
    # Delay between moves in seconds
    delay = random.uniform(0.072, 0.314)
    while (n > 0):
        # New cursor targer
        targetX = random.randint(-ampli, ampli)
        targetY = random.randint(-ampli, ampli)
        # Move the mouse
        distX = targetX - currentX
        distY = targetY - currentY
        if ((distX != 0) or (distY != 0)):
            mouse.move(distX, distY)
            # Record new position
            currentX = targetX
            currentY = targetY
            # Decrement remaining moves
            n = n - 1
            # Wait before next move
            sleep(delay)
    # Finish at (0,0)
    targetX = 0
    targetY = 0
    # Move the mouse
    distX = targetX - currentX
    distY = targetY - currentY
    if ((distX != 0) or (distY != 0)):
        mouse.move(distX, distY)

# ----- Main -----
delay = random.uniform(4.73, 5.22)
sleep(delay)
while True:
    pixels[0] = BLUE
    # Jiggle with 5 pixels amplitude and up to 5 moves
    jiggle(5, 5)
    pixels[0] = BLACK
    # wait before repeating
    delay = random.uniform(8.16, 31.42)
    sleep(delay)