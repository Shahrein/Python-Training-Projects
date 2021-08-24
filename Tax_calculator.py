

income = float(input("Enter the annual income: "))
income_threshold = 85528
Tax_relief = 556.02
slab_cross = 14839.02

if income < income_threshold:
    tax = (income * 0.18) - Tax_relief
elif income > income_threshold:
    tax = slab_cross + (income - income_threshold)* 0.32

tax = round(tax, 0)

if tax < Tax_relief:
    print ("The tax is:", 0.0, "thalers")
else:
    print("The tax is:", tax, "thalers")