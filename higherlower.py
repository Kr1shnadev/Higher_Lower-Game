import random
from art import logo,versus,lose
from game_data import data

def acc_desc(account):
    name = account["name"]
    foll = account["followers"]
    country = account["country"]
    return (f"{name},From {country}")
def answer(guess,a_followers,b_followers):
    if (a_followers>b_followers):
        return guess=='a'
    else:
        return guess=='b'
score=0
loop=True
acc_b=random.choice(data)

while(loop):

    print(logo)

    print("Option A: ")
    acc_a=acc_b
    print(acc_desc(acc_a))

    print(versus)

    print("Option B:")
    acc_b=random.choice(data)
    print(acc_desc(acc_b))

    choice=input("Who has more followers in Instagram: ").lower()
    is_ans_crct= answer(choice,acc_a["followers"],acc_b["followers"])


    if is_ans_crct== True:
        print("\n" * 7)
        score+=1
        print(f"Correct answer!......Current score:{score}")
    else:
        print(lose)
        print("Your guess was wrong.....better luck next time")
        print(f"Final score:{score}")
        loop=False