'''
PROGRAMMER: Carson L. King
USERNAME: cking20
PROGRAM: hw03_01.py

DESCRIPTION: Mortgage Amortization Table
'''

import finance

# Get input from user:
print("DATA ENTRY")
loan_amount = float(input("Enter loan amount ($):...... "))
apr         = float(input("Enter loan APR (%):......... "))
term_years  =   int(input("Enter loan term (yr):....... "))
filename    =   str(input("Filename (w/o ext):......... "))
print()

#Generate full and abbreviated Amortization Schedules
#Made some changes to handle a tupple
with open(filename + ".txt", "wt") as fp:
    title, summary, header, table = finance.mortgage_amortization(loan_amount, apr, term_years)
    fp.write(f"{title}\n{summary}\n")
    fp.write("\t".join(header) + "\n")
    for row in table:
        fp.write("\t".join(map(str, row)) + "\n")
    
title, summary, header, table = finance.mortgage_amortization(loan_amount, apr, term_years)
print(f"{title}\n{summary}")
print("\t".join(header))
for row in table:
    print("\t".join(map(str, row)))


