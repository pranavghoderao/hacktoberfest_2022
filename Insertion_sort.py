#Shree Ganeshaya Namah:

#Insertion sort works by comparing two adjacent elements and swapping them if needed. It also make use of backtracking.
#We create a virtual sorted subarray inside the array to fulfill the task

#So, let's do it.

def insertion(arr):
    i = 0
    while i<len(arr)-1:
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]= arr[i+1],arr[i]
            if i>0:
                i -= 1
        else:
            i += 1
    return arr

if __name__=="__main__":
    arr = [10,3,11,13,12,19,15,20,18,2,5,1,4,9]
    print(insertion(arr))
