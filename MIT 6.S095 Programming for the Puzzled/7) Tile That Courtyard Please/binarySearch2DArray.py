def binarySearch2D(T, e):
    """
    A binary search algorithm that works for 2D lists
    that are sorted by rows and columns. Assumes that all 
    elements are unique.
    
    Quadrant definitions: 0(top left)         1(top right)
                          2(bottom left)      3(bottom right)
    
    Input:
    T (Square 2D matrix list of ints): all rows and all columns are sorted
    e (int): element to be searched for in T
    
    Returns:
    True if e in T
    False otherwise
    """
    def getMiddle(T):
        #First we get the size of T
        rows, columns = len(T), len(T[0])
        
        #Start Search at middle of array
        rmid = rows//2
        cmid = columns//2
        
        return rmid,cmid
    
    def binarySearch(T, e, rmid, cmid):
        
        #Indices out of range
        if (rmid>len(T)) or (cmid>len(T[0])) or (rmid<0) or (cmid<0):
            return False
        
        #e is in middle
        if T[rmid][cmid] == e:
            return (rmid, cmid)
        
        #e is greater than middle quad 0 eliminated
        elif (e > T[rmid][cmid]):
            
            #search quad 1
            if binarySearch(T, e, rmid - rmid//2, cmid + cmid//2):
                print(e, 'found at position: ('+rmid+', '+cmid)
                return True
            
            #search quad 2
            elif binarySearch(T, e, rmid + rmid//2, cmid - cmid//2):
                print(e, 'found at position: ('+rmid+', '+cmid)
                return True
            
            #search quad 3
            elif binarySearch(T, e, rmid + rmid//2, cmid + cmid//2):
                print(e, 'found at position: ('+rmid+', '+cmid)
                return True
            
            return False
        
        #e is less than middle quad 3 eliminated
        else:
            #search quad 1
            if binarySearch(T, e, rmid - rmid//2, cmid + cmid//2):
                print(e, 'found at position: ('+rmid+', '+cmid)
                return True
            
            #search quad 2
            elif binarySearch(T, e, rmid + rmid//2, cmid - cmid//2):
                print(e, 'found at position: ('+rmid+', '+cmid)
                return True
            
            #search quad 0
            elif binarySearch(T, e, rmid - rmid//2, cmid - cmid//2):
                print(e, 'found at position: ('+rmid+', '+cmid)
                return True
            
            return False
        

    rmid, cmid = getMiddle(T)
    binarySearch(T, e, rmid, cmid)

    
    

T	=	[[ 1,  4,  7, 11, 15],
         [ 2,  5,  8, 12, 19],
         [ 3,  6,  9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]]



binarySearch2D(T, 21)
