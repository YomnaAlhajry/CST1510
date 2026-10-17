"""
RECORD CHECK  -  my version
===========================

Name  : Yomna Alhajry
Lane  :  AI     (delete two)
Date  : 16-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """returns the differenc, percent, and status"""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """This holds all the print commands in one record"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Value:   {value:>10.2f}")
    print(f"Limit:   {limit:>10.2f}")
    print(f"difference:   {difference:>10.2f}")     
    print(f"Percent:   {percent:>10.2f}%")       
    print(f"Status:   {status}")
    print("=" * 34)
 
def load_records(path):
    """label, value, limit, lines from files, then return list of dict or [] if not found"""
    try:
        records = []       # defining (records) in this function
        with open(path) as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                records.append({
                    "label": label, 
                        "value": float(value),
                        "limit": float(limit)
                        })
        return records
            
    except FileNotFoundError:
        print("File doesn't exist")
        return[]
# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

MODE = "threshold"
if MODE == "threshold":
    records = [
        {"label": "R-001", "value": 87.0, "limit": 100.0},
        {"label": "R-002", "value": 120.0, "limit": 100.0},
        {"label": "R-003", "value": 45.0, "limit": 100.0},
   ]
elif MODE == "typical":
    records = load_records("records_test.txt")

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
# used for loop so it goes through the dicts in the file 
for rec in records:
    difference, percent, status = check_record(rec["value"], rec["limit"])
    print_report(rec["label"], rec["value"], rec["limit"], difference, percent, status)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
"""
==================================
  RECORD CHECK  -  R-001
==================================
Value:        87.00
Limit:       100.00
difference:       -13.00
Percent:        87.00%
Status:   OK
==================================

==================================
  RECORD CHECK  -  R-002
==================================
Value:       120.00
Limit:       100.00
difference:        20.00
Percent:       120.00%
Status:   OVER LIMIT
==================================

==================================
  RECORD CHECK  -  R-003
==================================
Value:        45.00
Limit:       100.00
difference:       -55.00
Percent:        45.00%
Status:   OK
==================================




"""