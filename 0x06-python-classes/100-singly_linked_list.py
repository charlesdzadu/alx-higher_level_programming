#!/usr/bin/python3
""" Define class singly linked list """


class Node:
    """ A node of a singly linked list """

    def __init__(self, data, next=None):
        """ Initialize the node

        Args:
            data (int): The data of the node
            next (Node): The next node of the node
        """
        self.data = data
        self.next = next

    @property
    def data(self):
        """ Get/set the data of the node """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next(self):
        """ Get/set the next node of the node """
        return self.__next

    @next.setter
    def next(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next must be a Node object")
        self.__next = value



class SinglyLinkedList:
    """ A singly linked list """

    def __init__(self):
        """ Initialize the singly linked list """
        self.__head = None

    def __str__(self):
        """ Print the singly linked list """
        string = ""
        node = self.__head
        while node:
            string += str(node.data)
            node = node.next
            if node:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """ Insert a node in the singly linked list

        Args:
            value (int): The value of the node to insert
        """

        new = Node(value)
        if not self.__head:
            self.__head = new
            return
        if value < self.__head.data:
            new.next = self.__head
            self.__head = new
            return
        node = self.__head
        while node.next and value > node.next.data:
            node = node.next
        new.next = node.next
        node.next = new

