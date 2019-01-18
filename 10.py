#!/usr/bin/env python3

import sys

def encode(img_file: str, msg: str) -> None:
    if sys.getsizeof(msg) > 160: raise ValueError('Not support message')
    msg_list = ''.join(msg.split())

    (result, raw_msg) = ([], [])
    pointer = 300
    img = open(img_file, 'rb+')
    for word in msg_list: raw_msg += list(format(ord(word), 'b'))
    img.seek(pointer)
    img_bytes = list(img.read(len(raw_msg)))
    result += [img_bytes[_] - int(raw_msg[_]) for _ in range(0, len(img_bytes))]
    img.seek(pointer)
    for _ in result: img.write(chr(_).encode('ISO-8859-1'))
    img.flush()
    img.close()

encode(input("Input filename: "), input("Input your message: "))
