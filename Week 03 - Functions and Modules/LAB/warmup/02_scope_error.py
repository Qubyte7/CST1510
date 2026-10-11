# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status


print(check(87, 100))

# Status was declared inside the function, calling it outside the function not proper
# We have also to add return for us to get the results of the function call

