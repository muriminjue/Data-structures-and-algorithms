class Node:
    """
    Object for storing a single node of  a linked list
    models 2 attibutes datat and link to next node
    """

    data = None
    nextNode = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Node data: %s" % self.data


class LinkedList:
    """
    singly linked list
    """
    # head = None

    def __init__(self):
        self.head = None

    def isEmptty(self):
        return self.head == None

    def size(self):
        """
        Counts through all the nodes
        takes O(n)
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.nextNode

        return count

    def add(self, data):
        """
        Prepends datat to linked list
        takes constant time O(1)
        """
        new_node = Node(data)
        new_node.nextNode = self.head
        self.head = new_node

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return "Node data: %s" % current.data
            else:
                current = current.nextNode
        return None

    def insert(self, data, index):
        if index == 0:
            self.add(data)

        elif index > 0:
            position = index
            current = self.head

            while position > 1:
                position -= 1
                current = current.nextNode

            new_node = Node(data)
            new_node.nextNode = current.nextNode
            current.nextNode = new_node

    def remove(self, index):
        current = self.head
        if index == 0:
            self.head = current.nextNode
        else:
            position = 0

            while position < index:
                position += 1
                current = current.nextNode

            next_node = current.nextNode
            current.nextNode = next_node.nextNode

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            position = 0
            current = self.head

            while position < index:
                position += 1
                current = current.nextNode

            return current

    def __repr__(self):
        """
        Prints the ndoes in the linked list
        Takes (linear O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current == self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.nextNode is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.nextNode

        return "->".join(nodes)
