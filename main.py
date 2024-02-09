# firstly we import Counter from collections (module)
from collections import Counter



# here we Define the functions to check if any re-aarangment of the pattern exists in the text
def occurance_scribble_text(pattern, text):
    # here we Calculate the lengths of the pattern and the text.
    pattern_len = len(pattern)
    text_len = len(text)

    
    #  pattern and text length must be between 1-100 and 1-100000 respectively
    if pattern_len > 100 or  text_len > 100000:
        print("pattern length must be between 1-1000")
        print("text length must be between 1-100000")


    
    # here we count the occurrences of each character in the pattern and the initial slice of the text
    pattern_count = Counter(pattern)
    text_count = Counter(text[:pattern_len])
    
    # here we run for loop for iterating through character of pattern and text.
    for i in range(pattern_len, text_len):
        
        #if text count is similar to pattern count it return "yes"
        if text_count == pattern_count:
            return "YES"
        
        # Update the counts of characters in the text slice
        text_count[text[i-pattern_len]] -= 1 #her is text_count is a dictionary that counts the occurrences of characters in a slice of text.

        if text_count[text[i-pattern_len]] == 0: #This line checks if the count of the character that was just decremented has become zero.
            del text_count[text[i-pattern_len]] #If the count is zero, it means that character is no longer in the slice of text.

        text_count[text[i]] += 1 #Here the  text[i] accesses the character that is at the current position i in the text.



    return "YES" if text_count == pattern_count else "NO"

# Input
# Read the number of test cases
T = int(input("Enter the number of test cases: "))

# here we iterate througheach test cases
for i in range(T):
    
    # we take the input as pattern and text 
    pattern = input("Enter the pattern: ").strip()
    text = input("Enter the text: ").strip()
    
    # Output
    # Call the function to check if any permutation of the pattern exists in the text and print the result
    print("Output:", occurance_scribble_text(pattern, text))
