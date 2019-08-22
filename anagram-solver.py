from collections import Counter
import re

with open("words.txt") as f:
    words = f.read().splitlines()  # From: https://stackoverflow.com/a/3925701/3806231

    words_letters = [(word, Counter(re.sub(r"[^a-zA-Z0-9]", "", word.lower()))) for word in words]
