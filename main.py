# Daniel Mata
#-# Mason Fields, Also Adding Code Comments!
# I'll add some comments to my code

def encode(x): # Encodes the password, adds 3 units to each element in password
    enc_password1 = ''
    for i in x:
        enc_char = chr(ord(i) + 3)  #-# I suggest subtracting the ord by 10
        enc_password1 += enc_char   #-# Just in case you try to encode 7, 8, or 9
    return enc_password1


def main(): # Main function

    while True:
        print('Menu') # Printing the menu
        print('-------------') #-# Could clean this up by just doing \n, but I
        print('1. Encode')     #-# Understand why this might be simpler
        print('2. Decode')
        print('3. Quit')

        option = int(input('Please enter an option: '))

        if option == 1:
            password = input('Please enter your password to encode: ')
            enc_password = encode(password)
            print('Your password has been encoded and stored! \n')

        if option == 2:
            print(f'The encoded password is {enc_password}, and the original password is {password}.\n')

        if option == 3:
            print('\nExiting program')
            break


if __name__ == "__main__":
    main()

