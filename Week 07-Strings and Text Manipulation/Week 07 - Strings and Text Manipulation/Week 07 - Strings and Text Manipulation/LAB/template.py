"""
RECORD CHECK  -  my version
===========================

Name  : Yomna Alhajry
Lane  :  AI 
Date  :  12th, Nov, 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    rawline = raw_line.strip()
    hostname_part, rest = raw_line.split(",", 1)
    hostname = hostname_part.strip().lower()

    record = {"hostname": hostname}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip().lower()] = float(value.strip())

    return record

def status_of(rating):
    if rating >= 15:
        status = "OVER LIMIT"
    elif rating >= 10:
         status = "WARNING"
    else:
        status = "OK"

    return rating 

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

with open("C:\\Users\\yomna\\Downloads\\CST1510-1\\records_test.txt") as f:
    record_count = 0
    for raw_line in f:
        record = parse_line(raw_line)
        status = status_of(record["rating"])

        print(record, status)

        record_count += 1
print(f"\nRecords: {record_count}")

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
