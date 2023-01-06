import random


def bogo_sort(list):
    """
    Randomise list until find a sorted list
    should have factorial runtime O(n!)
    """
    while verify(list) is not True:
        random.shuffle(list)
    return list


def verify(list):
    if len(list) <= 1:
        return True

    return list[0] < list[1] and verify(list[1:])


print(bogo_sort([4, 7, 3, 9, 5, 8]))
