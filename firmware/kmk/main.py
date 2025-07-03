import board
import busio

#kmk stuff
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.scanners.keypad import MatrixScanner

# initializing the keyboard
keyboard = KMKKeyboard()

# macro setup
macros = Macros()
keyboard.modules.append(macros)

# initializing encoder handler
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# pin setup
PINS = [board.D4, board.D7, board.D8, board.D9, board.D10, board.D11]

encoder_handler.pins = (
    (board.D3, board.D2, board.D1, False),  # (pin_a, pin_b, pin_button, is_inverted)
)

# encoder actions
Rotate_left = KC.LEFT
Rotate_right = KC.RIGHT

encoder_handler.map = [
    ((Rotate_left, Rotate_right, KC.SPACE),),
]

# display setup
bus = busio.I2C(board.GP_SCL, board.GP_SDA)
driver = SSD1306(i2c=bus, device_address=0x3C)

display = Display(
    display=driver,
    width=128,
    height=32,
    flip = False,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.8
)

# display action
display.entries = [
        TextEntry(text="THE DialPad", x=64, y=16, x_anchor="M", y_anchor="M"),
]

keyboard.matrix = MatrixScanner(
    rows=(board.D11, board.D7, board.D4),
    cols=(board.D8, board.D9, board.D10),
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.1, KC.2, KC.3,
     KC.4, KC.5, KC.6,
     KC.7, KC.8, KC.9]
]

# starting kmk
if __name__ == '__main__':
    keyboard.go()