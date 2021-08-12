import time
import random

# running forever
while True:
    words = [i.rstrip() for i in open("words.txt").readlines()]
    # pick random word
    true_word = random.choice(words)
    # find the lenght of the word
    word_count = len(true_word.split())
    # start time
    t_start = time.time()
    # print word
    print(f'enter the word "{true_word}"\n')
    # input word
    input_text = str(input('enter the word: '))
    # stop time
    t_stop = time.time()
    # time taken var
    time_taken = abs(t_start - t_stop)
    # wpm var
    WPM = word_count / time_taken

    print("Your time was {%.2f} and your WPM was : {%.2f} \n" \
          % (time_taken, WPM))
