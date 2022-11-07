#objective: build a guess game print a quess and ask user to guess the thing related to.

print("what has long neck and strong head, strong but vegitable?")
print("You have 3 attempts")
answer="giraffe"
guess=""
guess_count=0
guess_limit=3
out_of_guess=False

while guess != answer and not(out_of_guess):
    if guess_count < guess_limit:
        guess=input("Enter Guess: ") 
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("You are out of limit to guess, try again later")
else:
    print("Correct answer")
