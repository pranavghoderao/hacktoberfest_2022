#Shree Ganeshaya Namah:
#Bubble sort works by comparing the neighboring elements and swaping them if needed.

#Let's air burst some bubbles. Shall we?

def bubble(arr):
    while True:
        i = 0
        flag = True
        while i<len(arr)-1:
            if arr[i]>arr[i+1]:
                flag = False
                arr[i],arr[i+1] = arr[i+1],arr[i]
            i += 1
        
        if flag:
            return arr

if __name__=="__main__":
    arr = [10,12,3,1,4,2,9,19,20,18]
    print(bubble(arr))
