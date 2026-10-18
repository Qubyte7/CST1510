""" In this programm we explore the use if decisions and loop to make reports """

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

