#!/usr/bin/python3
'''
A module to compute change
'''


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    :param coins: list of coin values
    :param total: target amount
    :return: fewest number of coins needed or -1 if total cannot be met
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for efficiency
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            num_coins += total // coin
            total %= coin

    return num_coins if total == 0 else -1
