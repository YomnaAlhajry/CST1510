# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
''''
value = input("Value: ")

print(value + 1)
'''
#The error is (type error) in line 6. The input returns a string, and you can't add an integer to a string.
# The correct code should be:
value = int(input("Value: "))
print(value + 1)
