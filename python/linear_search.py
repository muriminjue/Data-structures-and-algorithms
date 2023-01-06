def linear_search(List, target):
    """
    Loop through array list and return target index if found and none if not found
    """
    for i in range(0, len(List)):
        if List[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Item was found at index: ", index)
    else:
        print("item was not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)
