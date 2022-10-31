#Shree Ganeshaya Namah:

#This one is the dedicated practice for sorting algorithm called Selection sort.
#Selection Sort works be finding out the minimum element in the sub-array and then placing it at the 0th position of that array.
#It sorts the array itself. No need to return anything.

#Let's Begin.

def selection(arr):
    i = 0
    while i<len(arr):
        mini = arr[i]
        temp = i
        for j in range(i,len(arr)):
            if arr[j]<mini:
                mini = arr[j]
                temp = j
        arr[i],arr[temp] = arr[temp],arr[i]
        i += 1

if __name__=="__main__":
  arr = [20,3,10,2,1,5,11,19,12,21,18]
  selection(arr)
  print(arr)
