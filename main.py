#!/usr/bin/python3
import sys

def init(value):
    data = []
    while value != 0:
        data.append(value)
        value = value / 2
        value = int(value)
        if value == 0:
            break
    data.sort()
    for i in data:
        if i % 2 == 0 or i % 2 == 1:
            print(i % 2, end="")
    print("\n")
def main():
    try:
        if not "-B" in sys.argv[1].upper():
            print("[-] ./main.py -b [number]")
        elif "-B" in sys.argv[1].upper():
            init(int(sys.argv[2]))
    except IndexError:
        print("[-] ./main.py -b [number]")
main()
