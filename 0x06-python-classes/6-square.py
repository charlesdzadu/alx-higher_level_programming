#!/usr/bin/python3

class Square:
	"""Square class with a private attribute - size"""
	def __init__(self, size=0, position=(0, 0)):
		"""Initialize Square with size attribute"""
		self.size = size
		self.position = position

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

	@property
	def position(self):
		"""Getter for position attribute"""
		return self.__position

	@position.setter
	def position(self, value):
		"""Setter for position attribute"""
		if type(value) is not tuple or len(value) != 2 or \
		type(value[0]) is not int or type(value[1]) is not int or \
		value[0] < 0 or value[1] < 0:
			raise TypeError("position must be a tuple of 2 positive integers")
		else:
			self.__position = value

	def area(self):
		"""Return area of square"""
		return self.__size ** 2

	def my_print(self):
		"""Print square to stdout using #"""
		if self.__size == 0:
			print()
		else:
			for i in range(self.__position[1]):
				print()
			for i in range(self.__size):
				print("{}{}".format(" " * self.__position[0], "#" * self.__size))
