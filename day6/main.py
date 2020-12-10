import re

with open('input.txt', 'r') as f:
    input = f.read().split('\n\n')

def to_set(answers):
    return set(answers.replace('\n', ''))

count_of_yes_questions = [len(to_set(answers)) for answers in input]

print(sum(count_of_yes_questions))

######## PART 2 ##########

input_split = [{'user_answers': answers.split('\n'), 'set_of_yes': to_set(answers)} for answers in input]

def exists(question, user_answer):
    return True if question in user_answer else False

def check_user_answers(answers):
    all_yes_count = 0
    for question in answers['set_of_yes']:
        if all(exists(question, user_answer) for user_answer in answers['user_answers'] if user_answer):
            all_yes_count = all_yes_count + 1
    return all_yes_count

count_of_yes_question_all_users = [check_user_answers(answers) for answers in input_split]

print(sum(count_of_yes_question_all_users))
