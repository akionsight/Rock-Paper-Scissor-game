import random
import time
number = random.randint(1,3)

def play(number):
    print('rock')
    time.sleep(0.5)
    print('paper')
    time.sleep(0.5)
    print('scissor')
    time.sleep(0.5)
    if number == 1:
        print(f"\n\nROCK")
    if number == 2:
        print(f"\n\nPAPER")
    if number == 3:
        print(f"\n\nSCISSOR")

play(number)