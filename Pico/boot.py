# Disables showing up as Mass Storage device unless top left key is held down on boot

import storage
import board, digitalio

button = digitalio.DigitalInOut(board.GP13)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Disable UMS only if top left button is not pressed.
if button.value:
    storage.disable_usb_drive()