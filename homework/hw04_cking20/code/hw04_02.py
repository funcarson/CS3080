'''
PROGRAMMER: Carson L. King
USERNAME: cking20
PROGRAM: hw04_03.py

DESCRIPTION: Driver program for prime numbers
'''
from discrete_math import prime_factor
from discrete_math import pretty_int

import time

for n in [0, 1, 2, 3, 12, 97]:
    start_time = time.time()
    result = prime_factor(n)
    end_time = time.time()
    print("    %s = (%s)*(%s) ( %.3f seconds)" \
        % (pretty_int(n), pretty_int(result[0]),
        pretty_int(result[1]), end_time - start_time))
for n in [69_151*83_621, 1264447*3715967, 12957929*19528517, 320019647*57000000011, 61256847931289*612671]:
    start_time = time.time()
    result = prime_factor(n)
    end_time = time.time()
    print("    %s = (%s)*(%s) ( %.3f seconds)" \
            % (pretty_int(n), pretty_int(result[0]),
            pretty_int(result[1]), end_time - start_time))