from keys import *

import board
import digitalio
import time

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Set up keyboard USB device
kbd = Keyboard(usb_hid.devices)

# Pins left to right, top to bottom
# Combined with keys.py to create mapping
pins = [
    # Row 0
    board.GP13,
    board.GP18,
    board.GP21,
    board.GP3,
    board.GP0,
    # Row 1
    board.GP12,
    board.GP17,
    board.GP20,
    board.GP4,
    board.GP1,
    # Row 2
    board.GP11,
    board.GP16,
    board.GP19,
    board.GP22,
    board.GP2,
]

# Create list of pins and respective key inputs
switches = []
for pin, key in zip(pins, keys):
    pin = digitalio.DigitalInOut(pin)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    switches.append((pin, key))

# Array of booleans to save the state of the last time inputs were checked
state = [0] * len(switches)

# Main loop
while True:
    for i, (button, key) in enumerate(switches):
        if state[i] != button.value:
            try:
                # If pressed down
                if state[i] == True:
                    kbd.press(key)
                else:
                    kbd.release(key)
            # If > 6 keys pressed at once
            except:
                pass

            state[i] = button.value
    # Debounce
    time.sleep(0.01)
