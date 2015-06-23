from util import primes

if __name__ == '__main__':
    size = 2 ** 16

    while True:
        ps = list(primes(size))

        try:
            print(ps[10000])
        except IndexError:
            size *= 2
        else:
            break
