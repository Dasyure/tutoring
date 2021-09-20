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

def rainfall_alternative(integers):
    ''' List-comprehension solution '''
    positive = [i for i in integers if i > 0]
    if (len(positive) > 0):
        return sum(positive)/len(positive)
    else:
        return None
