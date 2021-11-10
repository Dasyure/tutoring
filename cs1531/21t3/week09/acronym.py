def acro(input):
    return "".join([word[0].upper() for word in input.split()])

if __name__ == '__main__':
    print(f"It's acronym is {acro(input('What is the name? '))}.")
