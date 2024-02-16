'''
PROGRAMMER: Carson L. King
USERNAME: cking20
PROGRAM: finance_modified.py

DESCRIPTION: Mortgage Functions
'''
#left this as given
def mortgage_report(amount, rate, years):
    
    report = ""
    for s in mortgage_amortization(amount, rate, years,accelerated):
        report += s
    return report

def mortgage_amortization(amount,rate,term,accelerated):
 # Convert rate to monthly interest rate and term to months
    monthly_rate = rate / 100 / 12
    term_months = term * 12

    # Calculate monthly payment using formula for monthly mortgage payment
    monthly_payment, final_payment = mortgage_payment(amount, rate, term)

    # Initialize variables for amortization table
    table_remaining_balance = amount
    table_interest_paid_total = 0
    table = []

    # Generate amortization table
    for month in range(1, term_months + 1):
        interest_payment = table_remaining_balance * monthly_rate
        principal_payment = monthly_payment - interest_payment + 500;
        
        #If the person wants to accelerate their payment
        if (accelerated == 1):
            principal_payment += 500
        table_interest_paid_total += interest_payment
        table_remaining_balance -= principal_payment

        # Append row to table
        table.append((month, format(interest_payment, '.2f'), format(principal_payment, '.2f'), format(table_remaining_balance, '.2f')))

    # Create title, summary, and header
    title = "Mortgage Amortization Schedule"
    summary = f"Loan amount: ${amount}, Interest rate: {rate}%, Term: {term} years, Monthly payment: ${monthly_payment:.2f}, Final payment: ${final_payment:.2f}, Total paid: ${monthly_payment * term_months:.2f}, Cost of credit: ${monthly_payment * term_months - amount:.2f}"
    header = ("Month", "Interest Payment", "Principal Payment", "Remaining Balance")

    return title, summary, header, table

#Adapted from HW2, gets the miniumum monthly payment
def mortgage_payment(amount, rate, term):
    #gets the term amount in months
    term_months = 12.0 * term;

    #Monthly interest rate
    monthly_interest_rate = (rate /100) / 12;


    #calcs the necessairy minimum monthly payment
    monthly_payment = round((amount * monthly_interest_rate) / (1 - ( 1 + monthly_interest_rate)**-term_months),2);
    
    #Sets up some holder vars
    minimum_remaining_bal = amount;
    total_interest_paid = 0.0;
    

    for term_months in range (1,int(term_months) + 1):
    
        #minimum monthly interest
        minimum_monthly_interest = minimum_remaining_bal * monthly_interest_rate;
    
    
        #calc the amount paid to the principle (minimum loan)
        minimum_principal_payment = monthly_payment - minimum_monthly_interest;
    
        #update remaining balance(minimum loan)
        minimum_remaining_bal -= minimum_principal_payment;
    
        #total interest paid
        total_interest_paid += minimum_monthly_interest;

    #Gets the final totals and rounds them correctly
    final_payment = round(monthly_payment + minimum_remaining_bal,2);
    
    return monthly_payment, final_payment
#Imported from hw2, gets the residual payment
def mortgage_residual(amount,rate,term,payment):
    #calcs the total payment

    #gets the term amount in months
    term_months = 12.0 * term;

    #Monthly interest rate
    monthly_interest_rate = (rate /100) / 12;
    
    #Sets up some holder vars
    minimum_remaining_bal = amount;
    total_interest_paid = 0.0;
    

    for term_months in range (1,int(term_months) + 1):
    
        #minimum monthly interest
        minimum_monthly_interest = minimum_remaining_bal * monthly_interest_rate;
    
    
        #calc the amount paid to the principle (minimum loan)
        minimum_principal_payment = payment - minimum_monthly_interest;
    
        #update remaining balance(minimum loan)
        minimum_remaining_bal -= minimum_principal_payment;
    
        #total interest paid
        total_interest_paid += minimum_monthly_interest;

    #Gets the final totals and rounds them correctly
    final_total = total_interest_paid + amount;
    minimum_rounded_bal = round(minimum_remaining_bal,2);
    
    return minimum_rounded_bal, final_total, total_interest_paid
