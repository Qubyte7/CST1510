
# your class goes here

class Record:
    over_limit_count = 0
    
    def __init__(self,label,value,limit):
        self.label = label
        self.value = value
        self.limit = limit
        
    def status(self):
        if self.value >= self.limit:
            return "OVER LIMIT"
        elif self.value >= self.limit * 0.9:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    ''' This function opens a file and return List of Record class Objects with label,value and limit attributes'''
    # records will hold all our records
    records = []
    
    with open(path) as f:
        
        # we loop through each line to assign data to label, value and limit 
        for data in f:
            label,value,limit = data.strip().split(",")
            
            # we make a record object for each line of data
            record = Record(label,float(value),float(limit))
            
            # we append the record to our list
            records.append(record)
            
    return records



records = load_records("./records_data.txt")

over_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Value:  {record.value}")
    print(f"  Limit:  {record.limit}")
    print(f"  Status: {record.status()}")
 
    # updating over count variable
    if record.status() == "OVER LIMIT":
        over_count += 1

    print("=" * 34)

print(f"{over_count} of {len(records)} records are OVER LIMIT")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
