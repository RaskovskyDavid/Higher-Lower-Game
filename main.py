from game_data import data
from art import logo, vs
from replit import clear
import random

score_right = 0
# generate random choice
def question(data_for_choose):
    follow_1 =random.choice(data_for_choose)
    follow_2 =random.choice(data_for_choose)
    return[follow_1, follow_2]
# generate the question 
def print_question(follow_1,follow_2):
    print(f"Compara A: {follow_1['name']}, {follow_1['description']}, from   {follow_1['country']} ")
    print(vs)
    print(f"Compara B: {follow_2['name']}, {follow_2['description']}, from   {follow_2['country']} ")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    return answer
#the logic
def logic(answer, follow_1,follow_2):
    if answer == 'A':
        if follow_1["follower_count"] > follow_2["follower_count"]:
            return True
        else:
            return False
    if answer == 'B':
        if follow_2["follower_count"] > follow_1["follower_count"]:
            return True
        else:
            return False
    return False        
def process_game(score_right):
    keep = True
    while keep:
        print(logo)
        print(f"Score: {score_right}")
        get_questions = question(data)
        user_answer = print_question(get_questions[0],get_questions[1])
        keep = logic(user_answer, get_questions[0],get_questions[1])
        if keep:
            score_right += 1
            clear()
        else:
            print(f"You loose Score: {score_right}")

process_game(score_right)
