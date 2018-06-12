import RPi.GPIO as GPIO  # importing time GPIO module
import time  # importing time module

GPIO.setmode(GPIO.BOARD)  # setting the numbering system
GPIO.setup(12, GPIO.IN)  # setting pin 12 as input
while True:  # while loop
    input_value = GPIO.input(12)  # reading from pin 12
    if input_value == False:  # comparing pin 12 input
        print("the button has been pressed.")  # printing message
        while input_value == False:
            input_value = GPIO.input(12)
