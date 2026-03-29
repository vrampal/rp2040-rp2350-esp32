import usb_cdc
import usb_midi
import storage
import supervisor

# This must be run in boot.py and not code.py

# The following lines will change vendor id and device id.
# WARNING: changing the vid and pid will prevent the REPL debugger to connect to the devide.
# Almost mimic a Logitech Unifying Receiver, see: https://devicehunt.com/view/type/usb/vendor/046D
# Use an obsolete vid to not confuse Logitech drivers, Logitech normal vid is 0x046D
supervisor.set_usb_identification(
    vid=0x04E0,
    pid=0xC52B,
    manufacturer="Logitech, Inc.",
    product="Unifying Receiver"
)
# Disable REPL
usb_cdc.disable()

# Uncommenting the folling line will disable storage.
# WARNING: it will become IMPOSSIBLE to access or modify code.py or boot.py after reboot
#storage.disable_usb_drive()

# Disable MIDI
usb_midi.disable()