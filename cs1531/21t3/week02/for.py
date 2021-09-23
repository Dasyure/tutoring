# Some for loop clarification
# Basically:
# range(5) == [0, 1, 2, 3, 4]


# For loop to print 0..9
for i in range(10):
    print(f"{i} ", end="")
print()

# For loop to print each word from word_list
my_word_list = ["My", "dog", "is", "cool"]
for word in my_word_list:
    print(word)

#For loop to print each word and its index from word_list
word_list = ["My", "dog", "is", "cool"]
for i, word in enumerate(word_list):
    print(f"Index: {i}, Word: {word}")
