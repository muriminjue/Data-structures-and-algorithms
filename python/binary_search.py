def binary_search(List, target):
    first = 0
    last = len(List)-1

    while first <= last:
        midpoint = (first + last) // 2

        if List[midpoint] == target:
            return midpoint
        elif List[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return None


def verify(index):
    if index is not None:
        print("Item was found at index: ", index)
    else:
        print("item was not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)
