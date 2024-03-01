import time
import threading


results = {}
lock = threading.Lock()

def pretty_int(n):
    return "{:,.0f}".format(n)

def prime_factor(n):
    if not isinstance(n, int) or n < 2:
        return (1, n)

    for p in range(2, n):
        if n % p == 0:
            return (p, n // p)

    return (n, 1)

def factor_thread(number):
    global results
    start_time = time.time()

    #uses the previous prime factor 
    factors = prime_factor(number)
    
    #tracks time per factor
    end_time = time.time()
    elapsed_time = end_time - start_time

    with lock:
        results[number] = (factors, elapsed_time)

def factor_list(numbers, time_limit):
    global results
    threads = []
    count = 0

    print(f"Factoring a list of RSA numbers\nList length: {len(numbers)} numbers\nTime limit: {time_limit} seconds")
    print("-" * 50)

    #Begins the process while starting the timer
    for number in numbers:
        t = threading.Thread(target=factor_thread, args=(number,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    #Checks if it took more time than required
    print("Results:")
    for number, (factors, elapsed_time) in results.items():
        if elapsed_time > time_limit:
            print(f"TIME EXPIRED for {number}")
            count += 1
        else:
            print(f"{pretty_int(number)} = {'*'.join(map(pretty_int, factors))} --- ( {elapsed_time:.3f} sec )")

    print(f"Successfully factored {len(numbers) - count} numbers.")
    print(f"Terminating {count} child threads.")
    print("Clean up complete, exiting program.")

if __name__ == "__main__":
    
    print("discrete_math.py : pretty_int() test")
    print()
    try:
        pretty_int(1)
    except NameError:
        print("    Function pretty_int() not implemented")
        print()
    else:
        n_list = [0, 1, 999, 1000, 2**16, 2**64]
        for n in n_list:
            print("  ", n, "=", pretty_int(n))
    print()
    
    print("discrete_math.py : prime_factor() test")
    print()
    try:
        prime_factor(1)
    except NameError:
        print("    Function prime_factor() not implemented")
        print()
    else:
    
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

    print("discrete_math.py : factor_list() test")
    print()
    try:
        factor_list
    except NameError:
        print("   Function factor_list() not implemented")
        print()
    else:
    
        rsa_p1 = [6186493,42598097,6186503,6186527,42598099,42597899,6186611,42597917,6186619,42597871]
        rsa_p2 = [42597871,42597889,42597899,42597911,42597917,42597923,6186527,42597979,42598097,42598099]
        rsa_list = []
        for p1, p2 in zip(rsa_p1, rsa_p2):
            rsa_list.append(p1 * p2)
        factor_list(rsa_list, 8)
        print("Done")

    