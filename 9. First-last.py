from typing import Sequence


def first_last(sequence):
    return sequence[0:1]+sequence[-1:]

print(first_last('abdf'))
print('abdf'[-1])
print('abdf'[0])
print(first_last((1,2,3,4)))