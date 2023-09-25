
# This is going to accept 2 arguments :
#       1) The List we're searching through
#       2) The target value we're looking for. (Looking for it's position in the list)
#            It will be denoted by an "index value"
def linear_search( list, target ):
    """
    Returns the index position of the target if found, else returns None
    """
# i stands for index
    for i in range( 0, len(list) ):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index )
    else:
        print("Target not found in list.")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 4)
verify(result)