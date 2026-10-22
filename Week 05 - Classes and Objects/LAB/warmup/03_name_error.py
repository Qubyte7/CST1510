# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        return "OVER LIMIT" if self.value > self.limit else "OK"

r = Record("R-001", 120.0, 100.0)

# Status belongs to Record class so we have to call it from an object 
# created from that Record class
print(r.status())
