def count_words(text):
   
    words = text.split()
    return len(words)
def rev_order(text):
    
    words = text.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
def replaced(text):
    
    return text.replace(" ", "-")
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print("Number of words:", count_words(input_string))
    print("Reversed sentence:", rev_order(input_string))
    print("Modified sentence:", replaced(input_string))
