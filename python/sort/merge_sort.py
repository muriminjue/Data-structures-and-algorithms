def merge_sort(list):
    """
    Divdie, , sort, merge

    Take a llist of items.
    Divide items into sublists until each list has single items
    merge and sort each sublist until return full sorted list
    """

    if len(list) <= 1:
        return list

    left_hand, right_hand = split(list)
    left = merge_sort(left_hand)
    right = merge_sort(right_hand)

    return merge(left, right)


def split(list):
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Take two arrays. Merges and sorts them
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1

        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify(list):
    if len(list) <= 1:
        return True

    return list[0] < list[1] and verify(list[1:])


print(verify([2, 8, 6, 7, 5, 4, 3, 1]))
print(verify(merge_sort([2, 8, 6, 7, 5, 4, 3, 1])))
