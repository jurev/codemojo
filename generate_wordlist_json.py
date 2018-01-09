import json
from collections import OrderedDict

words = open("english.txt").read().split()

D = OrderedDict()
D2 =OrderedDict()


def main():
    for i, word in enumerate(words):
        D["{0:011b}".format(i)] = word

    outfile = "english_reverse.json"
    open(outfile, "w").write(json.dumps(D, indent=4))
    print("wrote to {}".format(outfile))

    for bits, word in D.items():
        D2[word] = bits

    outfile = "english.json"
    open(outfile, "w").write(json.dumps(D2, indent=4))
    print("wrote to {}".format(outfile))


if __name__ == '__main__':
    main()
