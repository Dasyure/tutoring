
'''
Compute the average of only the positive elements in the list.
'''
def rainfall(integers):
    ''' List-comprehension solution '''
    positive = [i for i in integers if i > 0]
    if (len(positive) > 0):
        return sum(positive)/len(positive)
    else:
        return None
