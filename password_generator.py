import string
import secrets

print("===== PASSWORD GENERATOR =====")

while True:
    print("\nSelect password complexity:")
    print("1. Only Letters")
    print("2. Letters and Numbers")
    print("3. Letters, Numbers and Symbols")

    choice = input("Select your option (1/2/3): ")

    if choice not in ["1", "2", "3"]:
        print("Invalid option!")
        continue

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == "1":
        characters = string.ascii_letters

    elif choice == "2":
        characters = string.ascii_letters + string.digits

    else:
        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

    password = ""

    for i in range(length):
        password = password + secrets.choice(characters)

    print("\nGenerated Password:", password)

    again = input("\nGenerate another password? (yes/no): ").lower()

    if again != "yes":
        print("Password Generator closed.")
        break
