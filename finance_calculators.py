import math 

# ask the user to select 1 of 2 options - investment or bond
# make sure the user's input is not case sensitive
# display recommendation based on selection

while True:
    print("investment - to calculate the amount of interest you'll earn on your investment")

    print("bond - to calculate the amount you'll have to pay on a home loan")

    selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: " )

    print(selection)

    selection = selection.lower()

# when investment is selected, ask user for
# amount of money being deposited
# the interest rate
# number of years planning on investing

    if (selection == "investment"):
        deposit_p = float(input("State how much you are depositing: "))
        interest_r = float(input("State what your interest rate is: "))
        years_t = float(input("State how many years you plan to invest: "))

# ask user to choose compound or simple interest

        interest = input("Choose compound or simple interest: ")
    
# if simple is chosen, divide interest rate by 100 first
# then calculate with A = P (1 + r x t)

        if (interest == "simple"):
            total_interest = (((interest_r / 100) * years_t) + 1) * deposit_p
            print(total_interest)

            break

# if compound is selected, calculate A = P *nmath.pow(1+r),t)

        elif (interest == "compound"):
            total_interest = deposit_p * math.pow((1 + (interest_r / 100)), years_t)
            print(total_interest)

            break

# if bond is chosen, ask for
# present value of house
# interest rate
# number of months to repay the bond

    elif (selection == "bond"):
            house_value = float(input("State the present value of your house: "))
            interest_r = float(input("State your interest rate: "))
            months = float(input("State number of months you plan to replay the bond: "))

# divide interst rate by 100 first, then by 12 to get monthly interest rate

            interest_monthly = ((interest_r / 100) / 12)

# calculate monthly repayment with repayment = (i * P) / (1 + i) **(-n)

            monthly_repayment = (interest_monthly * house_value) / (1 - (1 + interest_monthly) ** -months)
            print(monthly_repayment)
            
            break


                











