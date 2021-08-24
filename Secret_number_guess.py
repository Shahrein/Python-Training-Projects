secret_number = 777

print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)

number = int(input("Enter the secret number: "))

while number != -1 :

    if number != secret_number:
        print("Ha ha! You are stuck in my loop now.")
    number = int(input("Enter the secret number: "))
    if number == secret_number:
        print("Well done, muggle! You are free now.")