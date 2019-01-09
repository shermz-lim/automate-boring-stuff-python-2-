import random

words = []
dicFileObj = open('dictionary.txt', 'r')
for word in dicFileObj.readlines():
    words.append(word[:-1])
    words.append(word[:-1].lower())
dicFileObj.close()    

random.shuffle(words)
print(words)