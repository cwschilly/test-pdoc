import numpy as np

def make_and_print_array():
  '''Generates and prints out an array'''
  array = np.arange(1, 26).reshape(5, 5)

  for row in array:
      print(row)

make_and_print_array()