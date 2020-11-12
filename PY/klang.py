def klang_encrypt(text):
    result = ""
    for i in range(len(text)):
        char = text[i].lower()
        
        if(char=='a'):
            result += 'k1'
        elif(char=='e'):
            result += 'k2'
        elif(char=='i'):
            result += 'k3'
        elif(char=='o'):
            result += 'k4'
        elif(char=='u'):
            result += 'k5'
        else:
            result += char
    return result

# text = "CEASER CIPHER DEMO"

# print(f'Plain Text : {text}')
# print(f'Cipher: {klang_encrypt(text)}')

