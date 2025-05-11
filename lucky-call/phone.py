import board
import digitalio
import time
import usb_hid
import random

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Set up phone buttons on GP0 and GP1
button_dial = digitalio.DigitalInOut(board.GP0)
button_dial.direction = digitalio.Direction.INPUT
button_dial.pull = digitalio.Pull.UP  # Pull-up resistor
    
hang_up_switch = digitalio.DigitalInOut(board.GP1)
hang_up_switch.direction = digitalio.Direction.INPUT
hang_up_switch.pull = digitalio.Pull.UP


number_file = "all-house-rep-nums.txt"


def place_call():
    # select a random number
    ind = random.randrange(0, 432)
    
    curr_ind = 0
    phone_num = ""
    with open(number_file) as f:
        for line in f:
            if curr_ind == ind:
                phone_num = line.strip().strip(",")
                break
            curr_ind +=1
    print(f"found number {phone_num}")
    

def hang_up():
    print("hanging up")
    

# HID keyboard support

keyboard = Keyboard(usb_hid.devices)
write_text = KeyboardLayoutUS(keyboard)

dial_threshold = 2
on_dock = True
sevens_dialed = 0
last_seven_time = 0
have_seen_seven = False

in_call = False
try:
    while True:
        this_time = time.time()
        
        if sevens_dialed >= 3 and not in_call:
            in_call = True
            sevens_dialed = 0
            place_call()

        if this_time - last_seven_time > dial_threshold:
            sevens_dialed = 0
            have_seen_seven = False

        on_dock = not hang_up_switch.value
        if not button_dial.value:
            if not have_seen_seven:
                have_seen_seven = True
                last_seven_time = this_time

            if not in_call and this_time - last_seven_time < dial_threshold:
                sevens_dialed += 1
                last_seven_time = this_time

            print(f"sevens dialed = {sevens_dialed}")
            time.sleep(0.1)
            
        if not hang_up_switch.value:
            if in_call:
                in_call = False
                hang_up()
            time.sleep(0.1)
        
        time.sleep(0.1)  # Slight delay to reduce CPU usage
except KeyboardInterrupt:
    print("Button test stopped.")
    

