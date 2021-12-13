# -*- coding: utf-8 -*-
"""
Determining optimal fuel rate for an engine given a specific load

Code adapted from: https://www.geeksforgeeks.org/combinations-with-repetitions/ 

Comination with repeition
"""


# Python3 program to print all combination
# of size r in an array of size n
 
''' arr[] ---> Input Array
    chosen[] ---> Temporary array to store
               current combination
    start & end ---> Starting and Ending indexes in arr[]
    r---> Size of a combination to be printed
 
    '''
    
# Driver code
arr = [ 135, 101.25, 67.5, 33.75]
r = 3
n = len(arr) - 1    


def CombinationRepetitionUtil(chosen, arr, index, r, start, end, load, trial2):
                                   
    # Current combination is ready,
    # print it
    if index == r:
        summer = 0
        trial_rate = 0
        for j in range(r):
            print(chosen[j], end = " ")
            summer += chosen[j]
             
            
            if chosen[j] == 135:
                trial_rate = trial_rate + (40.9)
            if chosen[j] == 101.25:
                trial_rate = trial_rate + (33.2)
            if chosen[j] == 67.5:
                trial_rate = trial_rate + (23.9)
            if chosen[j] == 33.75:
                trial_rate = trial_rate + (14.7)    
        if summer >= load: 
        #     trial[chosen_sum] = str(chosen)# if chosen_sum >= Load:
        # #     cost_model = cost_model[j].append()
            trial2.update({trial_rate : chosen[j:]})
        #print("this trail greater than summer")
            
       #  print()
       # # print("SUMMER:")
       #  print("Load for this trial (summer): " + str('{0:.6g}'.format(summer)))
       #  print("Trial fuel rate: " + str("{0:.6g}".format(trial_rate)))
       #  print("Lowest rate so far: " + str(min(trial2.items())))
       #  print()
        
       #  temp = min(trial2.values())
       #  res = [key for key in trial2 if trial2[key] == temp]
          
       #  # printing result 
       #  print("Keys with minimum values are : " + str(res)  )
        
        
        #COME BACK TO THIS YOU ARE HERE TYRING TO GET THE CORRESPONDING GENERATOR VALUES TO PRINT OUT
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
    CombinationRepetitionUtil(chosen, arr, index + 1, r, start, end, load, trial2)
    CombinationRepetitionUtil(chosen, arr, index, r, start + 1, end, load, trial2)
    
    #return summer
    
# The main function that prints all
# combinations of size r in arr[] of
# size n. This function mainly uses
# CombinationRepetitionUtil()
def CombinationRepetition(arr, n, r):
     
    # A temporary array to store
    # all combination one by one
    chosen = [0] * r
    load = 260.28
    trial2 = {}     #This is the dictionary which hold the total rate 
    summer = 0
    trial_rate = 0


 
    # Print all combination using
    # temporary array 'chosen[]'
    CombinationRepetitionUtil(chosen, arr, 0, r, 0, n, load, trial2)
    # print("end")
    # print()
    # # print("SUMMER:")
    # print("Load for this trial (summer): " + str('{0:.6g}'.format(summer)))
    # print("Trial fuel rate: " + str("{0:.6g}".format(trial_rate)))
    # print("Lowest rate so far: " + str(min(trial2.items())))
    # print()
    
    # temp = min(trial2.values())
    # res = [key for key in trial2 if trial2[key] == temp]
      
    # # printing result 
    # print("Keys with minimum values are : " + str(res)  )
     

for load in load_list:
    
    CombinationRepetition(arr, n, r)

print("end")
print()
# print("SUMMER:")
print("Load for this trial (summer): " + str('{0:.6g}'.format(summer)))
print("Trial fuel rate: " + str("{0:.6g}".format(trial_rate)))
print("Lowest rate so far: " + str(min(trial2.items())))
print()

temp = min(trial2.values())
res = [key for key in trial2 if trial2[key] == temp]
  
# printing result 
print("Keys with minimum values are : " + str(res)  )
 
 
# This code is contributed by Vaibhav Kumar 12.