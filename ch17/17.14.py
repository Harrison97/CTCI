import doctest
import heapq

def smallest_k(arr, k):
    heapq.heapify(arr)
    return heapq.nsmallest(k, arr)

