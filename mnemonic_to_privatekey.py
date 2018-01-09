"""

Given first N mnemonic words display known privatekey bits (if all 24 words present, also compute checksum)

>>> python self.py x y
00000111000 x
01100110010 y
??????????? [missing word #3]
??????????? [missing word #4]
...

>>> python self.py ...
...
checksum OK

Private key (hex):
0700e01c0380700e01c0380700e01c0380700e01c0380700e01c0380700e01c0

"""

import sys
import json
from checksum import checksum
from int_to_bitstr import int_to_bitstr

words = json.loads(open("english.json").read())
words_rev = json.loads(open("english_reverse.json").read())

def main(words24):
    bitstr = ""

    for i in range(24):
        word = None
        try:
            word = words24[i]
            bitstr += words[word]
            print(words[word], word)
        except:
            print("???????????", "[missing word #%s]" % (i+1))
        
    print()
    if (len(bitstr) == 264):
        if checksum(bitstr[:256]) == int(bitstr[256:], 2):
            print("checksum OK")
        else:
            print("checksum FAIL")
                
        print()
        print("Private key (hex):")
        private_key = "{0:064x}".format( int(bitstr[:256], 2) )
        print(private_key)
        return private_key

if __name__ == '__main__':
    main(sys.argv[1:])        

