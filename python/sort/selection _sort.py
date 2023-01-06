

def selection_sort(list):
    """
    Removes smalles time from unsorted list and adds it to sorted list
    has quadratic runtime O(n^2)
    """

    sorted_list = []

    while len(list) > 0:
        least_value = list[0]
        for item in list:
            if least_value > item:
                least_value = item
        sorted_list.append(least_value)
        list.remove(least_value)

    return sorted_list


print(selection_sort([4, 7, 3, 9, 5, 8]))
