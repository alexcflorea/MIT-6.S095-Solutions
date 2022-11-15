#Programming for the Puzzled -- Srini Devadas
#The Disorganized Handyman
#A recursive sorting algorithm based on pivoting where a pivot is selected
#and the list split into three lists: the first containing elements smaller
#than the pivot, second elements equal to the pivot, and the third containing
#elements greater than the pivot. These sublists are recursively sorted.


#This procedure selects a pivot and partitions the list into 3 sublists
#It uses using another list as auxiliary storage and returns the pivot
def pivotPartition(lst, start, end):
    pivot = lst[end]
    less = []
    pivotList = []
    more = []

    for e in lst:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            pivotList.append(e)
        
    i = 0
    for e in less:
        lst[i] = e
        i += 1
    for e in pivotList:
        lst[i] = e
        i += 1
    for e in more:
        lst[i] = e
        i += 1

    #print ('Pivot element is: ', pivot)
    return lst.index(pivot)


#This procedure sorts the list recursively using pivot-based partitioning
#at each step
def quicksort(lst, start, end):
    if start < end:
        split = pivotPartition(lst, start, end)
        #print (lst[start:end+1])
        quicksort(lst, start, split - 1)
        quicksort(lst, split + 1, end)
    else:
        return
    
    
#This procedure finds the kth smallest element in unsorted list
#assuming all elements in list are unique
def quickselect(lst, start, end, k):
    if k > len(lst) or k <= 0:
        raise ValueError()
    
    elif start <= end:
        split = pivotPartition(lst, start, end)
        
        pivot = lst[split]
        less = lst[0:split]
        
        if len(less) == k-1:
            return pivot
        
        elif len(less) >= k:
            return quickselect(lst, start, split - 1, k)
        
        else:
            return quickselect(lst, split + 1, end, k)
            
    
            
    
    
    
a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
print ('Initial list is:', a)

k = 8
print('{} smallest element is: {}'.format(k, quickselect(a, 0, len(a) - 1, k)))
print('current list:  ', a)

quicksort(a, 0, len(a) - 1)
print ('Sorted list is:', a)