from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

#SW0
btn1 = Pin(9, Pin.IN, Pin.PULL_UP)
#SW2
btn2 = Pin(7, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
#Display size
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

#ufo declaration, position and colour
x = 0
y = 45
colour = 1
ufo = "<=>"

#Ufo width is 3 characters * 8 pixels = 24
#Len ufo = 3
ufo_width = len(ufo) * 8
while True:
    
    #If sw0 is pressed the ufo moves to the right    
    if btn1() == 0:
        oled.fill(0)
        oled.text(ufo, x, y, colour)
        oled.show()
        x += 1
        if x >= (oled_width - ufo_width):
            x = oled_width - ufo_width
            y += 1
            if y >= 48:
                y = 48
    
    #If sw2 is pressed the ufo moves to the left
    if btn2() == 0:
        oled.fill(0)
        oled.text(ufo, x, y, colour)
        oled.show()
        x -= 1
        if x <= 0:
            x = 0
            y -= 1
            if y <= 0:
                y = 0
            
        
        

