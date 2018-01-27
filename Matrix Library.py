# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 12:36:10 2018

@author: akshat
"""

class matrix:
    def __init__(self, array):
        """By passing an n x m array, a n x m matrix object is created"""
        """The .matrix property refers to the data as an array, while .rows and
        .columns are the number of rows and columns of the matrix object"""
        self.rows = len(array)
        self.columns = len(array[0])
        self.matrix = array
    
    def scalar_multiply(self, n):
        """Multiply the matrix by a scalar e.g. 2"""
        for y in range(self.rows):
            for x in range(self.columns):
                self.matrix[y][x] *= n
    
    def scalar_add(self, n):
        """Add a scalar to the matrix"""
        for y in range(self.rows):
            for x in range(self.columns):
                self.matrix[y][x] += n
                
    def elementwise_add(self, mat):
        """Add the contents of one matrix to this one element by element"""
        if len(self.matrix) != len(mat) or len(self.matrix[0]) != len(mat[0]):
            raise ArithmeticError("The shapes of the matrices do not align lol")
        for y in range(self.rows):
            for x in range(self.columns):
                self.matrix[y][x] += mat[y][x]
    
    def elementwise_multiply(self, mat):
        """Multiply the contents of one matrix with this one element by element"""
        if len(self.matrix) != len(mat) or len(self.matrix[0]) != len(mat[0]):
            raise ArithmeticError("The shapes of the matrices do not align lol")
        for y in range(self.rows):
            for x in range(self.columns):
                self.matrix[y][x] *= mat[y][x]
    
    def apply_function(self, function):
        """Apply a function to this matrix element by element"""
        for y in range(self.rows):
            for x in range(self.columns):
                self.matrix[y][x] = function(self.matrix[y][x])
    
    def dot_product(self, mat):
        """Takes the dot product of two matrices"""
        if self.columns != mat.rows:
            raise ArithmeticError("The shapes of the matrices do not align lol")
        result = []
        for y in range(self.rows):
            result.append([])
            for x in range(mat.columns):
                su = 0
                for i in range(self.columns):
                    su += self.matrix[y][i]*mat.matrix[i][x]
                result[y].append(su)
                del su
        self.matrix = result
    
    def T(self):
        """Swaps the rows and columns of the matrix"""
        result = []
        for y in range(self.columns):
            result.append([])
            for x in range(self.rows):
                result[y].append(self.matrix[x][y])
        self.matrix = result