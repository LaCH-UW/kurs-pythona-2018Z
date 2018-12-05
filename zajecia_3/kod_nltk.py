import nltk  # sytuacja jak z reequests - powinnismy zainstalować nltk
nltk.download('punkt')  # przed pierwszym użyciem musimy ściągnąć paczkę z tokenizerami

from nltk.tokenize import sent_tokenize, word_tokenize


with open('dane/lalka-tom-drugi.txt', encoding='utf-8') as fp:
   tekst = fp.read()


s = sent_tokenize(tekst, language='polish')
print(s[:10])

w = word_tokenize(tekst, language='polish')
print(w[:20])
