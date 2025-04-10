import string

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return s.title()

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

if __name__ == "__main__":
    test = "my, little, Pony!"
    print("Reverse:", reverse_string(test))
    print("Capitalize:", capitalize_words(test))
    print("No Punctuation:", remove_punctuation(test))
