def primes(end, start=0):
    sieve = [True for n in range(end)]

    enum = enumerate(sieve)
    next(enum)
    next(enum)

    for n, is_prime in enum:
        if is_prime:
            if n > start:
                yield n

            for mult in range(2 * n, end, n):
                sieve[mult] = False
