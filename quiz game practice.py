#-----------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("#-----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#-----------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("your correct pookie bear!")
        return 1
    else:
        print("Wrong baby boo")
        return 0

#-----------------------------
def display_score(correct_guesses, guesses):
    print("#-----------------------------")
    print("RESULTS")
    print("#-----------------------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(questions.get(i), end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("your score is: "+str(score)+"%")
#-----------------------------
def play_again():

    response = input("Do you want play aggain? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#-----------------------------


questions = {
  "Who is the most beautiful?: ": "A",
  "What is an apple?: ": "B",
  "What is my full name?: ": "C",
  "Is the earth round?: ": "A"
}

options = [["A. My girlfriend", "B. her", "C. IDK", "D. Hmmmmm"],
           ["A. A food", "B. Fruit", "C. Vegetable?", "D. something?"],
           ["A. Josh", "B. Josh angelo", "C. Josh angelo agrazada", "D. IDK"],
           ["A. Yes", "B. Nah", "C. Probably", "D. Sometimes"]]

new_game()

while play_again():
    new_game()

print("Byeeeeeeeee!")