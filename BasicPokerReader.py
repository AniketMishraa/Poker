#Poker Texas Hold Em
#What hands can beat me if we play with one standard deck
#Aniket Mishra
user_hand_dict = {}
table_cards_dict = {}

user_hand = input("Enter the cards in your hand: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C 10,S)")
table_cards = input("Enter the cards on the table: (Put the number value then a comma then the suit after and seperate each entry by a space) (Ex: A,C 10,S 4,D)")

one, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace = 0,0,0,0,0,0,0,0,0,0,0,0,0,0
heart, spade, club, diamond = 0,0,0,0



user_hand_final = user_hand.split()
table_cards_final = table_cards.split()


for i in user_hand_final:
	i = i.split(",")
	user_hand_dict[i[0]] = i[1]

for i in table_cards_final:
	i = i.split(",")
	table_cards_dict[i[0]] = i[1]




#Check if hand + table can make any power hands
for key, value in user_hand_dict.items():
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
	else:
		pass
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
for key, value in table_cards_dict.items():
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
	else:
		pass
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


if heart == 5 or spade == 5 or club == 5 or diamond == 5:
	if ten >= 1 and jack >= 1 and queen >= 1 and king >= 1 and ace >= 1:
		print("You have a royal flush!")
	elif total_num % 5 == 0:
		print("You have a straight flush!")
	else:
		print("You have a flush!")

