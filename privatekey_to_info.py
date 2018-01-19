import logging
from pprint import pprint

from bitcash import Key

def main(privatekey):
    bytes = (int(privatekey, 16)).to_bytes(32, byteorder='big')    
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
        'wif': k and k.to_wif()
    }
    
if __name__ == '__main__':
    pprint(main(sys.argv[1:]))
