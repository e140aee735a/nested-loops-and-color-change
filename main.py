from m5stack import *
from m5ui import *
from uiflow import *
import time

setScreenColor(0x111111)








while True:
  while not (btnA.isReleased()):
    setScreenColor(0x3366ff)
    wait(0.5)
    setScreenColor(0xff0000)
    wait(0.5)
  setScreenColor(0x000000)
  for count2 in range(3):
    for count in range(3):
      M5Led.on()
      wait(0.1)
      M5Led.off()
      wait(0.3)
    wait(0.5)
  for count3 in range(20):
    M5Led.on()
    wait_ms(20)
    M5Led.off()
    wait_ms(20)
  wait(0.5)
  wait_ms(2)
