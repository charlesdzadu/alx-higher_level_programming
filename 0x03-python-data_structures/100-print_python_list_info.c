#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print list info
 * @p: pointer to Python Object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, i;
	PyObject *it;

	list_size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		it = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(it)->tp_name);
	}
}
