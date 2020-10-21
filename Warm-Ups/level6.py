def cipher(word, jumps):
  encryption = ""
  for char in word:
    pos = ord(char)
    for i in range(jumps):
      pos += 1
      if pos > 122:
        pos -= 26
    encryption += chr(pos)
  return encryption

word = str(input("Enter a word: "))
jumps = int(input("Enter the number of jumps: "))

print(cipher(word.lower(), jumps))
