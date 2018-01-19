import logging
from pprint import pprint
import textwrap
import json
import sys
from bitcash import Key

from checksum import checksum
from int_to_bitstr import int_to_bitstr

words_rev = json.loads(open("english_reverse.json").read())

def bitstr_to_mnemonic(bitstr):
    assert(len(bitstr) == 256), "Bad bitstr size: %s" % len(bitstr)
    mnemonic = []
    for bits in textwrap.wrap(bitstr, 11):
        if len(bits) != 11:
            bits += int_to_bitstr(checksum(bitstr))
        mnemonic.append(words_rev[bits])
    return mnemonic

def main(privatekey):
    if len(privatekey) == 256:
        bytes = (int(privatekey, 2)).to_bytes(32, byteorder='big')    
    elif len(privatekey) == 64:
        bytes = (int(privatekey, 16)).to_bytes(32, byteorder='big')    
    else:
        raise(Exception('wrong privatekey length: %s' % len(privatekey)))
    k = None
    balance = None
    try:
        k = Key.from_bytes(bytes)
        balance = k.get_balance()
    except Exception as e:
        logging.warn(e)
    
    return {
        'key': k,
        'address': k and k.address,
        'balance': balance,
        'wif': k and k.to_wif(),
        'mnemonic': " ".join(bitstr_to_mnemonic("".join(bin(x)[2:].zfill(8) for x in bytes)))
    }
    
if __name__ == '__main__':
    pprint(main(sys.argv[1]))
