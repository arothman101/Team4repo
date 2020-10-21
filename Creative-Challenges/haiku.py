import numpy

#"determiner", "adjective" " noun" "verb"
word_dict = {"1" : [["The ", "A ","This "],
["big ","small ","drunk ","ill ","mad ","mean ","coy ","cringe "],
["moon ","wolf ","cat ","shrimp ","wood ", "man ","trunk ","pyre ","orb ","item "],
["real ","light ","trip "],
["hunts ","drowns ","dies ","spins ","sighs ","strikes ","pries ","waits "]],
"2" : [[],
["brazen ", "hollow ", "yummy ","moody ","mellow ","peaceful ","slimey ","mega ","perfect ","freaky "],
["woman ","forest ","lizard ","ninja "],
["slowly ","quickly "],
["attacks ","escapes ","watches ","observes "]],
"3": [[],
["masculine ","physical ","innocent ","tropical ","imperfect ","sporadic "],
["family ","potato ", "adventure ", "consonant ","jupiter ","mercury "],
["easily ", "powerful ","steadily ","wearily ", "heartily "],
["amplify ","edify "]]
}
 
import random
haiku = [5,7,5]
def getSyllables5():
  sentance = ""
  num = random.randint(1,3)
  sentance += random.choice(word_dict["1"][0])
  if num == 1:
    sentance += random.choice(word_dict["2"][1])
    sentance += random.choice(word_dict["1"][2])
    sentance += random.choice(word_dict["1"][4])
  elif num == 2:
    sentance += random.choice(word_dict["1"][1])
    sentance += random.choice(word_dict["2"][2])
    sentance += random.choice(word_dict["1"][4])
  elif num == 3:
    sentance += random.choice(word_dict["1"][1])
    sentance += random.choice(word_dict["1"][2])
    sentance += random.choice(word_dict["2"][4])
  print(sentance)

def getSyllables7():
  available = 7
  sentance = ""
  sentance += random.choice(word_dict["1"][0])
  available -= 1
  value = random.randint(1,available-4)
  available -= value
  sentance += random.choice(word_dict[str(value)][1])
  value = random.randint(1,available-3)
  available -= value
  sentance += random.choice(word_dict[str(value)][2])
  value = random.randint(1,available-1)
  available -= value
  sentance += random.choice(word_dict["2"][3])
  sentance += random.choice(word_dict[str(available)][4])
  print(sentance)

  


getSyllables5()
getSyllables7()
getSyllables5()











  
