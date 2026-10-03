"""
RECORD CHECK  -  my version
===========================

Name  : Yomna Alhajry
Lane  :  AI       (delete two)
Date  : 26-09-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

label = input("Enter label: ")  
first = float(input("Enter first value: "))  
second = float(input("Enter second value: "))  

print("=" * 20)
print(f"  RECORD CHECK  -  {label}")
print("=" * 20)
print(f"Used\t:{first}")
print(f"Total\t:{second}")
print("=" * 20)

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second

label = input("Enter label: ")  
first = float(input("Enter first value: "))  
second = float(input("Enter second value: "))  

difference = second - first  
percent = (first / second * 100) 

print("=" * 20)
print(f"  RECORD CHECK  -  {label}")
print("=" * 20)
print(f"Used        :   {first:>10.2f}")
print(f"Total       :   {second:>10.2f}")
print(f"Difference  :   {difference:>10.2f}")
print(f"Percentage  :   {percent:>10.2f}%")
print("=" * 20)

# difference always shows its sign, plus one line of your own

label = input("Enter label: ")  
first = float(input("Enter first value: "))  
second = float(input("Enter second value: "))  

difference = second - first  
percent = (first / second * 100) 
remainingPercent = 100 - percent  #useful line of your own

print("=" * 20)
print(f"  RECORD CHECK  -  {label}")
print("=" * 20)
print(f"Used        :   {first:>10.2f}")
print(f"Total       :   {second:>10.2f}")
print(f"Difference  :   {difference:>+10.2f}")  #show sign
print(f"Percentage  :   {percent:>10.2f}%")
print(f"Remaining   :   {remainingPercent:>10.2f}%") # useful line of your own
print("=" * 20)


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign


# : your report lines go here
'''Threshold : print the three values you were given, inside a border
====================
  RECORD CHECK  -  8y0
====================
Used    :20.0
Total   :40.0
====================

Typical   : add difference and percent, 2 decimal places, right-aligned
====================
  RECORD CHECK  -  ty7
====================
Used        :        76.00
Total       :        99.00
Difference  :        23.00
Percentage  :        76.77%
====================

Excellent : difference always shows its sign, plus one line of your own
====================
  RECORD CHECK  -  exx55
====================
Used        :        23.00
Total       :        90.00
Difference  :       +67.00
Percentage  :        25.56%
Remaining   :        74.44%
====================

'''


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you