import usb_hid
from adafruit_hid.keyboard import Keyboard
from time import sleep

# Adjust depending of the targetted keyboard layout
import keyboard_layout_win_fr as keyboard_layout
from keycode_win_fr import Keycode

# Designed for Waveshare RP2040-One
# Should also work on any RP2040 or RP2350 board

keyboard = Keyboard(usb_hid.devices)
layout = keyboard_layout.KeyboardLayout(keyboard)

keyboard.send(Keycode.WINDOWS, Keycode.R)
sleep(0.1)
layout.write("powershell Start-Process https://www.youtube.com/watch?v=dQw4w9WgXcQ")
keyboard.send(Keycode.ENTER)