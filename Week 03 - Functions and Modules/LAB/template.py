"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    
    """ This function outputs "Overlimit" when percentage is over or equal to 100, "Warning" if equal or over 90 else "OK" """
    if percent >=100 :
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
def check(value,limit):
    """This function returns the difference between the value and limit and the percentage of the value to the limit"""
    difference = value - limit
    percentage  = (value/limit) * 100
    
    return difference,percentage

def print_report(label,value,limit,difference,percent,status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Used    :{value:>10.2f}")
    print(f"Total   :{limit:>10.2f}")
    print(f"Free    :{difference:>10.2f}")
    print(f"Percent :{percent:>10.2f}")
    print(f"status  :{status:>10}")

    print("=" * 34)

label = ""

over_limit_counter = 0

while label != "quit":
    label = input("Enter the labels: ")      
    if label == "quit":
        break
    value = float(input("Enter the value: "))     
    limit = float(input("Emter the limit: "))   

    difference = check(value,limit)[0]  
    percent = check(value,limit)[1]      
    status = status_of(percent)
    

    print_report(label,value,limit,difference,percent,status)
    
    if status == "OVER LIMIT":
        over_limit_counter +=1

print("OVER LIMIT encounted :",over_limit_counter)