# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

piece = "note=server=east"

# we need to add variable for the third value
key, value, location = piece.split("=")

print(key, value, location)
