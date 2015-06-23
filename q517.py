import math

from util import primes


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


if __name__ == '__main__':
    all_primes = primes(start=10000000, end=10010000)
    summed = sum([G(p) for p in all_primes])
    print(summed % 1000000007)
