#!/usr/bin/python3
'''
A module that determines a winner of x rounds of a prime game
'''


def isWinner(x, nums):
    '''
    Determines a winner of x rounds
    x : number of rounds
    nums : Array of "n" values for each round
    '''

    if not nums or x <= 0:
        return None

    # Maximum value of n to calculate the primes
    max_n = max(nums)

    # Determine prime numbers up to maximum using Sieve of Eratosthenes
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False # 0 and 1 are not prime numbers
    for k in range(2, int(max_n ** 0.5) + 1):
        if primes[k]:
            for multiple in range(k * k, max_n + 1, k):
                primes[multiple] = False

    # calculate the number of primes to each number
    prime_counts = [0] * (max_n + 1)
    for k in range (1, max_n + 1):
        prime_counts[k] = prime_counts[k - 1] + ( 1 if primes[k] else 0)

    # Initialize count wins for maria and Ben
    maria_win = 0
    ben_win = 0

    for n in nums:
        # maria starts
        if prime_counts[n] % 2 == 1:
            maria_win += 1
        else:
            ben_win += 1

    # Overall winner
    if maria_win > ben_win:
        return 'Maria'
    elif ben_win > maria_win:
        return 'Ben'
    else:
        return None
