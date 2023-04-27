#!/usr/bin/env python3
import sys

def usage():
    print("Usage:    range start stop [file]")

def main():
    if len(sys.argv) < 3:
        usage()
    elif len(sys.argv) == 3:
        for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
            print(i)
    elif len(sys.argv) == 4:
        with open(sys.argv[3], "w") as f:
            for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
                f.write(str(i) + "\n");



if __name__ == '__main__':
    main()