#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            str1 += chr(ord(str[i]) - 32)
        else:
            str1 += str[i]
    print("{}".format(str1))
