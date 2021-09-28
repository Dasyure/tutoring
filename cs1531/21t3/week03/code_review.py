'''
TODO Complete this file by following the instructions in the lab exercise.
'''
strings = ['This', 'list', 'is', 'now', 'all', 'together']
# print(' '.join(strings))

### Example 1
finalString = ""
for x in range(len(strings)):
    if x == 0:
        finalString += strings[x]
    else:
        finalString += " "
        finalString += strings[x]
print(finalString)

### Example 2
# code is less flexible with print statement inside, use variable
# don't iterate until a fixed number
for word in strings[0:5]:
    print(word, end = ' ')
print(strings[5])


#### PYTHONIC SOLUTION ####
final = ""
for i in strings:
    final += i + " "
print(final[:-1])

