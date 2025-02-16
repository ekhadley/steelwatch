import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

inpin = 19
outpin = 26

if __name__ == "__main__":
    gpio.setup(inpin, gpio.IN)
    gpio.setup(outpin, gpio.OUT)

    

    gpio.cleanup()
