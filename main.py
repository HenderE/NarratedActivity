secret_number = 7
max_attempts = 5
attempts_used = 0

while attempts_used < max_attempts:
    print(f"\nAttempt {attempts_used + 1} of {max_attempts}")
    user_input = input("\nGuess the number: ")
    guess = int(user_input)
    attempts_used = attempts_used + 1
    
    if guess == secret_number:
        print("\nAmazing! You won the game.")
        break
    elif guess < secret_number:
        print("\nClose... the secret number is higher.")
    else:
        print("\nToo high! The secret number is lower.")

if attempts_used == max_attempts and guess != secret_number:
    print(f"\nOut of attempts. The number was {secret_number}.")