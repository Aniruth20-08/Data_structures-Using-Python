'''def  binary_search(values,target):
    low=0
    high=len(values)-1

    while low<=high:
        mid=((high+low)//2)
    if values[mid]==target:
        return True
    elif target < values[mid]:
        high=mid-1
    else:
        low=mid + 1

    return False

val=[10,20,30,40,50,60]
tar=60
if binary_search(val,tar):
    print("target Found")
else:
    print('target not found')
'''
from math import floor
def binary_search(Array, Search_Term):
    n = len(Array)
    L = 0
    R = n-1
    
    while L <= R:
        mid = floor((L+R)/2)
        if Array[mid] < Search_Term:
            L = mid + 1
        elif Array[mid] > Search_Term:
            R = mid - 1
        else:
            return mid
    return -1


# Insert your array here
A = [1,2,3,4,7,9,12,14,18]
# term to be searched
term = 14
index = binary_search(A, term)
if index >= 0:
    print("{} is at index {}".format(A[index], index))
else:
    print("Search term not found")
