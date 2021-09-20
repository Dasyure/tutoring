
'''
Compute the average of only the positive elements in the list.
'''
def rainfall(integers):
    ''' Single-loop solution '''
    total = 0
    count = 0
    for i in integers:
        if  i > 0:
            total += i
            count += 1
    if (count > 0):
        return total/count
    else:
        return None
