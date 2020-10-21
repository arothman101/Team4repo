import string

array1 = ["qwgdg etfgdhfhgjfc sdfsdf sdfsdf. dfhfghsf sdfkhd.,fs."]


def longest_word(array1):
  word = ""
  list1 = []
  for i in array1:
    if i in list(string.punctuation) or i == " ":
      list1.append(word)
      word = ""
    else:
      word += i
  longestword = ""
  for i in list1:
    if len(i) > len(longestword):
      longestword = i


  return longestword

print(max(longest_word(array1[0])))
