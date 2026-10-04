

label = ""
value = 0.0
limit = 0.0
over_limit_count = 0

while label != "quit":
    label = input("Enter your label : ")    
    if label == "quit":
        break;
    else:
        value = float(input("Enter the value : "))   
        limit = float(input("Enter the limit :"))     

        # Calculation

        difference = value - limit   
        percent = (value/limit) * 100

        # Checking the value over limit

        status = ""   
        if value > limit:
            status = "OVER LIMIT"
            over_limit_count+=1
        else:
            status = "OK"

        print("\n")
        print("=" * 34)
        print(f"  RECORD CHECK  -  {label}")
        print("=" * 34)

        print(f"value : {value:>8.2f}")
        print(f"limit : {limit:>8.2f}")
        print(f"status: {status:>8}")

        print("=" * 34)
    
    
print(f"The over limit count is {over_limit_count}")

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
