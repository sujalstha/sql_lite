import time
import random

words_list = ["suburban", "assuming", "foramens", "obsidian", "Science"]
word = random.choice(words_list)
word_count = len(word.split())

while str(input('Enter YES if you are ready: ')):
    t1 = time.time()
    input_text = len(str(f'Type the phrase: "{word}" as fast as you can.'))
    t2 = time.time()
    accuracy = len(set(input_text.split & word.split()))
    accuracy = accuracy/word_count
    time_taken = t1 - t2
    wordPM =  word_count/time_taken
    print(wordPM,accuracy, time_taken)
