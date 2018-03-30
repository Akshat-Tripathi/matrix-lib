# matrix-lib
A simple module for matrix multiplication

# Installation
Install using git.
``` git clone https://github.com/Akshat-Tripathi/matrix-lib.git```

# Functions
This module allows you to:
* Create matrices
* Add and subtract matrices by each other
* Add and subtract matrices by numbers
* Multiply and divide matrices elementwise
* Multiply and divide matrices by numbers
* Perform dot product calculations on matrices
* Transpose matrices
* Apply functions to matrices
* Create matrices with random values

# Creating matrices
To create a matrix, the matrix class must be initialised by passing a 2d array.
```Python
a = matrix([[1, 2],
            [3, 4],
            [5, 6]])
b = matrix([[7, 8, 9],
            [10, 11, 12]])
c = matrix([[1, 2],
            [3, 4],
            [5, 6]])
```

# Adding, subtracting, multiplying and dividing matrices by each other.
Two matrices may be added if they have the same shape.
```Python
a+c #This works
a+b #This doesn't work
```
Two matrices may be subtracted if they have the same shape.
```Python
a-c #This works
a-b #This doesn't work
```
Two matrices may be multiplied elementwise if they have the same shape.
```Python
a*c #This works
a*b #This doesn't work
```
Two matrices may be divided elementwise if they have the same shape.
```Python
a/c #This works
a/b #This doesn't work
```

# Adding, subtracting, multiplying and dividing matrices by numbers.
A matrix may have all of its values changed by a number in the following way.
```Python
a+5
a-5
a*5
a/5
```

# Performing dot product calcuations.
Two matrices can only have a dot product applied if the number of columns in the first matrix is equal to the number of rows in the second.
```Python
a.dot_product(b) #This does work
a.dot_product(c) #This doesn't work
```

# Transposing matrices.
A matrix is transposed when its rows and columns swap.
```Python
a.Transpose() 
#This returns matrix([[1, 2, 3],
                      [4, 5, 6]])
```

# Applying functions to matrices.
This applies a function to every element of a matrix.
```Python
a.apply_function(lamda x: x**2) #This squares every element in a
```

# Other stuff
A matrix's data can be seen by using `.matrix`.
A matrix's shape is shown with `.shape`
```Python
a.matrix #This returns [[1, 2],
                        [3, 4],
                        [5, 6]]
a.shape # This returns [3, 2]
```
           
