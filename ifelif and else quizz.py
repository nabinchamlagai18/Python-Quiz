print("Welcome to the Python Quiz! ezz game")
score = 0

print("\nQuestion 1: What is the capital of France?")
answer1 = input("a) London\nb) Paris\nc) Rome\nYour answer: ")

if answer1.lower() == "b":
    print("Correct!")
    score += 1
elif answer1.lower() in ["a", "c"]:
    print("Incorrect.")
else:
    print("Invalid choice.")


print("\nQuestion 2: What is 5 * 3?")
answer2 = input("a) 8\nb) 15\nc) 10\nYour answer: ")

if answer2.lower() == "b":
    print("Correct!")
    score += 1
elif answer2.lower() in ["a", "c"]:
    print("Incorrect.")
else:
    print("Invalid choice.")


print("\nQuestion 3: Which language is this program written in?")
answer3 = input("a) Python\nb) Java\nc) C+\nYour answer: ")

if answer3.lower() == "a":
    print("Correct!")
    score += 1
elif answer3.lower() in ["b", "c"]:
    print("Incorrect.")
else:
    print("Invalid choice.")


print(f"\nYour final score is: {score}/3")

if score == 3:
    print("Excellent! You got all correct.")
elif score == 2:
    print("Great job! Almost perfect.")
elif score == 1:
    print("You got 1 right. Keep practicing!")
else:
    print("Oops! Try again.")
