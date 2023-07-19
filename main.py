def encode(x):
    enc_password1 = ''
    for i in x:
        enc_char = chr(ord(i) + 3)
        enc_password1 += enc_char
    return enc_password1


def main():

    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
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
            print('\nExiting program:)')
            break


if __name__ == "__main__":
    main()

