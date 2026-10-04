
label = input("Enter your label: ")      
first = float(input("Enter the first number: "))    
second = float(input("Enter the second number: "))   


# calculation
difference = first - second   # 
percent = (first*100)/second     # 


# =================================================================== OUTPUT
# 3. Print the report.


print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"first value   : {first:>+10.2f}")
print(f"second value  : {second:>+10.2f}")
print(f"percentage    : {percent:>10.2f} %")
print(f"difference    : {difference:>+10.2f}")

print("=" * 34)

