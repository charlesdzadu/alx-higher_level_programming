#!/usr/bin/python3

class Square:
	"""Square class with a private attribute - size"""
	def __init__(self, size=0):
		"""Initialize Square with size attribute"""
		self.__size = size

	@property
	def size(self):
		"""Getter for size attribute"""
		return self.__size

	@size.setter
	def size(self, value):
		"""Setter for size attribute"""
		if type(value) is not int:
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = value

	def area(self):
		"""Return area of square"""
		return self.__size ** 2

	def my_print(self):
		"""Print square with #"""
		if self.__size == 0:
			print()
		else:
			for i in range(self.__size):
				for j in range(self.__size):
					print("#", end="")
				print()
