#!/usr/bin/python3
"""this is singly linked list in python"""


class Node:
    """writing linked list"""

    def __init__(self, data, next_node=None):
        if not isinstance(next_node, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__next_node = next_node
            self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """singly linked list"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
