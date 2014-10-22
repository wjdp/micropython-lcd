# micropython-lcd

A simple class for controlling the HD44780 in 4 bit mode with the micropython
pyboard.

There are **no external dependences**, the only module we use is the pyboard's
`pyb`.

## Usage

```
import pyb
from lcd import HD44780

lcd = HD44780()

lcd.PINS = ['Y1','Y2','Y3','Y4','Y5','Y6']

lcd.init()

lcd.set_line(0) # First line
lcd.set_string("ABCDEFGHIJKLMNOP") # Send a string
lcd.set_line(1) # Second line
lcd.set_string("1234567890123456") # Again

pyb.delay(3000) # 3 second delay

lcd.clear() # Clear the display
```

## Pinout

Hookup your LCD like the following.

![Pinout photo][pinout]

|Pin |Code    |Description         |Do what with it                     |
|----|--------|--------------------|------------------------------------|
|1   |VSS     |GND                 |Ground it                           |
|2   |VDD     |+5V                 |5V please                           |
|3   |V0      |Contrast (0-5V)*    |Stick to 0V if you don't have a pot |
|4   |RS      |Register select     |Connect to pyboard, 0 in array      |
|5   |R/W     |Read/write          |Ground it                           |
|6   |E       |Enable              |Connect to pyboard, 1 in array      |
|7   |DB0     |Data Bit 0          |Unused                              |
|8   |DB1     |Data Bit 1          |Unused                              |
|9   |DB2     |Data Bit 2          |Unused                              |
|10  |DB3     |Data Bit 3          |Unused                              |
|11  |DB4     |Data Bit 4          |Connect to pyboard, 2 in array      |
|12  |DB5     |Data Bit 5          |Connect to pyboard, 3 in array      |
|13  |DB6     |Data Bit 6          |Connect to pyboard, 4 in array      |
|14  |DB7     |Data Bit 7          |Connect to pyboard, 5 in array      |
|15  |A       |Backlight +someV    |My display is LED, I use 3.3V       |
|16  |K       |Backlight GND       |Ground it                           |

Then the pinout array looks like this

    PINS = ['Y1','Y2','Y3','Y4','Y5','Y6']

[pinout]:http://cdn.instructables.com/FMC/PZRT/G8LWOHW9/FMCPZRTG8LWOHW9.MEDIUM.jpg
