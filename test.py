

def encode(password):
    encoded_pass = ''
    for char in password:
        char = int(char) + 3
        encoded_pass += str(char)
    return encoded_pass

print(encode('123455555'))
