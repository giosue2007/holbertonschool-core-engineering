#!/usr/bin/env python3
def uppercase(str):
    res = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            res += chr(ord(c) - 32)
        else:
            res += c
    print("{}".format(res))
