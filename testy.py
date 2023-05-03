import time
from rpi_ws281x import *
import argparse
from random import randint

# LED strip configuration:
LED_COUNT      = 144     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 100      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)
                
def randomColors(strip):
    
    for i in range(strip.numPixels()):
        R = randint(0,255)
        G = randint(0,255)
        B = randint(0,255)

        strip.setPixelColor(i, Color(R, G, B))
        strip.show()

def clearOff(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

def clearOn(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(255, 255, 255))
        strip.show()

def techSign(strip):
    for i in range(16):
        strip.setPixelColor(i, Color(0,0,0))
    for i in range(128,144):
        strip.setPixelColor(i, Color(0,0,0))
    for i in range(10):
        if i%2 == 0:
            for i in range(16,32):
                strip.setPixelColor(i, Color(0,0,255))
            for i in range(112,128):
                strip.setPixelColor(i, Color(0,0,255))
            
            # line 1
            strip.setPixelColor(33, Color(255,0,0))
            strip.setPixelColor(34, Color(255,0,0))
            strip.setPixelColor(35, Color(255,0,0))
            strip.setPixelColor(36, Color(0,0,255))
            strip.setPixelColor(37, Color(255,0,0))
            strip.setPixelColor(38, Color(255,0,0))
            strip.setPixelColor(39, Color(255,0,0))
            strip.setPixelColor(40, Color(0,0,255))
            strip.setPixelColor(41, Color(0,0,255))
            strip.setPixelColor(42, Color(255,0,0))
            strip.setPixelColor(43, Color(255,0,0))
            strip.setPixelColor(44, Color(0,0,255))
            strip.setPixelColor(45, Color(0,0,255))
            strip.setPixelColor(46, Color(255,0,0))
            strip.setPixelColor(47, Color(0,0,255))
            strip.setPixelColor(48, Color(255,0,0))

            # line 2
            strip.setPixelColor(49, Color(0,0,255))
            strip.setPixelColor(50, Color(255,0,0))
            strip.setPixelColor(51, Color(0,0,255))
            strip.setPixelColor(52, Color(0,0,255))
            strip.setPixelColor(53, Color(255,0,0))
            strip.setPixelColor(54, Color(0,0,255))
            strip.setPixelColor(55, Color(0,0,255))
            strip.setPixelColor(56, Color(0,0,255))
            strip.setPixelColor(57, Color(255,0,0))
            strip.setPixelColor(58, Color(0,0,255))
            strip.setPixelColor(59, Color(0,0,255))
            strip.setPixelColor(60, Color(255,0,0))
            strip.setPixelColor(61, Color(0,0,255))
            strip.setPixelColor(62, Color(255,0,0))
            strip.setPixelColor(63, Color(0,0,255))
            strip.setPixelColor(64, Color(255,0,0))

            # line 3
            strip.setPixelColor(65, Color(0,0,255))
            strip.setPixelColor(66, Color(255,0,0))
            strip.setPixelColor(67, Color(0,0,255))
            strip.setPixelColor(68, Color(0,0,255))
            strip.setPixelColor(69, Color(255,0,0))
            strip.setPixelColor(70, Color(255,0,0))
            strip.setPixelColor(71, Color(0,0,255))
            strip.setPixelColor(72, Color(0,0,255))
            strip.setPixelColor(73, Color(255,0,0))
            strip.setPixelColor(74, Color(0,0,255))
            strip.setPixelColor(75, Color(0,0,255))
            strip.setPixelColor(76, Color(0,0,255))
            strip.setPixelColor(77, Color(0,0,255))
            strip.setPixelColor(78, Color(255,0,0))
            strip.setPixelColor(79, Color(255,0,0))
            strip.setPixelColor(80, Color(255,0,0))

            # line 4
            strip.setPixelColor(81, Color(0,0,255))
            strip.setPixelColor(82, Color(255,0,0))
            strip.setPixelColor(83, Color(0,0,255))
            strip.setPixelColor(84, Color(0,0,255))
            strip.setPixelColor(85, Color(255,0,0))
            strip.setPixelColor(86, Color(0,0,255))
            strip.setPixelColor(87, Color(0,0,255))
            strip.setPixelColor(88, Color(0,0,255))
            strip.setPixelColor(89, Color(255,0,0))
            strip.setPixelColor(90, Color(0,0,255))
            strip.setPixelColor(91, Color(0,0,255))
            strip.setPixelColor(92, Color(255,0,0))
            strip.setPixelColor(93, Color(0,0,255))
            strip.setPixelColor(94, Color(255,0,0))
            strip.setPixelColor(95, Color(0,0,255))
            strip.setPixelColor(96, Color(255,0,0))

            # line 5
            strip.setPixelColor(97, Color(0,0,255))
            strip.setPixelColor(98, Color(255,0,0))
            strip.setPixelColor(99, Color(0,0,255))
            strip.setPixelColor(100, Color(0,0,255))
            strip.setPixelColor(101, Color(255,0,0))
            strip.setPixelColor(102, Color(255,0,0))
            strip.setPixelColor(103, Color(255,0,0))
            strip.setPixelColor(104, Color(0,0,255))
            strip.setPixelColor(105, Color(0,0,255))
            strip.setPixelColor(106, Color(255,0,0))
            strip.setPixelColor(107, Color(255,0,0))
            strip.setPixelColor(108, Color(0,0,255))
            strip.setPixelColor(109, Color(0,0,255))
            strip.setPixelColor(110, Color(255,0,0))
            strip.setPixelColor(111, Color(0,0,255))
            strip.setPixelColor(112, Color(255,0,0))
            
            
        else:
            for i in range(16,32):
                strip.setPixelColor(i, Color(255,0,0))
            for i in range(112,128):
                strip.setPixelColor(i, Color(255,0,0))
            
            # line 1
            strip.setPixelColor(33, Color(0,0,255))
            strip.setPixelColor(34, Color(0,0,255))
            strip.setPixelColor(35, Color(0,0,255))
            strip.setPixelColor(36, Color(255,0,0))
            strip.setPixelColor(37, Color(0,0,255))
            strip.setPixelColor(38, Color(0,0,255))
            strip.setPixelColor(39, Color(0,0,255))
            strip.setPixelColor(40, Color(255,0,0))
            strip.setPixelColor(41, Color(255,0,0))
            strip.setPixelColor(42, Color(0,0,255))
            strip.setPixelColor(43, Color(0,0,255))
            strip.setPixelColor(44, Color(255,0,0))
            strip.setPixelColor(45, Color(255,0,0))
            strip.setPixelColor(46, Color(0,0,255))
            strip.setPixelColor(47, Color(255,0,0))
            strip.setPixelColor(48, Color(0,0,255))

            # line 2
            strip.setPixelColor(49, Color(255,0,0))
            strip.setPixelColor(50, Color(0,0,255))
            strip.setPixelColor(51, Color(255,0,0))
            strip.setPixelColor(52, Color(255,0,0))
            strip.setPixelColor(53, Color(0,0,255))
            strip.setPixelColor(54, Color(255,0,0))
            strip.setPixelColor(55, Color(255,0,0))
            strip.setPixelColor(56, Color(255,0,0))
            strip.setPixelColor(57, Color(0,0,255))
            strip.setPixelColor(58, Color(255,0,0))
            strip.setPixelColor(59, Color(255,0,0))
            strip.setPixelColor(60, Color(0,0,255))
            strip.setPixelColor(61, Color(255,0,0))
            strip.setPixelColor(62, Color(0,0,255))
            strip.setPixelColor(63, Color(255,0,0))
            strip.setPixelColor(64, Color(0,0,255))

            # line 3
            strip.setPixelColor(65, Color(255,0,0))
            strip.setPixelColor(66, Color(0,0,255))
            strip.setPixelColor(67, Color(255,0,0))
            strip.setPixelColor(68, Color(255,0,0))
            strip.setPixelColor(69, Color(0,0,255))
            strip.setPixelColor(70, Color(0,0,255))
            strip.setPixelColor(71, Color(255,0,0))
            strip.setPixelColor(72, Color(255,0,0))
            strip.setPixelColor(73, Color(0,0,255))
            strip.setPixelColor(74, Color(255,0,0))
            strip.setPixelColor(75, Color(255,0,0))
            strip.setPixelColor(76, Color(255,0,0))
            strip.setPixelColor(77, Color(255,0,0))
            strip.setPixelColor(78, Color(0,0,255))
            strip.setPixelColor(79, Color(0,0,255))
            strip.setPixelColor(80, Color(0,0,255))

            # line 4
            strip.setPixelColor(81, Color(255,0,0))
            strip.setPixelColor(82, Color(0,0,255))
            strip.setPixelColor(83, Color(255,0,0))
            strip.setPixelColor(84, Color(255,0,0))
            strip.setPixelColor(85, Color(0,0,255))
            strip.setPixelColor(86, Color(255,0,0))
            strip.setPixelColor(87, Color(255,0,0))
            strip.setPixelColor(88, Color(255,0,0))
            strip.setPixelColor(89, Color(0,0,255))
            strip.setPixelColor(90, Color(255,0,0))
            strip.setPixelColor(91, Color(255,0,0))
            strip.setPixelColor(92, Color(0,0,255))
            strip.setPixelColor(93, Color(255,0,0))
            strip.setPixelColor(94, Color(0,0,255))
            strip.setPixelColor(95, Color(255,0,0))
            strip.setPixelColor(96, Color(0,0,255))

            # line 5
            strip.setPixelColor(97, Color(255,0,0))
            strip.setPixelColor(98, Color(0,0,255))
            strip.setPixelColor(99, Color(255,0,0))
            strip.setPixelColor(100, Color(255,0,0))
            strip.setPixelColor(101, Color(0,0,255))
            strip.setPixelColor(102, Color(0,0,255))
            strip.setPixelColor(103, Color(0,0,255))
            strip.setPixelColor(104, Color(255,0,0))
            strip.setPixelColor(105, Color(255,0,0))
            strip.setPixelColor(106, Color(0,0,255))
            strip.setPixelColor(107, Color(0,0,255))
            strip.setPixelColor(108, Color(255,0,0))
            strip.setPixelColor(109, Color(255,0,0))
            strip.setPixelColor(110, Color(0,0,255))
            strip.setPixelColor(111, Color(255,0,0))
            strip.setPixelColor(112, Color(0,0,255))
        
            
        strip.show()
        time.sleep(.2)



def update(strip, list):
    index = 0
    for i in range(strip.numPixels()):
        LEDcolor = list[i]
        color = LEDcolor.fill
        strip.setPixelColor(i, Color(*color))
        index += 1
    strip.show()


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            colorWipe(strip, Color(255,255,255))
            # theaterChase(strip, Color(0,128,128))
            # randomColors(strip)
            # rainbowCycle(strip)
            strip.show()
         
            

    except KeyboardInterrupt:
        colorWipe(strip, Color(0,0,0), 1)

