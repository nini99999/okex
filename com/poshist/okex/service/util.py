import zlib

def encodeZlib(data):
    return zlib.decompress(data, -zlib.MAX_WBITS)