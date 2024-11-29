morse_code = {
    "a": "._",
    "b": "_...",
    "c": "_._.",
    "d": "_..",
    "e": ".",
    "f": ".._.",
    "g": "__.",
    "h": "....",
    "i": "..",
    "j": ".___",
    "k": "_._",
    "l": "._..",
    "m": "__",
    "n": "_.",
    "o": "___",
    "p": ".__.",
    "q": "__._",
    "r": "._.",
    "s": "...",
    "t": "_",
    "u": ".._",
    "v": "..._",
    "w": ".__",
    "x": "_.._",
    "y": "_.__",
    "z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____",
    ".": "._._._",
    ",": "__..__",
    "?": "..__..",
    "/": "_.._.",
    "@": ".__._."
}
state = input("cypher or decypher?")
state = state.lower()
if state == "cypher":
    #  Cyphering the word
    user = input("Please tell me your secret message:\n")
    final_word = []
    test_list = [i for i in user]
    for i in test_list:
        final_word.append(morse_code[i])
    print(" ".join(final_word))
elif state == "decypher":
    # deciphering the word
    translated_word = []
    user = input("Please enter your coded message:\n")
    reversed_morse_dic = {value: key for key, value in morse_code.items()}
    morse_word = user.split(" ")
    for i in morse_word:
        translated_word.append(reversed_morse_dic[i])
    deciphered_word = "".join(translated_word)
    print(deciphered_word)
else:
    print("Please enter a valis state")
