# Example on usage of the HD44780 module

# Pin Code    Description         Do what with it
# -------------------------------------------------------------------
# 1   VSS     GND                 Ground it
# 2   VDD     +5V                 5V please
# 3   V0      Contrast (0-5V)*    Stick to 0V if you don't have a pot
# 4   RS      Register select     Pin 0
# 5   R/W     Read/write          Ground it
# 6   E       Enable              Pin 1
# 7   DB0     Data Bit 0          Unused
# 8   DB1     Data Bit 1          Unused
# 9   DB2     Data Bit 2          Unused
# 10  DB3     Data Bit 3          Unused
# 11  DB4     Data Bit 4          Pin 2
# 12  DB5     Data Bit 5          Pin 3
# 13  DB6     Data Bit 6          Pin 4
# 14  DB7     Data Bit 7          Pin 5
# 15  A       Backlight +someV    My display is LED, I use 3.3V
# 16  K       Backlight GND       Ground it


import pyb
from lcd import HD44780

def lcd_fun():
  # Main program block
  lcd = HD44780()

  # Pins 0-5 as above
  PINS = ['Y1','Y2','Y3','Y4','Y5','Y6']

  # Initialise display
  lcd.init()

  # Use it
  lcd.set_line(0) # First line
  lcd.set_string("ABCDEFGHIJKLMNOP") # Send a string
  lcd.set_line(1) # Second line
  lcd.set_string("1234567890123456") # Again

  pyb.delay(30) # 3 second delay

  # Send some more
  lcd.set_line(0)
  lcd.set_string("*micropython-lcd")
  lcd.set_line(1)
  lcd.set_string("github.com/wjdp")

  pyb.delay(3000)

  # Done
  lcd.clear()
