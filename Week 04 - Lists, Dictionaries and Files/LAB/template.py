

# FUNCTIONS

def check_record(value, limit):
    """Figure out how far past (or under) the limit we are, and what our status is."""
    diff = value - limit
    pct = (value / limit) * 100 if limit > 0 else 0
    status = "OVER LIMIT" if value > limit else "OK"
    return diff, pct, status


def print_report(label, diff, pct, status):
    """Print out a nice, readable status report for a single server."""
    print(f"Host: {label:<8}  Usage: {pct:5.2f}% {diff:+.1f} GB  Status: {status}")


def load_records(path):
    """Safely open up our data file and read each line into a handy list of dicts."""
    records = []
    try:
        with open(path, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    label, value, limit = parts
                    records.append({
                        "label": label.strip(),
                        "value": float(value),
                        "limit": float(limit)
                    })
    except FileNotFoundError:
        print("File not found, Please provide a valide file path")
    return records

# I created it_records.txt to use for our case
records = load_records("it_records.txt")

over_limit_count = 0
results_data = []

# Now we have to loop through every record
for record in records:
    label = record["label"]
    val = record["value"]
    lim = record["limit"]
    
    diff, pct, status = check_record(val, lim)
    print_report(label, diff, pct, status)
    
    
    if status == "OVER LIMIT":
        over_limit_count += 1
        
    results_data.append(f"{label},{status}")

print(f"Total servers checked: {len(records)}")
print(f"Servers over limit: {over_limit_count}")


# Write out the concise label,status results to 'results.txt' as requested
with open("results.txt", "w") as f:
    for res_line in results_data:
        f.write(res_line + "\n")

