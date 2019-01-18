#!/usr/bin/python3

import string
import random


def verify(pswd: str) -> bool:
    letters = string.ascii_uppercase + string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    for ch in letters:
        if pswd.count(ch) > 0:
            break
    else:
        return False

    for ch in digits:
        if pswd.count(ch) > 0:
            break
    else:
        return False

    for ch in special:
        if pswd.count(ch) > 0:
            break
    else:
        return False

    return True


def gen_pswd() -> str:
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))


pswd = ''
while True:
    pswd = gen_pswd()
    if verify(pswd):
        break

print(pswd)
