# Goal of this excercise:
# -> Move you away from C-style coding

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for num in num_list:
    if num % 2 == 0:
        result.append(num * 2)
    else:
        result.append(num)

print(result)

print([(num * 2 if num % 2 == 0 else num) for num in num_list])
## ^ Read it right to left

## ORIGINAL CODE:
# x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = []

# for idx in range(len(x)):
#   if x[idx] % 2 == 0:
#     result.append(x[idx] * 2)
#   else:
#     result.append(x[idx])

# print(result)
