def switcheroo (string1,char1,char2):
  list1 = []
  for char in string1:
    list1.append(char)
  for i in range(len(list1)):
    if list1[i] == char1:
      list1[i] = char2
    elif list1[i] == char2:
      list1[i] = char1
  word = ""
  for i in list1:
    word += i

  return(word)


print(switcheroo("veni, vidi, vici","v","i"))
