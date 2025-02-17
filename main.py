#!/usr/bin/env python3

import sys

print(sys.argv)

args = sys.argv
filename = ""

if len(args) <= 1:
    print("No argument provided")
    sys.exit()

del args[0]
filename = "_".join(args)

with open(f"{filename}.py", "w") as file:
    pass

