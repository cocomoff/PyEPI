def generate_primes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes


if __name__ == '__main__':
    print(generate_primes(100))
    print(generate_primes(1000))
