def RomanToArabic(Ramon):
  num = 0
  for char in Ramon:
    if char.upper() == "M":
      num += 1000
    elif char.upper() == "D":
      num += 500
    elif char.upper() == "C":
      num += 100
    elif char.upper() == "L":
      num += 50
    elif char.upper() == "X":
      num += 10
    elif char.upper() == "V":
      num += 5
    elif char.upper() == "I":
      num += 1
    else:
      pass
  print(num)

roman = input("Enter a roman numeral: ")
RomanToArabic(roman)
