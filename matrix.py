# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:52:06 2018

@author: akshat
"""

class ShapeError(Exception):
    pass
class matrix:
    def __init__(self, array):
        """Creates the matrix object from a 2d array"""
        self.matrix = array
        #Check if matrix is consistent
        if len(set(len(i) for i in array)) != 1:
            raise TypeError("Your matrix is not consistent")
        if type(array[0]) != list:
            raise TypeError("Only a list of lists can be passed to a matrix object")
        self.shape = [len(array), len(array[0])]
        
    def __add__(self, other):
        """Adds the contents of one matrix to this one, or increments the value of every number in the matrix by the other"""
        if type(other) == matrix or type(other) == random_matrix:
            if other.shape == self.shape:
                result = [[] for i in range(self.shape[0])]
                for y in range(self.shape[0]):
                    for x in range(self.shape[1]):
                        temp = self.matrix[y][x] + other.matrix[y][x]
                        result[y].append(temp)
                return matrix(result)
            else:
                raise ShapeError("The shapes do not align")
        elif type(other) == int or type(other) == float:
            result = [[] for i in range(self.shape[0])]
            for y in range(self.shape[0]):
                for x in range(self.shape[1]):
                    result[y].append(self.matrix[y][x] + other)
            return matrix(result)
    
    def __sub__(self, other):
        """Subtracts the contents of one matrix to this one, or decrements the value of every number in the matrix by the other"""
        if type(other) == matrix or type(other) == random_matrix:
            if other.shape == self.shape:
                result = [[] for i in range(self.shape[0])]
                for y in range(self.shape[0]):
                    for x in range(self.shape[1]):
                        result[y].append(self.matrix[y][x] - other.matrix[y][x])
                return matrix(result)
            else:
                raise ShapeError("The shapes do not align")
        elif type(other) == int or type(other) == float:
            result = [[] for i in range(self.shape[0])]
            for y in range(self.shape[0]):
                for x in range(self.shape[1]):
                    result[y].append(self.matrix[y][x] - other)
            return matrix(result)
    
    def __mul__(self, other):
        """Performs a Hadamard product, or multiplies the value of every number in the matrix by the other"""
        if type(other) == matrix or type(other) == random_matrix:
            if other.shape == self.shape:
                result = [[] for i in range(self.shape[0])]
                for y in range(self.shape[0]):
                    for x in range(self.shape[1]):
                        result[y].append(self.matrix[y][x] * other.matrix[y][x])
                return matrix(result)
            else:
                raise ShapeError("The shapes do not align")
        elif type(other) == int or type(other) == float:
            result = [[] for i in range(self.shape[0])]
            for y in range(self.shape[0]):
                for x in range(self.shape[1]):
                    result[y].append(self.matrix[y][x] * other)
            return matrix(result)
    
    def __rmul__(self, other):
        """Performs a Hadamard product, or multiplies the value of every number in the matrix by the other"""
        if type(other) == matrix or type(other) == random_matrix:
            if other.shape == self.shape:
                result = [[] for i in range(self.shape[0])]
                for y in range(self.shape[0]):
                    for x in range(self.shape[1]):
                        result[y].append(self.matrix[y][x] * other.matrix[y][x])
                return matrix(result)
            else:
                raise ShapeError("The shapes do not align")
        elif type(other) == int or type(other) == float:
            result = [[] for i in range(self.shape[0])]
            for y in range(self.shape[0]):
                for x in range(self.shape[1]):
                    result[y].append(self.matrix[y][x] * other)
            return matrix(result)
    
    def __truediv__(self, other):
        """Divides the contents of one matrix to this one, or divides the value of every number in the matrix by the other"""
        if type(other) == matrix or type(other) == random_matrix:
            if other.shape == self.shape:
                result = [[] for i in range(self.shape[0])]
                for y in range(self.shape[0]):
                    for x in range(self.shape[1]):
                        try:
                            result[y].append(self.matrix[y][x] / other.matrix[y][x])
                        except ZeroDivisionError:
                            result[y].append(0)
                return matrix(result)
            else:
                raise ShapeError("The shapes do not align")
        elif type(other) == int or type(other) == float:
            if other == 0:
                raise ZeroDivisionError
            result = [[] for i in range(self.shape[0])]
            for y in range(self.shape[0]):
                for x in range(self.shape[1]):
                    result[y].append(self.matrix[y][x] / other)
            return matrix(result)
    
    def apply_function(self, function):
        """Apply a function to this matrix element by element"""
        result = [[] for i in range(self.shape[0])]
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                result[y].append(function(self.matrix[y][x]))
        return matrix(result)
    
    def Transpose(self):
        """Swaps the rows and columns of the matrix"""
        result = []
        for y in range(self.shape[1]):
            result.append([])
            for x in range(self.shape[0]):
                result[y].append(self.matrix[x][y])
        return matrix(result)
    
    def dot_product(self, other):
        """Performs a dot product operation to the matrix"""
        if self.shape[1] != other.shape[0]:
            raise ShapeError("The shapes of the matrices do not align")
        result = [[] for i in range(self.shape[0])]
        for y in range(self.shape[0]):
            for x in range(other.shape[1]):
                su = 0
                for i in range(self.shape[1]):
                    su += self.matrix[y][i] * other.matrix[i][x]
                result[y].append(su)
                del su
        return matrix(result)

from random import random
class random_matrix(matrix):
    def __init__(self, shape):
        """Creates a matrix with random starting values"""
        self.matrix = [[random() for x in range(shape[1])] for y in range(shape[0])]
        self.shape = shape
