def checksum(bitstr):
    chksum = 0
    for bit in bitstr:
        if bit == "1":
            chksum += 1
        chksum %= 256
    return chksum
        
if __name__ == '__main__':
    import sys
    print(checksum(sys.argv[1]))
