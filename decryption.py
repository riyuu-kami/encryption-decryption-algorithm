def decrypt(word):
    __dict__ ={'0': 'a' , '1':'e' , '!':'i' , '2':'o' , '3':'u' , '@':'t' , '^':'w' , '$':'t' , '#':'l' , 'f':' '}
    word_lower = word.lower()
    reverse_lower = word_lower[::-1]
    decrypted_word = ""
    for char in reverse_lower:
        if char in __dict__:
            decrypted_word += __dict__[char]
        else:
            decrypted_word += char
    return(decrypted_word)
word_to_be_decrypted = input("enter word to be decrypted: ")
final = decrypt(word_to_be_decrypted)
print(final)
