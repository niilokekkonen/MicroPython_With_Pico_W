from machine import Pin, ADC
import time as t

#Accessing the led on the pico.
led = Pin("LED", Pin.OUT)

#Accessing the potentiometer, on pin 27 (ADC-1). 
pot = ADC(Pin(27))

#Converting the 16bit ADC reading (0-65535) into a voltage (0V-3.3V)
conversion_factor = 3.3 / 65535

while True:
    
    #Reading the ADC from pin 27(ADC-1)
    ADC = pot.read_u16() * conversion_factor
    
    #Defining maximum ADC value.
    ADC_MAX = 3.3
    
    #Delay between 0-1 second
    delay = ADC/ADC_MAX
    print(ADC)
    
    #LED functionality
    led.on()
    t.sleep(delay)
    led.off()
    t.sleep(delay)
        