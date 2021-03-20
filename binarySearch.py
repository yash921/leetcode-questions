# #Solution-1-->Using recursion
def binarySearch(array, target):
    """
    Time = O(log(n)) | Space = O(log(n))
    """
    return helperfun(array, target, 0, len(array) - 1)

def helperfun(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMiddle = array[middle]
    if potentialMiddle == target:
        return middle
    
    elif potentialMiddle > target:
        return helperfun(array, target, left, middle - 1)
    else:
        return helperfun(array, target, middle + 1, right)


<-------------------------------------------------------------->


   
#Solution-2-->    
def binarySearch(array, target):
    """
    Time = O(log(n)) | Space = O(1)
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        potentialMiddle = array[middle] 
        if potentialMiddle == target:
            return middle
        elif potentialMiddle > target:
            right = middle - 1     
        else:
            left = middle + 1
    return -1

print(binarySearch([1,2,3,4,5,6,7,8,9], 8))