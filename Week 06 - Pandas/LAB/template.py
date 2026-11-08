"""
RECORD CHECK  -  my version
===========================

Name  :  (put your name here)
Lane  :  IT
Date  :  (put today's date here)

Run it:   python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt   # needed for the bar chart at the end

# LOAD
# I'm going with the IT lane, so my CSV has hostname, used_gb and total_gb.
# I made it_records.csv myself with 8 servers so there's a mix of OK,
# WARNING and OVER LIMIT rows to test with.

df = pd.read_csv("it_records.csv")


# PROCESS
# percent = how much of the disk is used.
#I round to 2 decimals so it's easier to read.
df["percent"] = ((df["used_gb"] / df["total_gb"]) * 100).round(2)

# status column: I used a lambda with .apply()
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)


# OUTPUT
# Show the whole table first, with the new percent and status columns.
print("Full table:")
print(df)

# Now only the servers that need attention, anything that isn't "OK".

print("\nServers that are not OK:")
print(df[df["status"] != "OK"])

# Count how many servers fall into each status.
# groupby("status") sorts the rows into groups, then .count() counts them.
counts = df.groupby("status")["hostname"].count()
print("\nCount per status:")
print(counts)

# Save the full DataFrame (with the extra columns) to a new CSV.
df.to_csv("it_records_checked.csv", index=False)

# Bar chart of the counts, saved as a PNG.
counts.plot(kind="bar")
plt.title("Servers per status")
plt.xlabel("Status")
plt.ylabel("Number of servers")
plt.xticks(rotation=0)       # keeps the labels flat so they're readable
plt.tight_layout()           # stops the labels getting cut off
plt.savefig("status_counts.png")
plt.close()                  # tidy up so the chart doesn't hang around in memory
print("\nSaved it_records_checked.csv and status_counts.png")


# ==========================================================================
# Hand check (srv-02): 115 / 120 = 0.9583, so * 100 = 95.83%.
# That's 90% or more but under 100%, so the status should be WARNING.
# It matches what the table shows.