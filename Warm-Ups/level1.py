Array1 = ["qwgdg, etyfgdhfhgjfc sdfsdf sdfsdf. dfhfghsf","sdfkh,.,sd.,fsd."]

def longest_word(array):
  word = ""
  list1 = []
  for i in array:
    if i.lower() in list(string.punctuation):
      list1.append(word)
      word = ""
    else:
      word += i

def min_max_product(array):
  return (min(Array1)*max(Array1))

print(min_max_product(Array1))
