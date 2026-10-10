# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status

num = check(87, 100)

print(num)

#I added the return, so it returns the status and stores its data in the num variable