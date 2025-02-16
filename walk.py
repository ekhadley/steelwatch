import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)


inpin = 26
outpin = 21
if __name__ == "__main__":
    gpio.setup(outpin, gpio.OUT)
    gpio.setup(inpin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

    while True:
        inval = gpio.input(inpin)
        print(inval)

    gpio.cleanup()

"""
 from metal side up on board-side connector, holes pointing forward:
far right:  wheel forward
1 from right: wheel backwards
3 from right: constant 3.3v?
4 from right: constant 3.3v?
motor seems to work without the constant 3.3v lines.
"""
