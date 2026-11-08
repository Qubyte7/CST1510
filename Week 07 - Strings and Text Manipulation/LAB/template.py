"""
RECORD CHECK  -  my version
===========================

Name  :  (put your name here)
Lane  :  IT
Date  :  (put today's date here)

Run it:   python template.py
"""

# FUNCTIONS

def parse_line(raw_line):
    """Clean one messy line like '  Srv-01 , used=87 , total=100  ' into a tidy dict."""
    # strip + lowercase the whole line first, so spacing and case stop mattering
    cleaned = raw_line.strip().lower()

    # split on commas, the first piece is always the hostname
    pieces = cleaned.split(",")
    record = {"hostname": pieces[0].strip()}

    # every other piece looks like key=value, so split on "=" and strip each side
    for piece in pieces[1:]:
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())   # float() raises ValueError for text like "unknown"

    # a record with no used/total can't be checked, so treat it as bad too
    if "used" not in record or "total" not in record:
        raise ValueError("missing used or total")

    return record


def status_of(record):
    """Return OVER LIMIT, WARNING or OK depending on how full the server is."""
    # guard against total being 0 so we never divide by zero
    if record["total"] <= 0:
        return "OVER LIMIT"

    percent = record["used"] / record["total"] * 100

    # check the biggest threshold first, otherwise 105% would be caught by the 90% check
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# INPUT
# Now let us read from the file

raw_records = []
with open("messy_lines.txt") as file:
    for line in file:
        # skip blank lines, there's nothing to parse in them
        if line.strip() == "":
            continue
        raw_records.append(line)


# PROCESS and OUTPUT
# Parse every line, print the cleaned dict with its status, and keep count.

total_records = 0
flagged_count = 0
skipped_count = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
        status = status_of(record)

        print(record, "->", status)

        total_records += 1
        if status != "OK":      # anything that isn't OK counts as flagged
            flagged_count += 1

    except ValueError:
        # we catch the value error
        print("Could not parse:", raw_record.strip())
        skipped_count += 1

# one-line summary at the end
print(f"\nSummary: {total_records} records parsed, {flagged_count} flagged, {skipped_count} skipped.")

