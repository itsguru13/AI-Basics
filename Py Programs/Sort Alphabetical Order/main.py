sentence = input("Type something: ")
words = [word.lower() for word in sentence.split()]

words.sort()

print("The sorted words are: ")
for word in words:
    print(word)