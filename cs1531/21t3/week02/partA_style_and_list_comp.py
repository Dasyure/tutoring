# Goal of this excercise:
# -> Move you away from C-style coding


##############################
### 1) ORIGINAL CODE:

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultx = []

for idx in range(len(x)):
  if x[idx] % 2 == 0:
    resultx.append(x[idx] * 2)
  else:
    resultx.append(x[idx])
print(resultx)



##############################
### 2) FIXED FOR STYLE:

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for num in num_list:
    if num % 2 == 0:
        result.append(num * 2)
    else:
        result.append(num)
print(result)



##############################
### 3) INTRO TO LIST COMPREHENSION
###    Sort of like ternary operators:
###    value_if_true if condition else value_if_false

numm_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = []

for num in numm_list:
    results.append(num * 2 if num % 2 == 0 else num)
print(results)



##############################
### 4) LIST COMPREHENSION
###    Tip: Read it right to left
my_list = [(num * 2 if num % 2 == 0 else num) for num in num_list]
print(my_list)
