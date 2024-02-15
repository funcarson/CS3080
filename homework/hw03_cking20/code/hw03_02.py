'''
PROGRAMMER: Carson L. King
USERNAME: cking20
PROGRAM: hw03_02.py


DESCRIPTION: Mortgage Amortization Table w/wo acceleration
'''

import finance_modified

# Get input from user:
print("DATA ENTRY")
amount = float(input("Enter loan amount ($):...... "))
rate         = float(input("Enter loan APR (%):......... "))
term  =   int(input("Enter loan term (yr):....... "))
filename    =   str(input("Filename (w/o ext):......... "))
accelerated = 	int(input("Would you like the payment to be accelerated (1 if yes, 0 if no):........."))
print()

#Generate full and abbreviated Amortization Schedules
#Made some changes to handle a tupple
with open(filename + ".txt", "wt") as fp:
    title, summary, header, table = finance_modified.mortgage_amortization(amount,rate,term,accelerated)
    fp.write(f"{title}\n{summary}\n")
    fp.write("\t".join(header) + "\n")
    for row in table:
        fp.write("\t".join(map(str, row)) + "\n")
    
title, summary, header, table = finance_modified.mortgage_amortization(amount,rate,term,accelerated)
print(f"{title}\n{summary}")
print("\t".join(header))
for row in table:
    print("\t".join(map(str, row)))



