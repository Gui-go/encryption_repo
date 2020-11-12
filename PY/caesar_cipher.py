def caeser_cipher_encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + s)).upper()
        elif (char.islower()):
            result += chr((ord(char) + s)).lower()
        elif (char == ' '):
            result += ' '
    return result

# text = "CEASER CIPHER DEMO"
# s = 1

# print(f'Plain Text : {text}')
# print(f'Shift pattern : {str(s)}')
# print(f'Cipher: {encrypt(text,s)}')


