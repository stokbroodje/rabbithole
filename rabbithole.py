#this programs lists words that are uncommon in a bulgarian text
#This is too help study for a text so when reading it will be a more enjoyable process
from load_data import Load
from collections import Counter

Loader = Load("tatoeba_bg_eng.tsv")
bg_words = Loader.bg_words
counts = Counter(bg_words)
print(counts)