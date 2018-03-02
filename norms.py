from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from random import *



def main():
    alst = [[0.2, -5, 3, 0.4, 0.0],[ -0.5 ,1 , 7 , -2 , 0.3 ],[0.6 ,2 ,-4 ,3 ,0.1 ],[3 ,0.8, 2,  -0.4, 3 ],[ 0.5,3,2,0.4,1]]
    ainv_lst = [[-0.7079,2.5314,2.4312,0.9666,-3.9023],[ -0.1934 , 0.3101 , 0.2795 , 0.0577 , -0.2941] , [0.0217 ,0.3655 ,0.2861 ,0.0506 ,-0.2899],[0.2734 ,-0.1299, 0.1316,  -0.1410, 0.4489],[ 0.7815 ,-2.8751 ,-2.6789 ,-0.7011, 4.2338]]

    a = np.array(alst)
    ainv = np.array(ainv_lst)

    print cond_num(a,ainv)





def infnorm(a):
    max_sum = 0.0
    m = len(a)
    n = len(a[0])

    for i in range(0,m):
        summ = 0.0
        for j in range(0,n):
            summ+= abs(a[i,j])
        if summ > max_sum:
            max_sum = summ
    return max_sum

def cond_num(a,ainv):
    return infnorm(a)*infnorm(ainv)




if __name__ == '__main__':
        main()
