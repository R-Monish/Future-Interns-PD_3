import random

user_choice= int(input('what do you choose type 0 for Rock,1 for paper, 2 for Scissors :'))
print(user_choice)

computer_choice=random.randint(0,2)
print('computer_choice')
print(computer_choice)

if user_choice>=3 or user_choice<0:
    print('Ypur type an invalid number.You Lose!')
elif user_choice==0 and computer_choice==2:
    print('You Win!')
elif computer_choice==0 and user_choice==2:
    print('You Lose!')
elif computer_choice>user_choice:
    print('You Lose!')
elif user_choice>computer_choice:
    print('You Win!')
elif computer_choice==user_choice:
    print("It's a Draw!")

