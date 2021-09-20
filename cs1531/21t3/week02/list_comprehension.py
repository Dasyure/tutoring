# https://www.w3schools.com/python/python_lists_comprehension.asp
# https://www.programiz.com/python-programming/list-comprehension

h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)


#######################################################

h_letters2 = [ letter for letter in 'human' ]
print( h_letters2)
