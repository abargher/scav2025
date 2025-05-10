from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)
button_pin = Pin(0, Pin.IN, Pin.PULL_UP)

print("LED starts flashing...")
pin.off()
while True:
    try:
        if button_pin.value() == 0:
            pin.on()
        else:
            pin.off()
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
