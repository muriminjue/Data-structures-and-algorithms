from Linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sort a linked list
    - recusrively split linked list to single nod lists
    - merge node into new dorted linked list
    """

    if linked_list.size() == 1 or linked_list.size is None:
        return linked_list

    left_hand, right_hand = split(linked_list)
    left = merge_sort(left_hand)
    right = merge_sort(right_hand)

    return merge(left, right)


def split(linked_list):
    """
    Devid unsorted linked list into sublists
    """

    if linked_list == None or linked_list.head == None:
        right_half = None
        left_half = linked_list
        return left_half, right_half
    else:
        mid = linked_list.size() // 2
        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.nextNode
        mid_node.nextNode = None
        return left_half, right_half


def merge(left, right):
    """
    Merges two linked lists, sorting by datain nodes
    returns a new merge list
    """

    # new empty linked list
    merged = LinkedList()

    # add one items as fake head
    merged.add(0)

    current = merged.head

    # obtain heads for right and letf sublists
    left_head = left.head
    right_head = right.head

    # iterate over linked list until tail of either
    while left_head or right_head:
        # if the left head is none we are past the tails therefore add the right head
        if left_head is None:
            current.nextNode = right_head
            # Thi next line will stop loop if right head was also a tail node
            right_head = right_head.nextNode

        # if the right head is none we are past the tails therefore add the left head
        elif right_head is None:
            current.nextNode = left_head
            # Thi next line will stop loop if leaf head was also a tail node
            left_head = left_head.nextNode

        else:
            # not at aiether tail node copair nodes
            if left_head.data < right_head.data:
                current.nextNode = left_head
                left_head = left_head.nextNode
            else:
                current.nextNode = right_head
                right_head = right_head.nextNode

        current = current.nextNode

    # discard fake node
    merged.head = merged.head.nextNode

    return merged


l = LinkedList()
l.add(1)
l.add(5)
l.add(3)
l.add(7)
l.add(2)
l.add(4)


def verify(linked_list):
    if linked_list is None or linked_list.head.nextNode is None or linked_list.head is None:
        return True
    return linked_list.head.data < linked_list.head.nextNode.data and verify(linked_list.remove(0))


print(verify(l))
print(verify(merge_sort(l)))
