#Poker Texas Hold Em
#What hands can beat me if we play with one standard deck
#Aniket Mishra




user_hand_dict = {}
table_cards_dict = {}
l1 = []


user_hand1 = input("Enter the first card in your hand: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
user_hand2 = input("Enter the second card in your hand: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
l1.append(user_hand1)
l1.append(user_hand2)
table_cards_num = input("Enter how many cards there are on the table currently: ")
table_cards_num = int(table_cards_num)
if table_cards_num == 3:
	table_cards1 = input("Enter the first card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	table_cards2 = input("Enter the second card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	table_cards3 = input("Enter the third card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	l1.append(table_cards1)
	l1.append(table_cards2)
	l1.append(table_cards3)
elif table_cards_num == 4:
	table_cards1 = input("Enter the first card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	table_cards2 = input("Enter the second card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	table_cards3 = input("Enter the third card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	table_cards4 = input("Enter the fourth card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	l1.append(table_cards1)
	l1.append(table_cards2)
	l1.append(table_cards3)
	l1.append(table_cards4)
elif table_cards_num ==  5:
	table_cards1 = input("Enter the first card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	table_cards2 = input("Enter the second card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	table_cards3 = input("Enter the third card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	table_cards4 = input("Enter the fourth card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	table_cards5 = input("Enter the fifth card on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C)")
	l1.append(table_cards1)
	l1.append(table_cards2)
	l1.append(table_cards3)
	l1.append(table_cards4)
	l1.append(table_cards5)


one, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace = 0,0,0,0,0,0,0,0,0,0,0,0,0,0
heart, spade, club, diamond = 0,0,0,0



#user_hand_final = user_hand.split()
#table_cards_final = table_cards.split()

print(l1)


for i in l1:
	i = i.split(",")
	if i[0] in user_hand_dict:
		user_hand_dict[i[0]].append(i[1])
	else:
		user_hand_dict[i[0]] = [i[1]]
	

#Check if hand + table can make any power hands
for key, value in user_hand_dict.items():
	if len(user_hand_dict[key]) > 1:
		for i in value:
			if key == '1':
				one += 1
			elif key == '2':
				two += 1
			elif key == '3':
				three += 1
			elif key == '4':
				four += 1
			elif key == '5':
				five += 1
			elif key == '6':
				six += 1
			elif key == '7':
				seven += 1
			elif key == '8':
				eight += 1
			elif key == '9':
				nine += 1
			elif key == '10':
				ten += 1
			elif key == "J":
				jack += 1
			elif key == "Q":
				queen += 1
			elif key == "K":
				king += 1
			elif key == "A":
				print("here")
				ace += 1
			if value == "H":
				heart += 1
			elif value == "S":
				spade += 1
			elif value == "C":
				club += 1
			elif value == "D":
				diamond += 1
			else:
				pass
	else:
		if key == '1':
			one += 1
		elif key == '2':
			two += 1
		elif key == '3':
			three += 1
		elif key == '4':
			four += 1
		elif key == '5':
			five += 1
		elif key == '6':
			six += 1
		elif key == '7':
			seven += 1
		elif key == '8':
			eight += 1
		elif key == '9':
			nine += 1
		elif key == '10':
			ten += 1
		elif key == "J":
			jack += 1
		elif key == "Q":
			queen += 1
		elif key == "K":
			king += 1
		elif key == "A":
			ace += 1
		if value == "H":
			heart += 1
		elif value == "S":
			spade += 1
		elif value == "C":
			club += 1
		elif value == "D":
			diamond += 1
		else:
			pass

total_num = one + 2*two + 3*three + 4*four + 5*five + 6*six +7* seven + 8*eight + 9*nine + 10*ten + 11*jack + 12*queen + 13*king + 14*ace

print(ace)
if heart == 5 or spade == 5 or club == 5 or diamond == 5:
	if ten >= 1 and jack >= 1 and queen >= 1 and king >= 1 and ace >= 1:
		print("You have a royal flush!")
	elif total_num % 5 == 0:
		print("You have a straight flush!")
	else:
		print("You have a flush!")
if one == 4 or two == 4 or  three == 4 or  four == 4 or  five == 4 or  six == 4 or  seven == 4 or  eight == 4 or  nine == 4 or  ten == 4 or  jack == 4 or  queen == 4 or  king == 4 or ace == 4:
	print("You have four of a kind!")
if one == 3 or two == 3 or  three == 3 or  four == 3 or  five == 3 or  six == 3 or  seven == 3 or  eight == 3 or  nine == 3 or  ten == 3 or  jack == 3 or  queen == 3 or  king == 3 or ace == 3:
	if one == 2 or two == 2 or  three == 2 or  four == 2 or  five == 2 or  six == 2 or  seven == 2 or  eight == 2 or  nine == 2 or  ten == 2 or  jack == 2 or  queen == 2 or  king == 2 or ace == 2:
		print("You have a full house!")
	else:
		print("You have three of a kind!")


