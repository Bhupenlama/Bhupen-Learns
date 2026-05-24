#count the total number of vowels in a given sentence.case-insensitive.
sentence = input("Enter a sentence: ")
count = 0
vowels = "aeiouAEIOU"
for char in sentence:
    if char in vowels:
        count += 1  
        print("Vowels:",count)