morse_codes = {
    "a": ".-",
    'b': "-...",
    'c': "-.-.",
    'd': "-..",
    'e': ".",
    'f': "..-.",
    'g': "--.",
    'h': "....",
    'i': "..",
    'j': ".---",
    'k': "-.-",
    'l': ".-..",
    'm': "--",
    'n': "-.",
    'o': "---",
    'p': ".--.",
    'q': "--.-",
    'r': ".-.",
    's': "...",
    't': "-",
    'u': "..-",
    'v': "...-",
    'w': ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ' ': '/',
    '1': ".----", '2': "..---", '3': "....--", '4': "....-", '5': ".....",
    '6': "-....", '7': "--...", '8': "---..", '9': "----.", '0': "-----",
    '.': ".-.-.-", ',': "--..--", '?': "..--..", '!': "-.-.--",
    "'": ".----.", '"': ".-..-.", '(': "-.--.", ')': "-.--.-",
    '&': ".-..", ':': "---...", ';': "-.-.-.", '/': "-..-.",
    '=': "-...-", '+': ".-.-.", '-': "-...-", '$': "...-..-",
    '@': ".--."

}

word = input("Enter a word: ").lower()


def encode():
    for letter in word:
        print(morse_codes[letter], end=" ")


def decode():
    code_list = word.split(" ")
    if len(code_list) >= 9:
        code_list.remove(code_list[len(code_list) - 1])
    for code in code_list:
        print(list(morse_codes.keys())
              [list(morse_codes.values()).index(code)], end="")


def main():
    if word[0] == "-" or word[0] == ".":
        try:
            decode()
        except ValueError:
            print("The morse code contains invalid character please try again!")
    else:
        try:
            encode()
        except KeyError:
            print("The word or phrase you've provided contains invalid characters. we can only convert the letters "
                  "A-Z, "
                  "numbers, and spaces to Morse Code in this program.")


if __name__ == '__main__':
    main()
