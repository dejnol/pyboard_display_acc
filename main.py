import pyb
from pyb import Pin, ADC
from ssd1306 import SSD1306

accel = pyb.Accel()
adc = ADC(Pin('X22'))
display = SSD1306(pinout={'sda': 'Y10','scl': 'Y9'},height=64,external_vcc=False)

def sw_callback():
  led_green.toggle()
  print("ButtonPressed")
 
sw = pyb.Switch()
sw.callback(sw_callback)

led_red = pyb.LED(1)
led_red.off()

led_green = pyb.LED(2)
led_green.on()

led_orange = pyb.LED(3)
led_orange.on()

try:
  display.poweron()
  display.init_display()
  
  display.draw_text(32,21,'X')
  display.draw_text(64,56,'Y')
  
  display.set_pixel(1,1,True)
  
  print("printdebug")
  
  for x in range(40,84):
    display.set_pixel(x,6,True)
    display.set_pixel(x,50,True)
    
  for y in range(6,50):
    display.set_pixel(40, y,True)
    display.set_pixel(84, y,True)
    
  while True:
    display.set_pixel(63 - accel.x(), 30 - accel.y(), True)
    display.draw_text(100,1,str(adc.read()))
    display.display()
    
except Exception as ex:
  led_red.on()
  print('Unexpected error: {0}'.format(ex))
  display.poweroff()

 
