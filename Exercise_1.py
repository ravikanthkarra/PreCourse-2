# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
    return helperbinSearch(arr, l, r, x)



def helperbinSearch(arr, l, r, x):

    if l > r:
        return -1

    mid = (l+r) // 2

    if x == arr[mid]:
        return mid
    elif x > arr[mid]:
      l = mid+1
      return helperbinSearch(arr, l, r, x)
    else:
      r = mid-1
      return helperbinSearch(arr, l, r, x)


# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}")
else: 
    print("Element is not present in array")
