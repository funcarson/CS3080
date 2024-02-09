'''
PROGRAMMER: Carson L. King
USERNAME: cking20
PROGRAM: HW01_01
DESCRIPTION: asks user to enter a loan amount (in dollars), an APR (in percent), and a term (in years). Run a payment simulation over the term of the loan, tracking the
remaining balance as on-time payments are made and interest is collected. 
'''

def mortgage_payment(term, APR, loan_amount):
    #gets the term amount in months
    term_months = 12.0 * term;

    #Monthly interest rate
    monthly_interest_rate = (APR /100) / 12;


    #calcs the necessairy minimum monthly payment
    monthly_payment = round((loan_amount * monthly_interest_rate) / (1 - ( 1 + monthly_interest_rate)**-term_months),2);
    
    return monthly_payment


def mortgage_residual(term,APR,loan_amount):
    #calcs the total payment

    #gets the term amount in months
    term_months = 12.0 * term;

    #Monthly interest rate
    monthly_interest_rate = (APR /100) / 12;
    
    #Sets up some holder vars
    remaining_bal = loan_amount;
    minimum_remaining_bal = loan_amount;
    total_interest_paid = 0.0;
    
    #gets the monthly payment
    monthly_payment = mortgage_payment(term,APR,loan_amount);

    for month in range (1,int(term_months) + 1):
    
        #minimum monthly interest
        minimum_monthly_interest = minimum_remaining_bal * monthly_interest_rate;
    
    
        #calc the amount paid to the principle (minimum loan)
        minimum_principal_payment = monthly_payment - minimum_monthly_interest;
    
        #update remaining balance(minimum loan)
        minimum_remaining_bal -= minimum_principal_payment;
    
        #total interest paid
        total_interest_paid += minimum_monthly_interest;

    #Gets the final totals and rounds them correctly
    final_total = total_interest_paid + loan_amount;
    minimum_rounded_bal = round(minimum_remaining_bal,2);
    minimum_final_payment = round(monthly_payment + minimum_remaining_bal,2);
    
    return monthly_payment,minimum_final_payment, final_total, total_interest_paid

def main():
    #Variable lists
    str_loan_amount = "";
    str_APR = "";
    str_term = "";
    valid = False;

    #Creats a loop to make sure information added is correct
    while not valid:
    
        #Asks the user to enter their loan amount
        print("DATA ENTRY");
        str_loan_amount = input("Enter loan amount ($): ....... ");
        str_APR = input("Enter loan APR (%): .......... ");
        str_term = input("Enter loan term (yr): ........ ");
        print("");

    #converts inputs into floating points, if not displays an error and repeats the loop
        try:
            loan_amount = float(str_loan_amount);
            APR = float(str_APR);
            term = float(str_term);
            valid = True;
        except ValueError:
            print("Entered amount is not a number");
            valid = False;
    #End of while loop
    mortgage_all = mortgage_residual(term, APR, loan_amount);
    #Prints the totals with the calculated minimum payment
    print("MORTGAGE TERMS")
    print("Loan amount: ................... " + str(APR) + " %");
    print("Loan rate: ................... " + str(term) + " years");
    print("Loan term: ................. $ " + str(loan_amount));
    print("Monthly payment: ............. $ " + str(mortgage_all[0]));
    print("Final Payment: ............... $ " + str(mortgage_all[1]));
    print("Total paid ................. $ " + str(round(mortgage_all[2],2)));
    print("Cost of Credit ................. $ " + str(round(mortgage_all[3],2)));
if __name__ == "__main__":
    main()