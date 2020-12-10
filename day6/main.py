import re

with open('input.txt', 'r') as f:
    input = f.read().split('\n\n')

def to_set(answers):
    return set(answers.replace('\n', ''))

count_of_yes_questions = [len(to_set(answers)) for answers in input]

print(sum(count_of_yes_questions))
