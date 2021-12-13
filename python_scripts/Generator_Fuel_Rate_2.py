#OPTIMIZATION COST FOR ONLY GENERATORs
#Code adapted from: https://www.geeksforgeeks.org/combinations-with-repetitions/
#This function shows the fuel consumption rate of "n" generators.
#The output will show the total fuel rate for n generators, follwed by each individual generator fuel rate

#Combination code for generator
import numpy
import matplotlib.pyplot as plt
import openpyxl
from itertools import combinations


# Python3 program to print all combination
# of size r in an array of size n
 
''' arr[] ---> Input Array
    chosen[] ---> Temporary array to store
               current combination
    start & end ---> Starting and Ending indexes in arr[]
    r---> Size of a combination to be printed
 
    '''
    # Driver code

#Cost of fuel
fuel_cost = 1           #$/L


#Fuel consumption rate (L/hr)
#100_rate = 40.9
# 75_rate = 33.2
# 50_rate = 23.9
# 25_rate = 14.7

#Setting parameters
arr = [ 135, 101.25, 67.5, 33.75 ]
#This is the hourly average for each month
load_demand = [260.28, 273.89, 279.41, 264.38, 263.81, 257.51, 243.32, 248.20, 257.63, 266.87, 273.45, 265.63]
generator = 3 #possible number of generators 
r = 3
n = len(arr) - 1


def CombinationRepetitionUtil(chosen, arr, index, r, start, end, load, trial):
                                   
    # Current combination is ready,
    # print it
   
    if index == r:
        range_sum = 0
        trial_rate = 0

        for j in range(r):
           # print(chosen[j], end = " ")
           # print("hi")
           
            if chosen[j] == 135:
                trial_rate = trial_rate + (40.9)
            if chosen[j] == 101.25:
                trial_rate = trial_rate + (33.2)
            if chosen[j] == 67.5:
                trial_rate = trial_rate + (23.9)
            if chosen[j] == 33.75:
                trial_rate = trial_rate + (14.7)  
               
            range_sum += chosen[j]
        # print("HERE")
        # print("Output power from trial: " + str(range_sum))
        # print("Fuel rate from trial: " + str(trial_rate))
        # print()
        
        if range_sum >= load: 
            
            trial[range_sum] = float('{0:.2f}'.format(trial_rate))   # if chosen_sum >= 376.1:
        #     cost_model = cost_model[j].append()
            #trial.update({range_sum : chosen[j:]})
        return 
    # When no more elements are
    # there to put in chosen[]
    if start > n:
        return 

    # Current is included, put
    # next at next location
    chosen[index] = arr[start]
     
    # Current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)
    CombinationRepetitionUtil(chosen, arr, index + 1, r, start, end, load, trial)
    CombinationRepetitionUtil(chosen, arr, index, r, start + 1, end, load, trial)
 
# The main function that prints all
# combinations of size r in arr[] of
# size n. This function mainly uses
# CombinationRepetitionUtil()
def CombinationRepetition(arr, n, r):
     
    # A temporary array to store
    # all combination one by one
    chosen = [0] * r
 
    # Print all combination using
    # temporary array 'chosen[]'
    #load = 280
    trial = {}

    fuel_used = 0

    for load in load_demand:

        CombinationRepetitionUtil(chosen, arr, 0, r, 0, n, load, trial)
        
        print("MINIMUM fuel rate FOR " + str(load))
        print(min(trial.items()))
        min_rate = min(trial.items())
        
        fuel_used += min_rate[1]
        print(fuel_used)
    print()
    print("TOTAL fuel used in day")
    print(('{0:.2f}'.format(fuel_used)) + " L/day")

 
CombinationRepetition(arr, n, r)
 
