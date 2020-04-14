import sys


args = len(sys.argv)
i = 0
errtext = ["InputError:", "too many arguments",
           "too few arguments", "only numbers"]
if args == 1:
    i = 4
elif args > 3:
    i = 1
elif args < 3:
    i = 2
elif (not(sys.argv[1].isdecimal()) or not(sys.argv[2]).isdecimal()):
    i = 3

if i != 0:
    if i is not 4:
        print(f"{errtext[0]} {errtext[i]}\n")
    print('''Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3''')
    sys.exit()
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f"Sum:        {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product:    {a * b}")
    print(f"Quotient:   ", end="")
    print(f"{a / b}" if b != 0 else "ERROR (div by zero)")
    print(f"Remainder:  ", end="")
    print(f"{a % b}" if b != 0 else "ERROR (modulo by zero)")
