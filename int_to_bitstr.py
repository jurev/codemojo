def int_to_bitstr(x, length=8):
    fmt = "{0:0%sb}" % length
    return fmt.format(x)
    
if __name__ == '__main__':
    import sys
    print(int_to_bitstr(int(sys.argv[1]), int(sys.argv[2])))
