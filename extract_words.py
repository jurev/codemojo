"""

Given a text, return words that are the mnemonic candidates. 

"""

import sys
import json
import re
from pprint import pprint

words = json.loads(open("english.json").read())
words_rev = json.loads(open("english_reverse.json").read())

def main(text):
    ret = []
    for word in text.split():
        word = word.strip().lower()
        word = re.sub(r"\W", "", word)
        if word in words:
            ret.append(word)

    return ret
    
if __name__ == '__main__':
    pprint(main(open(sys.argv[1]).read()))
    
