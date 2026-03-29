import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard
from time import sleep

# Adjust depending of the targetted keyboard layout
import keyboard_layout_win_fr as keyboard_layout
from keycode_win_fr import Keycode

# Designed for Waveshare RP2040-One
# Should also work on any RP2040 or RP2350 board

keyboard = Keyboard(usb_hid.devices)
layout = keyboard_layout.KeyboardLayout(keyboard)
cc = ConsumerControl(usb_hid.devices)

keyboard.send(Keycode.WINDOWS, Keycode.D)
sleep(0.1)
keyboard.send(Keycode.WINDOWS, Keycode.R)
sleep(0.2)
layout.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
keyboard.send(Keycode.ENTER)
for n in range(100):
    cc.send(ConsumerControlCode.VOLUME_INCREMENT)
sleep(0.5)
keyboard.send(Keycode.F11)
sleep(2.0)
keyboard.send(Keycode.F)