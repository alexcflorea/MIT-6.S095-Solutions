#Programming for the Puzzled -- Srini Devadas
#The Disorganized Handyman
#A recursive sorting algorithm based on pivoting where a pivot is selected
#and the list split into three lists: the first containing elements smaller
#than the pivot, second elements equal to the pivot, and the third containing
#elements greater than the pivot. These sublists are recursively sorted.


#This procedure selects a pivot and partitions the list into 3 sublists
#It only uses one element worth of additional storage for the pivot!
def pivotPartitionClever(lst, start, end):
    pivot = lst[end] 
    bottom = start - 1       
    top = end
    iterations = 0

    done = False
    while not done: 

        while not done:
            #Move rightward from left searching for element > pivot
            bottom += 1 
            iterations += 1
            if bottom == top: 
                done = True 
                break
            if lst[bottom] > pivot: 
                lst[top] = lst[bottom] 
                #print (lst, 'bottom =', bottom, 'top = ', top)
                break 

        while not done:
            #Move leftward from right searching for element < pivot
            top -= 1
            iterations += 1
            if top == bottom: 
                done = True 
                break
            if lst[top] < pivot: 
                lst[bottom] = lst[top] 
                #print (lst, 'bottom =', bottom, 'top = ', top)
                break 

    lst[top] = pivot 
    #print (lst)
    return top, iterations


def quicksort(lst, start, end):
    iterations = 0
    
    if start < end: 
        #print ('Partition start: bottom =', start - 1, 'top = ', end)
        #print (lst)
        split, iterations = pivotPartitionClever(lst, start, end)
        #print ('Partition end')
        iterations += quicksort(lst, start, split - 1)
        iterations += quicksort(lst, split + 1, end)
        
    return iterations
    
a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
print ('Initial list is:', a)
print('Total number of iterations: {}'.format(quicksort(a, 0, len(a) - 1)))
print ('Sorted list is:', a)
print()

L = list(range(100))
print ('Initial list is:', L)
print('Total number of iterations: {}'.format(quicksort(L, 0, len(L) - 1)))
print ('Sorted list is:', L)
print()

D = list(range(99, -1, -1))
print ('Initial list is:', D)
print('Total number of iterations: {}'.format(quicksort(D, 0, len(D) - 1)))
print ('Sorted list is:', D)
print()
# Iterations for D (worst case) is ([N(N+1)]/2)-1 the -1 is from ignoring the last
# switch
# ------------------
# There is no difference in # of iterations between L and D because both lists are
# sorted. The only difference is quicksort moves the entire list either to right or
# left of the pivot

R = [0] * 100
R[0] = 29
for i in range(100):
    R[i] = (9679 * R[i-1] + 12637 * i) % 2287
print ('Initial list is:', R)
print('Total number of iterations: {}'.format(quicksort(R, 0, len(R) - 1)))
print ('Sorted list is:', R)
print()