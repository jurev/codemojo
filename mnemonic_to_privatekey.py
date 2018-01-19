"""

Given first N mnemonic words return known privatekey bits (if all 24 words present, also compute checksum)

"""

import sys
import json
from checksum import checksum
from int_to_bitstr import int_to_bitstr
from pprint import pprint

words = json.loads(open("english.json").read())
words_rev = json.loads(open("english_reverse.json").read())

def main(words24):
    bitstr = ""

    ret = {
        'decoded': [],
        'checksum_ok': False,
        'private_key_hex': None,
    }

    for i in range(24):
        word = None
        try:
            word = words24[i]
            bitstr += words[word]
            ret['decoded'].append((words[word], word))
        except:
            ret['decoded'].append(("???????????", "[missing word #%s]" % (i+1)))
        
    if (len(bitstr) == 264):
        if checksum(bitstr[:256]) == int(bitstr[256:], 2):
            ret['checksum_ok'] = True
                
        private_key = "{0:064x}".format( int(bitstr[:256], 2) )
        ret['privatekey_hex'] = private_key

        return ret

if __name__ == '__main__':
    pprint(main(sys.argv[1:]))

