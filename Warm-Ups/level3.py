def evenish_oddish(num=str(input("Enter a number: "))):
  summation = 0
  for i in range(len(num)):
    summation += int(num[i])
  if summation % 2 == 0:
    print("Evenish")
  else:
    print("Oddish")
 
evenish_oddish()
    
