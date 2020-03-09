#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:28:02 2019

@author: jivila
"""
import numpy as np

def cost_calculator(prices, input_matrix, quantities):
    '''
    Description:
    
    inputs:
        prices= vector of prices of the inputs
        quantities = vector of the desire quantities to produce
        input_matrix = matrix that specifiy the quantities of factors to produce one quantitie.
    output:
        total cost
    '''
    p_by_matrix = np.dot(input_matrix, prices)
    total_cost = np.dot(q, p_by_matrix)
    rv =print("Total Cost equal to "+str(total_cost)+"\n"+"The price for one " +"Road is $"+str(p_by_matrix[0])+"\n"+"The price for one " +"Settlement is $"+str(p_by_matrix[1])+"\n"+"The price for one " +"City is $"+str(p_by_matrix[2])+"\n"+"The price for one " +"Dev. Card is $"+str(p_by_matrix[3]))
    return rv

prod_matrix =[[1,0,0,0,1],[1,1,1,0,1],[0,2,0,3,0],[0,1,1,1,0]]
p = [1,5,3,8,2]
q = [1,1,1,1]

cost_calculator(p,prod_matrix,q)