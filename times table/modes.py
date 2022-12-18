import random
import os

times_table = input("Enter the times table you want to be tested on: ")
q_amount = input("Enter the amount of questions you want: ")
mode = input("Enter mode (easy, medium, hard): ")

def tt(times_table, q_amount,mode):
    correct = 0
    incorrect = 0 
    
    for i in range(int(q_amount)):
        os.system("title Correct - {} Incorrect - {}".format(correct,incorrect))
        if mode.lower() == "easy":
            num = random.randint(2,10)
        elif mode.lower() == "medium":
            num = random.randint(5,15)
        elif mode.lower() == "hard":
            num = random.randint(11,20)
        answer = int(times_table) * num
        user = input("{} x {} = ".format(num,times_table))
        if user:
            if int(user) == answer:
                print("Correct! Editing score...")
                correct+=1
            else:
                print("Incorrect.")
                incorrect+=1
        else:
            print("No answer entered, skipping.")


tt(times_table,q_amount,mode)