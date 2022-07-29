import pyperclip as pc  # To copy and paste the final matrix when it has been processed

import functions as fns
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Get the overall rotation matrix given the transformation the user wants
rotation_matrix = fns.overall_rotation_matrix()
print(rotation_matrix)

# Get the user to input the structure of the tensor
user_tensor = fns.enter_tensor()
print(user_tensor)

print(fns.calculate_rotated_tensor(user_tensor, rotation_matrix))


















# TODO 1: Graph the components of A tensors on a graph, with labels and a key


# TODO 2: Graph both graphs as a subplot
# x = np.arange(-4 * np.pi, 4 * np.pi, 0.1)
# y = l[0][0][0]
# plt.plot(x, y)
# plt.show()

# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html#sphx-glr-gallery-subplots-axes-and-figures-subplot-py
# TODO 2: Graph the components of BOTH tensors on two seperate graphs, with labels and a key
