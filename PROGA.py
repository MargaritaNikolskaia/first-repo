import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(value):
  return [int(bit) for bit in bin(value)[2:].zfill(8)]

def bin2dac(value):
  signal = decimal2binary(value)
  GPIO.output(dac, signal)
  return signal
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
  while True:
    inputStr = input("Введите значение от 0 до 255(q для выхода) > ")
    
    if inputSt.isdigit():
      value = int(inputStr)
      if value >= levels:
        print("Значение слишком большое, попробуйте еще раз")
        continue
      signal = bin2dac(value)
      voltage = value/levels*maxVoltage
      print ("Введенное значение = {:3} -> {}, output voltage = {:.2f}".format(value, signal, voltage))
    elif inputStr == 'q':
      break
    else:
      print ("Введите положительное число")
except:
  pass
else:
  pass
finally:
  pass    
          
