"""

Given 23 mnemonic words display options for the last, 24th word (3bits + 8bit checksum)

>>> python self.py alpha alpha alpha alpha alpha alpha alpha alpha alpha alpha alpha alpha alpha alpha
                   alpha alpha alpha alpha alpha alpha alpha alpha alpha
...
word 24 candidates:
00000110000 alcohol
00100110001 change
01000110001 economy
01100110010 green
10000110001 mail
10100110010 play
11000110010 shock
11100110011 toy

"""

import sys
import json
from checksum import checksum
from int_to_bitstr import int_to_bitstr

words = json.loads(open("english.json").read())
words_rev = json.loads(open("english_reverse.json").read())

def main(words23):
    bitstr253 = ""
    for word in words23:
        print(words[word], word)
        bitstr253 += words[word]
        
    print()
    print(bitstr253)


    print()
    print("word 24 candidates:")
    for i in range(8):
        chunk3 = "{0:03b}".format(i)
        tmp256 = bitstr253 + chunk3
        chk8 = int_to_bitstr(checksum(tmp256))    
        
        print(chunk3 + chk8, words_rev[chunk3 + chk8])
        
if __name__ == '__main__':
    main(sys.argv[1:])
    
