from PyDictionary import PyDictionary
dict=PyDictionary()

word=input()
meaning=dict.meaning(word)
antonyms=dict.antonym(word)
synonyms=dict.synonym(word)

print("meaning : ",meaning)
print("Synonym : ",synonyms)
print("Antonym : ",antonyms)