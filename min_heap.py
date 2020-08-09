# Course: CS261 - Data Structures
# Assignment: 5
# Student:
# Description:


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    @staticmethod
    def left(i):
        """
        TODO: Write this implementation
        """
        return int(2 * i + 1)

    @staticmethod
    def right(i):
        """
        TODO: Write this implementation
        """
        return int(2 * (i + 1))

    @staticmethod
    def parent(i):
        """
        TODO: Write this implementation
        """
        return int((i - 1) / 2)

    def add(self, node: object) -> None:
        """
        TODO: Write this implementation
        """
        if self.heap.length() == 0:
            self.heap.append(node)
        else:
            index = self.heap.length()
            self.heap.append(node)
            self.bubble_up(index)

        return

    def bubble_up(self, i):
        """
        TODO: Write this implementation
        """
        p = self.parent(i)
        while i > 0 and self.heap.get_at_index(i) < self.heap.get_at_index(p):
            self.heap.swap(i, p)
            i = p
            p = self.parent(i)

    def get_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.heap.length() == 0:
            raise MinHeapException
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.heap.length() == 0:
            raise MinHeapException
        else:
            self.heap.swap(0, self.heap.length() - 1)
            x = self.heap.pop()
            self.trickle_down(0)
            return x

    def trickle_down(self, i):
        """
        TODO: Write this implementation
        """
        while i >= 0:
            j = -1
            r = self.right(i)
            if r < self.heap.length() and self.heap.get_at_index(r) < self.heap.get_at_index(i):
                l = self.left(i)
                if self.heap.get_at_index(l) < self.heap.get_at_index(r):
                    j = l
                else:
                    j = r
            else:
                l = self.left(i)
                if l < self.heap.length() and self.heap.get_at_index(l) < self.heap.get_at_index(i):
                    j = l
            if j >= 0:
                self.heap.swap(j, i)
            i = j

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        old = DynamicArray()
        old = self.heap
        


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
