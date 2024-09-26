import random


def check_positive_number(prompt):
    '''Function to get valid numeric input from user'''
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please choose a number greater than 0\n")
        except ValueError:
            print("Please choose a number!")


def generate_password(nr_letters, nr_symbols, nr_numbers):
    '''Password generation function'''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Choosing random characters
    password = [random.choice(letters) for _ in range(nr_letters)] + \
               [random.choice(symbols) for _ in range(nr_symbols)] + \
               [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password)  # Mixing characters
    return ''.join(password)   # Returning the final password


def main():
    '''Main function'''
    print("\nWelcome to the PyPassword Generator!")

    while True:
        # Getting the number of characters from the user
        nr_letters = check_positive_number(
            "How many letters would you like in your password?\n")
        nr_symbols = check_positive_number(
            "How many symbols would you like?\n")
        nr_numbers = check_positive_number(
            "How many numbers would you like?\n")

        # Checking if there are enough characters for a valid password
        if nr_letters + nr_symbols + nr_numbers > 0:
            password = generate_password(nr_letters, nr_symbols, nr_numbers)
            print(f"Here is your password: {password}\n")
        else:
            print("Upss! We can't gnerate a password without characters! Try again! \n")

        while True:
            retry = input(
                "Do you want to try again?\nType 'y' for yes or 'n' for no.  ").lower()
            if retry in ["y", "n"]:
                break
            else:
                print("\nAnswer is not valid. Choose again.")

        if retry == "y":
            continue
        else:
            print("See you next time!")
            break


if __name__ == "__main__":
    main()
