import random
import string


def main():
    length = int(input("Enter the password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))

    print(f"\nGenerated password: {password}")


if __name__ == "__main__":
    main()
