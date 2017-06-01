import sys

codecs = [
    'utf_8',
    'utf_16',
    'utf_16_be',
    'utf_16_le',
    'utf_7',

    'gb2312',
    'gbk',
    'gb18030',
    'hz',
]

def str_to_hex(str):
    str_buffer = buffer(str)
    r = ''
    for b in str_buffer:
        r += hex(ord(b)) + ' '

    return r


def encode(str_to_encode, str_encoding):
    str_unicode = str_to_encode.decode(encoding=str_encoding)

    print 'codec: ' + 'unicode'
    print '    encoded hex: ' + str_to_hex(str_unicode)

    for c in codecs:
        str_encoded = str_unicode.encode(encoding=c)
        print 'codec: ' + c
        print '    encoded hex: ' + str_to_hex(str_encoded)


if __name__ == '__main__':
    args = sys.argv[1:]
    str_to_encode = args[0]
    if len(args) == 2:
        str_encoding = args[1]
    else:
        str_encoding = 'utf-8'

    encode(str_to_encode, str_encoding)

