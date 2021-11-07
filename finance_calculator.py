import math

# Request input from user select between investment or bond.
fin_plan = input("Choose either ' investment 'or ' bond ' from the menu below to proceed:\n"
    "investment     - to calculate the amount of interest you'll earn on interest\n"
    "bond           - to calculate the amount you'll have to pay on a home loan\n"   )

# Lowercase users inout to avoid senesitive inputs.
fin_plan = fin_plan.lower()
# If users input is investment run following prompts.
if fin_plan == "investment":
    deposit = float(input(" Please enter the amount of money your depositing:        \t"))
    interest_rate = float(input(" Please enter the interest rate e.g  8 of 8 %:       \t"))
    num_years = int(input(" Please enter the number of years you plan on investing:   \t"))
# Request user to select between simple or compound interate options.
    interest = input(" Would you like this to be 'simple' or 'compound' interest?:     \t")

# If interest outputs simple run simple interest calculation.
    if interest == "simple":
# calculation is a = p(1+r)*t.
        total_amount = deposit*(1+(interest_rate/100)*num_years)
# Round of value.
        total_amount = round(total_amount,2)
        print(f"The investment simple interest will be: R{total_amount}")
# if inter output is compound run compound interest calculation.
    elif interest == "compound":
# calculation is a = p*(1+r)**t.
        total_amount = deposit*math.pow((1+(interest_rate/100)),num_years)
# Round of value.
        total_amount = round(total_amount,2)
        print(f"The investment compounded interest will be: R {total_amount}")

# Else if user selects bond run following prompts.
elif fin_plan == "bond":
    present_value = float(input("Enter present value of the house:                   \t"))
    interest_rate = float(input("Enter monthly interest rate e.g 8 of 8%:            \t"))
    number_of_months = int(input("Enter the number of months over your bond:         \t"))
# Repayment of bond calculation.
    repayment = ((interest_rate/100) * present_value)/(1-(1+(interest_rate/100))**(-number_of_months))
# Round of.
    repayment = round(repayment,2)
# Output amount payable monthly.
    print(f"The repayable monthly amount will be:                                    \tR {repayment}  ")


# Nhlakanipho Hlophe @nhlakaniphohlophe@gmail.com


  
