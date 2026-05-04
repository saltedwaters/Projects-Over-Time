questions = ("What Grade sorcerer is Gojo Satoru?:",
             "What cursed tool Toji use?:",
             "What cursed technique does Inumaki have?:",
             "Which of the disaster curses have the highest firepower?")

options = (("A. Grade 3", "B. Grade 2", "C. Grade 1", "D. Special Grade"),
           ("A. None", "B. Inverted Spear of Heaven", "C. Playful Cloud"),
           ("A. Copy", "B. Infinity", "C. Cursed Speech", "D. Shrine"),
           ("A. Jogo", "B. Hanami", "C. Mahito", "D. Dagon"))

answers = ("D", "B", "C", "A")

guesses = []

score = 0

question_number = 0

for question in questions:
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter A, B, C, or D: ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_number]} is the correct answer")
    question_number += 1

    print(f"Your score is: {score}")
