"""
RECORD CHECK  -  my version
===========================

Name  : Yomna ALhajry
Lane  :  AI       (delete two)
Date  : 9/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
# threshold
def status_of(percent):
    """it returns the status based on the value of the percent"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
# Typical
def check(value, limit):
    """it returns the difference and percentage"""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent
# Excellent
def print_report(label, value, limit, difference, percent, status):
    """This holds all the print commands in one record"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Used:   {value:>10.2f}")
    print(f"Total:   {limit:>10.2f}")
    print(f"Free:   {difference:>10.2f}")      # added for the typical
    print(f"Percent:   {percent:>10.2f}%")      # added for the typical 
    print(f"Status:   {status}")
    print("=" * 34)
# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

# threshold, typical
#label = input("Enter label: ")      
#value = float(input("Enter value: "))     
#limit = float(input("Enter limit: "))      


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

# threshold
#difference, percent = check(value, limit)   # added for the typical
#status = status_of(percent)         


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

over_count = 0
while True:
    label = input("Enter label or 'quit' to stop:   ")
    if label == "quit":
        break
    value = float(input("Enter value: "))     
    limit = float(input("Enter limit: "))  
    difference, percent = check(value, limit)   # added for the typical
    status = status_of(percent)  

    print_report(label, value, limit, difference, percent, status) #call print_report()
    if status == "OVER LIMIT":
        over_count += 1

print(f"Num of OVER LIMIT:  {over_count}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
""""
==================================
  RECORD CHECK  -  srv-01
==================================
Used:       128.00
Total:       120.00
Free:        -8.00
Percent:       106.67%
Status:   OVER LIMIT
==================================
Enter label or 'quit' to stop:   quit
Num of OVER LIMIT:  1
"""