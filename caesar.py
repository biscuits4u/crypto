def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lowercase_letter = letter.lower()
    return alphabet.index(lowercase_letter)

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.isalpha():
        x = alphabet_position(char)
        x = (x + rot) % 26
        x = (alphabet[x])
        if char.isupper():
            x = x.title()
        return x
    else:
        return char

def encrypt(text, rot):
    list1 = ""
    for char in text:
        list1 += rotate_character(char, rot)
    return list1


def main():
    message = input("Type a message:")
    rotation = input("Rotate by:")
    result = encrypt(message, rotation)
    print(result)

if __name__ == "__main__":
    main()    


