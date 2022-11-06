import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet
from random import randint

word=input()
synonyms = []
antonyms=[]
n=randint(0,5)
for i in wordnet.synsets(word):
    for j in i.lemmas():
      synonyms.append(j.name())
for i in wordnet.synsets(word):
    for j in i.lemmas():
      if j.antonyms():
        antonyms.append(j.antonyms()[0].name())
               
print ("synonym : ",synonyms[n])
print("antonym : ",antonyms[n])