import os
import random

# Get the directory where the Python script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Join the script directory with 'Stories' to get the absolute path to the 'Stories' directory
directory = os.path.join(script_dir, 'Stories')

files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.startswith('story')]
random_file = random.choice(files)
random_file = os.path.join(directory, random_file)

with open(random_file, 'r') as f:
    story = f.read()

words = set() # Using set to avoid duplicates
start_of_word = -1
target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}
for word in words:
    answer = input("Enter a word for " + word + " : ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print("Here is your story:\n")
print(story)