from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from random import *

#a is coefficient matrix (it is rxc)
#b is right-hand-side (RHS) (it is cx1)
#x is the solution (it is cx1)

def augment(a,b):
    #set things up for Gaussian elim.
    ab = np.c_[a, b]  # we now should have the augmented form - this is just a python numpy library function
    return ab

def normalize(ab,i,order):
    #note this assumes it is part of a elimination scheme and only normalizes to the right of i,i
    ab_new =ab      #get a copy of ab
    n = len(ab)     #e.g. for 3x3 problem this would be 3
    norm = ab_new[order,i]  #This is the pivot ab_i,i
    for j in range(i,n+1):   #this will include i, i+1, ... n
        ab_new[order,j]=ab_new[order,j]/norm        #this is just dividing each element in row i by the value norm
    return ab_new

def backsub(ab, order):
    #this is to take a matrix in upper diagonal form and back solve for x's
    n = len(ab)     #get the number of rows
    x = np.empty(shape=(n,1)) #make an x vector to hold the solution
    x[n-1]=ab[order[n-1],n]/ab[order[n-1],n-1]    #find the solution for the last row before starting our loops
    for i in range(n-2,-1,-1):      #this starts at the next to last row and proceeds upward in the matrix
        sum = get_sum(ab,x,order,i)       #use our function get_sum to calculate the summation in the equation for this alg.
        x[i]=(ab[order[i],n]-sum)/ab[order[i],i]  #calc. x-value for the ith row
    return x

def get_sum(ab,x,order,i):
    summ = 0.0  #initialize our summation
    for j in range(i+1,n):          #start at column i+1 (just right of the diagonal / stop at n-1
        summ = summ + ab[order[i],j]*x[j]  #see algorithm in notes
    return summ

def forward_elim(ab):
    # Forward Elimination algorithm discussed in class
    n = len(ab)
    # create order vector and initially fill it with "ordered" indexes
    order = [0]
    for l in range(1,n):
        order.append(l)
    for i in range(0, n):  # loop to work on each pivot row from 0 to n-1
        #determine best row order so largest pivot is in a_i,i
        max = abs(ab[order[i],i])
        #print max, order, i
        for l in range(i+1,n):
            print abs(ab[order[l], i])
            if abs(ab[order[l],i]) > max:
                max = abs(ab[order[l],i])
                index = l
        #print i, index, order[i], order[index]
        #print ""
        tmp = order[i]
        order[i] = order[index]
        order[index] = tmp
        print order
        normalize(ab, i, order[i])  # normalize the equation so the pivot is 1.0

        for k in range(i + 1, n):  # loop to forward eliminate on row k - goes from i+1 to n-1
            for j in range(i + 1,
                           n + 1):  # loop to calculate new vals for each element on row k from i+1 to n (includes b)
                ab[order[k], j] = ab[order[k], j] - ab[order[k], i] * ab[order[i], j]

        print ab[order[0]]
        print ab[order[1]]
        print ab[order[2]]


    return ab, order

#make an array

#this is an example from class
a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
a = np.array(a_lst) #this makes a_lst an 2D array
b_lst = [-5.173, -5.458,4.415]
b= np.array(b_lst)

#print a,b
#a = np.empty(shape=(n,n))
#b = np.empty(shape=(n,1))

ab = augment(a,b)   #augment the b RHS vector on the right side of a
n = len(ab)         #number of rows in ab

ab_new, order = forward_elim(ab)

print ab[order[0]]
print ab[order[1]]
print ab[order[2]]

x = backsub(ab_new, order)
print x


