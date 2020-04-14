import sys

args = ' '.join(sys.argv[1:])
result = ""
i = len(args) - 1
while i >= 0:
    if args[i].isupper():
        result += args[i].lower()
    elif args[i].islower():
        result += args[i].upper()
    else:
        result += args[i]
    i -= 1

print(result)
