#Shree Ganeshaya Namah:
#Merge sort makes use of the Divide And Conquer concept.
#In this we first split the array upto unit length and then we merge them according to their value order.

#Let's Start:


def merging(arr1,arr2):
  """Returns the sorted array from two different arrays"""
    i,j=0,0
    s = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            s.append(arr1[i])
            i += 1
        else:
            s.append(arr2[j])
            j+=1
    if i<len(arr1):
        s += arr1[i:]
    else:
        s+= arr2[j:]
    return s
  

def merge(arr):
  """Returns the sorted array by making use of recursion and merging function
  Here first we divide the array into two parts and repeat the process up to unit length of arrays
  then we return the sorted array from it using the merging function."""
    if len(arr)<=1:
        return arr
    n = len(arr)//2
    l = merge(arr[:n])
    r = merge(arr[n:])
    return merging(l,r)
  


 if __name__=="__main__":
  arr = [10,22,19,2,3,5,16,11,20,1,4,5,8]
  print(merge(arr))
