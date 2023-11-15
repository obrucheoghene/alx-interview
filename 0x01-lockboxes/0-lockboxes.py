#!/usr/bin/python3
"""
Module to Determine number of locked boxes in front of you
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened
    """
    for key in range(1, len(boxes) - 1):
        ctr = False
        for idx in range(len(boxes)):
            ctr = (key in boxes[idx] and key != idx)
            if ctr:
                break
        if ctr is False:
            return ctr
    return True
