#Write a Python program that takes a sentence from the user and prints:

def count_words(words):
    print("Number of words in the sentence:", len(words))

def count_characters(words):
    char_count=0
    for word in words:
        char_count += len(word)
    print("Number of characters in the sentence :", char_count)

def count_vowels(words):
    vowels='aeiouAEIOU'
    vouwel_count=0
    for words in words:
        for char in words:
            if char in vowels:
                vouwel_count += 1
    print("Number of vowels in the sentence:", vouwel_count)


sentance=input("Enter a sentence: ")
words=sentance.split()

print(words)
count_words(words)
count_characters(words)
count_vowels(words)