#Poker Texas Hold Em
#What hands can beat me
#Aniket Mishra
user_hand_dict = {}


user_hand = input("Enter the cards in your hand: (Put the number value then the suit after and seperate each entry by a space) (Ex: AC or 4S)")
table_cards = input("Enter the cards on the table: (Put the number value then the suit after and seperate each entry by a space) (Ex: AC or 4S)")



user_hand_final = user_hand.split()

for i in user_hand_final:
	user_hand_dict[i[0]] = i[1]

#for i,j in user_hand_dict.items():
#	print(i)
#	print(j)