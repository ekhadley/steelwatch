import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def blink(pin: int, count:int = 10):
    GPIO.setup(pin, GPIO.OUT)
    for _ in range(count):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(1)

if __name__ == "__main__":
    blink(26)
    GPIO.cleanup()
