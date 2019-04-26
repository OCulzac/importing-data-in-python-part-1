""" Loading .mat files
In this exercise, you'll figure out how to load a MATLAB file using scipy.io.loadmat() and you'll discover what Python datatype it yields.

The file 'albeck_gene_expression.mat' is in your working directory. This file contains (gene expression data)[https://www.mcb.ucdavis.edu/faculty-labs/albeck/workshop.htm] from the Albeck Lab at UC Davis. You can find the data and some great documentation (here)[https://www.mcb.ucdavis.edu/faculty-labs/albeck/workshop.htm]. """

# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))
