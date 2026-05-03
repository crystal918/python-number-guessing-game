import random

best_score = None  # Keeps track of the best score

while True:
    print("\nChoose a difficulty level:")
    print("1. Easy (1–50)")
    print("2. Medium (1–100)")
    print("3. Hard (1–500)")
    print("4. Quit")

    try:
        choice = int(input("Enter 1, 2, 3, or 4: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 4:
        print("Thanks for playing! Goodbye 👋")
        break

    if choice == 1:
        secret = random.randint(1, 50)
        max_num = 50
    elif choice == 2:
        secret = random.randint(1, 100)
        max_num = 100
    elif choice == 3:
        secret = random.randint(1, 500)
        max_num = 500
    else:
        print("Invalid choice, try again.")
        continue

    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {max_num} (or 0 to quit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == 0:
            print("Game exited. The secret number was", secret)
            break

        attempts += 1

        if guess > secret:
            print("Too high, try again 🙂")
        elif guess < secret:
            print("Too low, try again 🙂")
        else:
            print(f"Good job, you got it in {attempts} tries! 🎉")

            # Update scoreboard
            if best_score is None or attempts < best_score:
                best_score = attempts
                print("🏆 New best score!")
            else:
                print(f"Your best score so far is {best_score} attempts.")

            break