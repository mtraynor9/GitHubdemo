#def encoder
# Caio # Mike


# this is the encode function:
def encode(password):
    encoded_pass = ''
    #takes in each character
    for char in password:
        #adds three to the pass word
        char = int(char) + 3
        encoded_pass += str(char)
    # returns modified pass word
    return encoded_pass

#This is the decoded function!
def decode(encoded_password):
    decoded_pass = " "
    for char in encoded_password:
        char = int(char) - 3
        decoded_pass += str(char)
    return decoded_pass




Continue = True
#While loop
while Continue:
    print('\nMenu \n------------- \
            \n1. Encode  \
            \n2. Decode \
            \n3. Quit\n ')

    option = int(input('Please enter an option: '))

    if option == 1:
        password = input('Enter your password to encode: ')
        # here you encode your password and store it!
        encoded_password = encode(password)
        #password encoded statement:
        print('Your password has been encoded and stored!')


    if option ==2:
        original_pass = decode(encoded_password)  # Sets original_pass to decoded version of the encoded password
        print(f'The encoded password is {encoded_password}, and the original password is {original_pass}.')  # string allows looped function

    if option == 3:
        #terminates the loop
        Continue = False











