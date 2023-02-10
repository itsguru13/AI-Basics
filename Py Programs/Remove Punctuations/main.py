import string

sentence = input("Enter a sentence: ")
sentence = sentence.translate(str.maketrans('','', string.punctuation))

print(sentence)