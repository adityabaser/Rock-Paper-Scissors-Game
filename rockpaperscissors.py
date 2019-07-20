import random
while  True:
	user_choice = input("Enter a choice,\n 1.rock \n 2. paper \n 3.scissors:")
	if user_choice =="1":
		user_choice_name = "Rock"
	elif user_choice =="2":
		user_choice_name = "Paper"
	elif user_choice =="3":
		user_choice_name = "Scissors"
	print( "The user choice is", user_choice_name)
	print("Now it's computer's turn")
#We use the randint method of the random module
	comp_choice=random.randint(1,3)
	while comp_choice == user_choice:
		comp_choice = random.randint(1,3)
	if comp_choice == 1:
		comp_choice_name = "Rock"
	elif comp_choice ==2:
		comp_choice_name = "Paper"
	elif comp_choice == 3:
		comp_choice_name = "Scissors"
	print("The computer choice is", comp_choice_name)
	print(user_choice_name,"vs",comp_choice_name)
#Condition for winning
	if ((comp_choice ==1 and user_choice =="2") or (comp_choice == 2 and user_choice == "1")):
		print("Paper wins")
	elif ((comp_choice ==2 and user_choice =="3") or (comp_choice == 3 and user_choice == "2")):
		print("Scissors wins")
	elif ((comp_choice == 3 and user_choice == "1") or (comp_choice == 1 and user_choice == "3")):
		print("Rock wins")
	print("Do you want to play again?")
	ans = input("Enter Y/N:")
	if ans == "N":
		break
		

