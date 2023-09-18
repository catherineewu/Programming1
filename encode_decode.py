def encode(password):
    # Catherine Wu
    list_password = []
    for letter in password:
        list_password.append(int(letter))
    for i in range(len(list_password)):
        list_password[i] += 3
        if list_password[i] > 9:
            list_password[i] -= 10
        list_password[i] = str(list_password[i])
    coded = ''.join(list_password)
    return coded


def main():
    menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n"

    while True:
        print(menu)
        option = int(input("Please enter an option: "))
        if option == 1:
            password_to_encode = input("Please enter your password to encode: ")
            encoded_password = encode(password_to_encode)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            try:
                print(f"The encoded password is {encoded_password}, and the original password is {password_to_encode}.\n")
            except EOFError:
                print("There is no password stored.")
        elif option == 3:
            break


if __name__ == '__main__':
    main()
