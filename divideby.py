def divideby(number):
  try:
    print(str(42/int(number)))
  except ZeroDivisionError:
    print('Error: Invalid arguement')
  
divideby(10)  
divideby(6)
divideby(0)
divideby(3)
