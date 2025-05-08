import os
import sys
cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cur_dir+"/../../")
from Utils.KeyObject import KeyObject

class LinkedListNode:
    def __init__(self, data):
        """Initialize a node of a circular doubly linked list with a sentinel with the given data """
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)

class DoublyLinkedListSentinel:
    def __init__(self, get_key_func=None):  
        """Initialize a circular doubly linked list with a sentinel.

        Arguments:
        get_key_func -- an optional function that returns the key for 
        the objects stored. May be a static function in the object class.
        if omitted, then a identity function is used.
        """
        self.sentinel = LinkedListNode(None)  # hold None as data
        # the sentinel points to itself in an empty list
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
        self.get_key_func = get_key_func if get_key_func else lambda x:x

    def search(self, k):
        """
        Search a circular doubly linked list with a sentinel for a node with key k.

        Returns:
        node with key k or None if not found
        """
        for node in self.iterator():
            if self.get_key_func(node.data) == k:
                return node
        return None

    def insert(self, item, y:LinkedListNode):
        """
        Insert a node after node y.

        Arguments:
        item -- node or data
        """
        x = item
        if not isinstance(item, LinkedListNode):
            x = LinkedListNode(item)
        x.prev = y
        x.next = y.next
        y.next.prev = x
        y.next = x
        return x

    def prepend(self, item):
        """
        Insert a node as the head of a circular doubly linked list with a sentinel.
        """
        x = item
        if not isinstance(item, LinkedListNode):
            x = LinkedListNode(item)
        return self.insert(x, self.sentinel)
    
    def append(self, item):
        """
        Append a node to the tail of a circular doubly linked list with a sentinel.
        """
        x = item
        if not isinstance(item, LinkedListNode):
            x = LinkedListNode(item)
        return self.insert(x, self.sentinel.prev)

    def delete(self, x: LinkedListNode):
        """
        Remove a node x from a circular doubly linked list with a sentinel.
        """
        if x is self.sentinel:
            raise RuntimeError("Cannot delete sentinel.")
        x.prev.next = x.next 
        x.next.prev = x.prev

    def delete_all(self):
        """
        Delete all nodes in a circular doubly linked list with a sentinel.
        """
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
    
    def iterator(self):
        """
        Iterator from the head of a circular doubly linked list with a sentinel.
        """
        x = self.sentinel.next
        while x is not self.sentinel:
            yield x
            x = x.next

    def copy(self):
        """
        Return a copy of this circular doubly linked list with a sentinel.
        """
        c = DoublyLinkedListSentinel(self.get_key_func)  
        for node in self.iterator():
            c.append(node.data)
        return c

    def __str__(self):
        string = ""
        for index, node in enumerate(self.iterator()):
            if index != 0:
                string += " \u27F7 "
            
            string += "[" + str(node.data) + "]"

        if self.sentinel.next == self.sentinel:
            string += "[]"
        return string

# Testing
if __name__ == "__main__":

	# Insert. 
	linked_list1 = DoublyLinkedListSentinel()
	for i in range(10):
		linked_list1.prepend(i)
	print(linked_list1)

	# Search. 
	print(linked_list1.search(5))

	# Copy.
	linked_list2 = linked_list1.copy()
	linked_list2.append(99)
	print(linked_list1)
	print(linked_list2)
	
	# Delete. 
	linked_list2 = DoublyLinkedListSentinel()
	linked_list2.prepend(5)
	linked_list2.prepend(6)
	linked_list2.prepend(7)
	print(linked_list2)
	x = linked_list2.search(6)  # should be 6
	print(x)
	linked_list2.delete(x)
	print(linked_list2.search(6))  # unsuccessful search
	print(linked_list2)

	# Delete sentinel error. 
	try:
		linked_list2.delete(linked_list2.sentinel)
	except RuntimeError as e:
		print(e)

	# Object.
	linked_list3 = DoublyLinkedListSentinel(KeyObject.get_key)
	list1 = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "HI", "NH", "NY"]
	for i in range(len(list1)):
		linked_list3.append(KeyObject(list1[i], i))
	print(linked_list3)
	node5 = linked_list3.search(5)  # CO has key 5
	print(node5)
	linked_list3.insert(KeyObject("VT", 17), node5)  # insert VT after CO
	linked_list3.delete(node5)                       # delete CO
	print(linked_list3)
