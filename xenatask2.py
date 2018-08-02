import random

randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)]) 
randomPhrase 
reversePhrase = randomPhrase[::-1] 
print(reversePhrase)
