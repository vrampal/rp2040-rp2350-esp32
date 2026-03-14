import usb_cdc
import usb_midi
import storage

# Rename this file into boot.py to hide storage and REPL
# Warning: it will become impossible to change code.py or boot.py after reboot

storage.disable_usb_drive()
usb_cdc.disable()
usb_midi.disable()