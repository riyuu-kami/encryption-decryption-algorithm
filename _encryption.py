def encrypt(word):
	dict_ = {'a': '0' , 'e':'1' , 'i':'!' , 'o':'2' , 'u':'3' , 't':'@' , 'w':'^' , 't':'$' , 'l':'#'}
	word_lower = word.lower()
	reverse_lower = word_lower[::-1]
	encrypted_word = ""
	for char in reverse_lower:
		if char in dict_:
			encrypted_word += dict_[char]
		else:
			encrypted_word += char
	return(encrypted_word)
word_to_be_encrypted = input("enter word to encrypt: ")
final = encrypt(word_to_be_encrypted)
print(final)