# Function that determines if a string has all unique characters.
# True = Unique, False = Not Unique.
def uniqString (word):
    # Length of the word
    wordLen = len(word)
    
    # Run through each character of the word to check for duplicates.
    # Runs at O(n log n)
    for i in range(wordLen):
        for j in range(i+1, wordLen):
            if word[i] == word[j]:
                return False
    # If it runs through the whole word with no problems then this is a word with unique characters.
    return True
