# Terrible Programming Language Interpreter
# jdev082, MIT License 2023
# It's in the name, don't bother.
import sys

ERRS = ["MISSING_ARGS", "UNSUPPORTED_FILE_TYPE", "MISSING_ARGTYPE_IDENTIFIER", "VAR_UNDEFINED"]
RT_VARS = [""]

def err(code):
    print(f"ERR: {ERRS[code]}")
    exit()

if len(sys.argv[1:]) < 1:
    err(0)
    exit()

def intrp(lcont):
    if line[:2] == "pr":
        if (line[3] == ":"):
            try:
                l = line.replace(":", (RT_VARS[int(line[4:6])]))
            except IndexError:
                err(3)
            print(l[3:])
        else:
            print(line[3:])
    if line[:2] == "dv":
        VAR = line[3:6]
        RT_VARS[int(VAR)] = line[6:]
    

with open(sys.argv[1]) as f:
    for line in f:
        intrp(line)

