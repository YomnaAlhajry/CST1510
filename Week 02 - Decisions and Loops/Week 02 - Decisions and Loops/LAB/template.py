"""
RECORD CHECK  -  my version
===========================

Name  : Yomna Alhajry
Lane  :  AI       (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Enter label: ")      # replace with an input() call
used = float(input("Enter used: "))      # replace with an input() call, converted with float()
total = float(input("Enter total: "))    # replace with an input() call, converted with float()

if used > total:
    status = "OVER LIMIT"
else:
    status = "OK"
print('=' * 30)
print(f"Record check - {label}")
print('=' * 30)
print(f"Used        :{used:>10.2f}")
print(f"Total       :{total:>10.2f}")
print(f"Status      :{status:>10}")
print('=' * 30)

# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]
difference = 0.0   # replace with your calculation
percent = 0.0       # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

label = input("Enter label: ")      # replace with your if / else (or if / elif / else)
used = float(input("Enter used: "))      
total = float(input("Enter total: "))
difference = total - used
percent = (used / total) * 100    

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"
print('=' * 30)
print(f"Record check - {label}")
print('=' * 30)
print(f"Used        :{used:>10.2f}")
print(f"Total       :{total:>10.2f}")
print(f"Difference  :{difference:>10.2f}")
print(f"Percent     :{percent:>10.2f}%")
print(f"Status      :{status:>10}")
print('=' * 30)   
# ===================================================================
over_limit = 0
while True:
    label = input("Enter label (or 'quit' to exit): ")
    if label == "quit":
        break
    used = float(input("Enter used: "))      
    total = float(input("Enter total: "))
    difference = total - used
    percent = (used / total) * 100    

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    
    print('=' * 30)
    print(f"Record check - {label}")
    print('=' * 30)
    print(f"Used        :{used:>10.2f}")
    print(f"Total       :{total:>10.2f}")
    print(f"Difference  :{difference:>10.2f}")
    print(f"Percent     :{percent:>10.2f}%")
    print(f"Status      :{status:>10}")
    print('=' * 30)
print(f"Number of records OVER LIMIT: {over_limit}")

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.


# your report lines go here
'''
THRESHOLD
==============================
Record check - sr03
==============================
Used    :     234.0
Total   :     120.0
Status  :OVER LIMIT
==============================

TYPICAL
==============================
Record check - 102
==============================
Used        :    120.00
Total       :    120.00
Difference  :      0.00
Percent     :    100.00%
Status      :OVER LIMIT
==============================




'''

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
