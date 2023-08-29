#!/usr/bin/python3

class Square:
	"""Square class with a private attribute - size"""
	def __init__(self, size=0):
		"""Initialize Square with size attribute"""
		if type(size) is not int:
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size

	def area(self):
		"""Return area of square"""
		return self.__size ** 2

	@property
	def size(self):
		"""Getter method for size"""
		return self.__size

	@size.setter
	def size(self, value):
		"""Setter method for size"""
		if type(value) is not int:
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = value
