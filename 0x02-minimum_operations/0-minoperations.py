#!/usr/bin/python3
'''
Task 0. Minimum Operations
'''


def minOperations(n):
    '''
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file
    '''
    if not isinstance(n, int):
        return 0
    count = 0
    copy = 0
    done = 1
    while done < n:
        if copy == 0:
            copy = done
            done += copy
            count += 2
        elif n - done > 0 and (n - done) % done == 0:
            copy = done
            done += copy
            count += 2
        elif copy > 0:
            done += copy
            count += 1
    return count
