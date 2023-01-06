def recursive_binary_search(List, target):
    if len(List) == 0:
        return False

    else:
        midpoint = len(List)//2
        if List[midpoint] == target:
            return True
        else:
            if List[midpoint] < target:
                recursive_binary_search(List[midpoint+1:], target)
            else:
                recursive_binary_search(List[:midpoint], target)
    return False

def verify(result):
    print("Item found:", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
