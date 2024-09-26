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
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    # Choosing random characters
    password = [random.choice(letters) for _ in range(nr_letters)] + \
               [random.choice(symbols) for _ in range(nr_symbols)] + \
               [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password)  # Mixing characters
    return ''.join(password)   # Returning the final password

def ask_to_retry():
    '''Function to ask the user if they want to retry'''
    while True:
        retry = input(
            "Do you want to try again? Type 'y' for yes or 'n' for no.  ").lower()
        if retry in ["y", "n"]:
            return retry
        else:
            print("\nAnswer is not valid. Choose again.")


def main():
    '''Main function'''
    print("\nWelcome to the PyPassword Generator!")

    while True:
        # Getting the number of characters from the user
        nr_letters = check_positive_number(
            "\nHow many letters would you like in your password? ")
        nr_symbols = check_positive_number(
            "How many symbols would you like? ")
        nr_numbers = check_positive_number(
            "How many numbers would you like? ")

        # Checking if there are enough characters for a valid password
        if nr_letters + nr_symbols + nr_numbers > 0:
            password = generate_password(nr_letters, nr_symbols, nr_numbers)
            print(f"\nHere is your password: {password}\n")
        else:
            print("\nUpss! We can't gnerate a password without characters! Try again! \n")

        # Asking the user if they want to generate another password
        retry = ask_to_retry()

        if retry == "n":
            print("\nSee you next time!")
            break


if __name__ == "__main__":
    main()
