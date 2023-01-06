def quick_sort(list):
    """
    Get first item in the list
    devid list int two. Values less than first itema nad freat than that
    run this recursively over each list and add them to pivot on both sides

    runtime of O(n log n)
    """
    if len(list) <= 1:
        return list

    lesser_values = []
    greater_values = []
    pivot = list[0]

    for item in list[1:]:
        if item > pivot:
            greater_values.append(item)
        else:
            lesser_values.append(item)

    return quick_sort(lesser_values) + [pivot] + quick_sort(greater_values)


print(quick_sort([4, 7, 3, 9, 5, 8]))
