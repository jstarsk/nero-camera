import time

# Raspberry PI
# importing time GPIO module
# import RPi.GPIO as GPIO
# importing time module
# # setting the numbering system
# GPIO.setmode(GPIO.BOARD)
# # setting pin 12 as input
# GPIO.setup(12, GPIO.IN)
#
# Sequoia camera
from NEROSequoia import *

nero = NEROSequoia()

while True:
    # input value by Raspberry pit
    # reading from pin 12
    # input_value = GPIO.input(12)

    # input value by keyboard
    input_value = raw_input('Press "T" to trigger sequoia camera.:')
    if input_value.upper() == "T":
        print(str.format("the button has been pressed is : {0}", input_value.upper()))
        nero.triggerCamera()
        input_value = " "