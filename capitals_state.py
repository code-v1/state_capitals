import random
states = [
    {
        "name": "Alabama",
        "capital": "Montgomery",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Alaska",
        "capital": "Juneau",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Arizona",
        "capital": "Phoenix",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Arkansas",
        "capital": "Little Rock",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "California",
        "capital": "Sacramento",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Colorado",
        "capital": "Denver",
        "correct": 0,
        "incorrect": 0
    }
]

# We will need to make a loop through the states. 
# We need to tally the scores. 
#Create play again option. 
# add corrrect and incorrect keys for each of the dictionaries
# need a get random feature.
# if counter equals 50 we have code to reset the game.

print('Welcome, do you want to play a game?')
random.shuffle(states) 
print(states[0]["name"])


correct_answer = 0
wrong_answer = 0
index = 0

# def tally_score(state):
    return 

while index <= len(states):
    if index == len(states):
        ask = input('Continue? Yes/No: ')
        if ask == "Yes":
            correct_answer = 0
            wrong_answer = 0
            index = 0 
            random.shuffle(states)
            states.insert(0, )
        else:
            break
    print(f'Correct Answer: {correct_answer} | Wrong Answer {wrong_answer}')
    print(f'Guess the capital of this state {states[index]["name"]}')
    user_guess = input('Input the correct capital for the state listed: ')
    if user_guess == states[index]["capital"]:
        print("You got that right!")
        correct_answer += 1
        states[index]["correct"] += 1
        
    else:
        print("You're an idiot!")
        states[index]["incorrect"] += 1
        wrong_answer += 1
    index += 1
print(f'Correct Answer: {correct_answer} | Wrong Answer {wrong_answer}')