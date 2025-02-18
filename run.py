import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

def blink(pin: int, count:int = 10):
    gpio.setup(pin, gpio.OUT)
    for _ in range(count):
        gpio.output(pin, gpio.HIGH)
        time.sleep(1)
        gpio.output(pin, gpio.LOW)
        time.sleep(1)

if __name__ == "__main__":
    blink(26)
    gpio.cleanup()
