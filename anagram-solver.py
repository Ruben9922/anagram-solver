from collections import Counter

with open("words.txt") as f:
    words = f.read().splitlines()  # From: https://stackoverflow.com/a/3925701/3806231

    words_letters = [(word, Counter(word)) for word in words]
