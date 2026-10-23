"""
RECORD CHECK  -  my version
===========================

Name  :  Yomna Alhajry
Lane  :  AI       (delete two)
Date  :  22-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    def __init__(self, label, value, limit):
        """Store a record's label, value, and limit."""
        self.label = label
        self.value = float(value)
        self.limit = float(limit)

    def status(self):
        """this returns the status of each record"""    # docstring
        prct = (self.value / self.limit) * 100
        if prct >= 100:
            return "OVER LIMIT"
        elif prct >= 90:
            return "WARNING"
        else: 
            return "OK"

# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

def load_records(path):
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records
#added the file path
records = load_records("C:\\Users\\yomna\\Downloads\\CST1510-1\\Week 05 - Classes and Objects\\Week 05 - Classes and Objects\\LAB\\records_sample.txt")
over_limit = 0
# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)
for record in records:
    status = record.status()
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here
    print(f"  value  :  {record.value}")
    print(f"  limit  :  {record.limit}")
    print(f"  status  :  {status}")
    if status == "OVER LIMIT":
        over_limit += 1

    print("=" * 34)

print(f"{over_limit} of {len(records)} were over limit")

# ==========================================================================
# 4. Before you finish:
"""
==================================
  RECORD CHECK  -  R-001
==================================
  value  :  87.0
  limit  :  100.0
  status  :  OK
==================================

==================================
  RECORD CHECK  -  R-002
==================================
  value  :  120.0
  limit  :  100.0
  status  :  OVER LIMIT
==================================

==================================
  RECORD CHECK  -  R-003
==================================
  value  :  45.0
  limit  :  100.0
  status  :  OK
==================================
1 of 3 were over limit
"""
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
