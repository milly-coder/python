import random

# Define the Quiz Data using a dictionary
# for every keys in the dictionary holds the questions and the values holds the answers
quiz = {
    "question1": {"question": "What is the capital of France?", "answer": "Paris"},
    "question2": {"question": "What is the capital of Germany?", "answer": "Berlin"},
    "question3": {"question": "What is the capital of Italy?", "answer": "Rome"},
    "question4": {"question": "What is the capital of Spain?", "answer": "Madrid"},
    "question5": {"question": "What is the capital of Portugal?", "answer": "Lisbon"},
    "question6": {"question": "What is the capital of Switzerland?", "answer": "Bern"},
    "question7": {"question": "What is the capital of Austria?", "answer": "Vienna"},
}
# this prompt user for answers to the questions asked.
def ask_question(question_data):
    user_answer = input(question_data['question'] + " ").capitalize()
    if user_answer == question_data['answer']:
        print("Correct!")
        return True
    else:
    # print correct answer if answer is wrong.
        print(f"Wrong! The correct answer is {question_data['answer']}.")
        return False
    
"""Runs the entire quiz, asking each question in random order and calculating the score.
using radomization to shuffle the questions or keys to make it more engaging and
unpredictable. and also loop through or iterate over the keys or question"""

def Start_quiz(quiz):
    total_score = 0       # initialized score to 0. 
    shuffled_questions = list(quiz.keys()) 
    random.shuffle(shuffled_questions)      
    for key in shuffled_questions:          
        if ask_question(quiz[key]):
             total_score += 1    # add 1 if the answer is correct
    return total_score

def display_final_score(total_score, total_questions):
#Displays the final results to the user.
    percentage = (total_score / total_questions) * 100
    print(f"You answered {total_score} questions correctly out of {total_questions}.")
    print(f"Your final score is: {percentage:.2f}%")

# Run the quiz
total_score= Start_quiz(quiz)

# Show the results
display_final_score(total_score, len(quiz))