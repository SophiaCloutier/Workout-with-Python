

# imports the voice
import pyttsx3
# import the time module
import time
# import the random number generator
import random
from random import seed
from random import randint




# initialize Text-to-speech engine
engine = pyttsx3.init()
# get details of all voices available
voices = engine.getProperty("voices")
# set another voice
engine.setProperty("voice", voices[1].id)


# variables/lists

exercises_list = []
duration_list = []
rest_time = []
motivation_phrases = ["You're doing great!", "Feel the burn!", "You look great", "I feel awesome, What about you?", "No pain, no gain", "You can do it!", "Do your best and forget the rest", "You are a winner!", "Feeling good!", "Suck it up butter-cup"]



def one_exercise(exercise_name, duration, rest):
    print(exercise_name.upper())
    exercise_text = exercise_name, 'for', str(duration), 'seconds'
    engine.say(exercise_text)
    engine.runAndWait()
    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        if duration == 5:
            engine.say('5 seconds left')
            rando_phrase = randint(0, len(motivation_phrases)-1)
            engine.say(motivation_phrases[rando_phrase])
            engine.runAndWait()
        duration -= 1
    engine.say("Great job! Now you rest.")
    engine.runAndWait()
    print('')
    while rest:
        mins, secs = divmod(rest, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        rest -= 1
    print('')


workout_choice = 'x'

while workout_choice != 'y' and workout_choice != 'n' and workout_choice != 'd':
    workout_choice = input("Press 'y' for a pre-made workout, press 'n' to customize your workout, press 'd' for a fast product demo: ")

if workout_choice == 'n':
    exercises_inp = input("Enter your exercise or type 'done': ")
    exercise_duration = int(input("For how long(seconds): "))
    rest_duration = int(input("With how much rest(seconds): "))
    while exercises_inp != 'done':
        exercises_list.append(exercises_inp)
        duration_list.append(exercise_duration)
        rest_time.append(rest_duration)
        exercises_inp = input("Enter your exercise or type 'done': ")
        if exercises_inp != 'done':
            exercise_duration = int(input("For how long(seconds): "))
            rest_duration = int(input("With how much rest(seconds): "))
        else:
            num_rounds = int(input("How many rounds do you want to do: "))
            print('')
elif workout_choice == 'y':
    exercises_list = ['Flutter kicks', 'Hold the world', 'Squats', 'Plank', 'Leg lifts', 'Mason twist', 'Push ups', 'Suitcases', 'Lunges', 'Burpies', 'Sit-up get-ups']
    duration_list = [40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]
    rest_time = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    num_rounds = 2
elif workout_choice == 'd':
    exercises_list = ['Flutter kicks', 'Hold the world', 'Squats', 'Plank']
    duration_list = [6, 6, 6, 6]
    rest_time = [2, 2, 2, 2]
    num_rounds = 1

print("Workout")
print(num_rounds, 'x')
for entry in range(len(exercises_list)):
    print(exercises_list[entry], duration_list[entry], 'second(s) on', rest_time[entry], 'second(s) rest')
print('')

engine.say("Let's get started!")
engine.runAndWait()

while num_rounds:
    for position in range(len(exercises_list)):
        one_exercise(exercises_list[position], duration_list[position], rest_time[position])
    num_rounds -= 1


print("Workout complete! You're one step closer to achieving your goals and dreams!")
engine.say("Workout complete! You're one step closer to achieving your goals and dreams!")
engine.runAndWait()


