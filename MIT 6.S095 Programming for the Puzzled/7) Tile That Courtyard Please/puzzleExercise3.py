def binarySearch2D(T, e):
    """
    A binary search algorithm that works for 2D lists
    that are sorted by rows and columns. Assumes that all 
    elements are unique.
        
    Input:
    T (2D matrix list of ints): all rows and all columns are sorted
    e (int): element to be searched for in T
    
    Returns:
    True if e in T
    False otherwise
    """
    rows, columns = len(T)-1, len(T[0])-1
    print(T[0][columns])
        
    #Start in top right
    if T[0][columns] == e:
        return True

    elif (rows == 0) and (columns == 0):
        return False
    
    #e is smaller than top right
    elif (T[0][columns] < e):
       return binarySearch2D(T[1:], e)
       
    # e is greater than top right
    else:
        T = [row[:-1] for row in T]
            
        return binarySearch2D(T, e)
    

T    =  [[ 1,  4,  7, 11, 15],
         [ 2,  5,  8, 12, 19],
         [ 3,  6,  9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]]



print(binarySearch2D(T, 20))
print(T)
print(binarySearch2D(T, 13))