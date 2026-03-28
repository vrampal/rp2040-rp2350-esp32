import board
import digitalio
from time import sleep

# Designed for any Raspberri Pi Pico
# Gen 1 or Gen 2, with our without wireless

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    sleep(0.5)
    led.value = False
    sleep(0.5)
