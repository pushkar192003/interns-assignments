def ispallindrome(text):

    cleaned_text = text.replace(" ", "").lower()
    
    
    return cleaned_text == cleaned_text[::-1]
if __name__ == "__main__":
    input_string = input("Enter a string: " )
    if ispallindrome(input_string):
        print(f"The string '{input_string}'is a palindrome.")
    else:
        print("The string is not a palindrome.")