def find_vowels(message):
    # vowels = {'a':0, 'e':0, 'i':0, ...}
    vowels = {}
    for character in message:
        if character.isupper():
            raise ValueError
        if character in 'aeiou':
            vowels[character] = vowels.get(character, 0) + 1
    return vowels

if __name__ == '__main__':
    words = input('Please enter a series of words: ')
    try:
        print(find_vowels(words))
    except ValueError:
        print("Please only use lowercase")
