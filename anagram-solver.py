from collections import Counter, defaultdict
import re

with open("words.txt") as f:
    words = f.read().splitlines()  # From: https://stackoverflow.com/a/3925701/3806231

    words_letters = [(word, frozenset(Counter(re.sub(r"[^a-zA-Z0-9]", "", word.lower())).items())) for word in words]

    letters_word_dict = defaultdict(set)
    for item in words_letters:
        letters_word_dict[item[1]].add(item[0])

    s = input("Enter string: ")
    s_letters = frozenset(Counter(re.sub(r"[^a-zA-Z0-9]", "", s.lower())).items())
    print(letters_word_dict[s_letters])
