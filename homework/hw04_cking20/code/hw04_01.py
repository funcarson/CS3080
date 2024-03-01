'''
PROGRAMMER: =Carson L. King
USERNAME: cking20
PROGRAM: hw04_03.py

DESCRIPTION: Driver program for pretty int
'''

from discrete_math import pretty_int

#Puts the test codes specfied in the pdf
test_1 = pretty_int(0)
test_2 = pretty_int(1)
test_3 = pretty_int(999)
test_4 = pretty_int(1000)
test_5 = pretty_int(2**16)
test_6 = pretty_int(2**64)

#prints the results
print("The results of the test cases")
print(test_1)
print(test_2)
print(test_3)
print(test_4)
print(test_5)
print(test_6)