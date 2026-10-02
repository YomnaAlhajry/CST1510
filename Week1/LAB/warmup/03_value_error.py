# BROKEN ON PURPOSE.
# Run it, type 23.7 when asked, read the last line, then fix it.
'''
value = int(input("Value: "))

print(value)
'''
#The error is (value error) in line 6. The input returns a string, and you can't convert a string with a decimal to an integer.
# The correct code should be:
value = float(input('Value: '))
print(value)
