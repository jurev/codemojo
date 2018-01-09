"""

Generate first 23 words for your mnemonic.

"""

import sys
import json
import random

words = json.loads(open("english.json").read())
words_rev = json.loads(open("english_reverse.json").read())

def main():
    selected = []

    count = 0
    while True:
        word = random.choice(list(words))
        if input(word + "? [y/N] ").lower() == "y":
            count += 1
            selected.append(word)
        if count >= 23:
            break
            
    print()
    print("Your 23 words:")
    print(" ".join(selected))
    
    return selected

if __name__ == '__main__':
    main()
