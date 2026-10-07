# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = int(input("Value: "))

# we can't compare string to interger so casted the string to integer
if value > limit:
    print("OVER")
else:
    print("OK")
