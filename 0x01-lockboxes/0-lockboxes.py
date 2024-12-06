#!/usr/bin/python3
"""
A module to detrmine if boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of list of int): List where each index represents a box
    and contains a list of keys available in that box.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    n = len(boxes)
    unlocked = [False] * n  # Keep track of unlocked boxes
    unlocked[0] = True      # The first box is unlocked
    keys = set(boxes[0])    # Collect all keys from the first box

    while True:
        new_key_found = False
        for i in range(n):
            if not unlocked[i] and i in keys:
                unlocked[i] = True
                keys.update(boxes[i])
                new_key_found = True
        if not new_key_found:
            break

    return all(unlocked)
