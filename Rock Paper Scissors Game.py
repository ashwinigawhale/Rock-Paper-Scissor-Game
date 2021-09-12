#Rock Paper Scissor Game

import random
print("Rules of the game:\n"
+"Rock v/s paper ->paper wins\n"
+"Ppaer v/s Scissor ->Scissor wins\n"
+"Rock v/s Scissor -> Rock wins\n")

while "True":
    print("Choose from the list\n 1.Rock\n 2. Ppaper\n 3. Scissor\n")
    choice = int(input("Enter the no.\n"))
    while choice>3 or choice<1:
        print("Enter the valid no.\n")
    
    if choice==1:
        choice_name='Rock'
    elif choice==2:
        choice_name='Paper'
    else:
        choice_name='Scissor'
    
    print("Your choice\n"+ choice_name)
    print("Now its computer turn\n")

    comp_choice= random.randint(1,3)

    while comp_choice==choice:
        comp_choice=random.randint(1,3)
    
    if comp_choice==1:
        comp_choice='Rock'
    elif comp_choice==2:
        comp_choice='Paper'
    else:
        comp_choice='Scissor'

    print("computer choice is\n"+ comp_choice)

    if ((choice==1 and comp_choice==2)or(choice==2 and comp_choice== 1)):
        print("Paper wins\n", end="")
        result="Paper"
    elif ((choice==1 and comp_choice==3)or (choice==3 and choice==1)):
        print("Rock wins\n",end="")
        result="Rock"
    else:
        print("Scissor wins\n", end="")
        result="Scissor"

    if result== choice_name:
        print("User wins\n")
    else:
        print("Computer wins\n")

    
