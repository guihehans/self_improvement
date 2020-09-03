#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: Bag.py
@time: 2020/9/2 11:11
@function:

"""

from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")
S = TypeVar("S")


class Bag(Generic[T]):
    """
    The Bag class represents a bag (or multiset) of generic items. It
    supports insertion and iterating over the items in arbitrary order.
    This implementation uses a singly linked list with a static nested class Node.
    See LinkedBag for the version from the
    textbook that uses a non-static nested class.
    The add, is_empty, and size operations
    take constant time. Iteration takes time proportional to the number of items.
    """

    class Node(Generic[S]):
        # helper linked list class
        def __init__(self):
            self.next: Optional[Bag.Node[T]] = None
            self.item: Optional[S] = None

    def __init__(self) -> None:
        # beginning of bag
        self._first: Optional[Bag.Node[T]] = None
        # the number of elements in bag
        self._n: int = 0

    def is_empty(self):
        """
        Returns true if the bag is empty

        :return: True if bag is empty;
                 False otherwise.
        """
        return self._first is None

    def size(self) -> int:
        """
        Returns the numer of element in a bag

        :return: the number of items in this bag
        """
        return self._n

    def __len__(self):
        return self.size()

    def add(self, item: T) -> None:
        """
        Adds the item to this bag.

        :param item:the item to add in this bag
        """
        pre_first_node = self._first
        self._first = Bag.Node()
        self._first.item = item
        self._first.next = pre_first_node
        self._n += 1

    def __iter__(self) -> Iterator[T]:
        current = self._first
        while current:
            assert current.item is not None
            yield current.item
            current = current.next

    def __repr__(self) -> str:
        out = "{"
        for elem in self:
            out += "{}".format(elem)

        return out + "}"
