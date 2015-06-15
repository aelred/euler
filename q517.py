import math


def g(a, x):
    y_max = math.ceil(x / a - 1) + 1

    mem = [1] * (y_max+1)

    z_start = math.floor(x - a)

    for z in range(z_start, -1, -1):
        y_start = math.floor((x - z) / a - 1)

        for y in range(y_start, -1, -1):
            mem[y] += mem[y+1]

    return mem[0]


def G(n):
    return g(n ** 0.5, n)


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


if __name__ == '__main__':
    all_primes = primes(start=10000000, end=10010000)
    summed = sum([G(p) for p in all_primes])
    print(summed % 1000000007)
