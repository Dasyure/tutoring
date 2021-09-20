for i in range(10):
    print(f"{i} ", end="")
print()

word_list = ["My", "dog", "is", "cool"]
for word in word_list:
    print(word)

word_list = ["My", "dog", "is", "cool"]
for idx, word in enumerate(word_list):
    print(f"Index: {idx}, Word: {word}")
