#!/usr/bin/env python3
# Created by: Declan.Moher
# Created on: Nov. 20, 2023
# This program checks


def main():
    # is going though the numbers 1000-1999
    for counter in range(1000, 2000):
        if counter == 1000:
            print(f"{counter} ", end="")
        # if counter is divisible by 5
        elif counter % 5 == 0:
            # print counter with the curser on the same line
            print(f"\n {counter} ", end="")
        # otherwise print other numbers all on the same line
        else:
            print(f"{counter} ", end="")


if __name__ == "__main__":
    main()
