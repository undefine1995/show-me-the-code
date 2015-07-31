#-*coding:utf-8*-

import string
from random import choice

def bease():
    return string.ascii_uppercase+string.digits

def work():
    while True:
        yield ''.join(choice(bease()) for num in range(21))

def main():
    result = set()
    for code in work():
        if len(result) < 200:
            result.add(code)
        else:
            break

    for item in result:
        print item

if __name__ == '__main__':
    main()