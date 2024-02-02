# Alternate keymapping that acts as a numpad

from adafruit_hid.keycode import Keycode

keys = [
    # Row 0
    Keycode.ESCAPE,
    Keycode.KEYPAD_SEVEN,
    Keycode.KEYPAD_EIGHT,
    Keycode.KEYPAD_NINE,
    Keycode.BACKSPACE,
    # Row 1
    Keycode.KEYPAD_NUMLOCK,
    Keycode.KEYPAD_FOUR,
    Keycode.KEYPAD_FIVE,
    Keycode.KEYPAD_SIX,
    Keycode.KEYPAD_EQUALS,
    # Row 2
    Keycode.KEYPAD_ZERO,
    Keycode.KEYPAD_ONE,
    Keycode.KEYPAD_TWO,
    Keycode.KEYPAD_THREE,
    Keycode.KEYPAD_ENTER,
]
