import random
import os
cards = [[1,2,3,4,5,6,7,8,9,10,10,10,11],
        [1,2,3,4,5,6,7,8,9,10,10,10,11],
        [1,2,3,4,5,6,7,8,9,10,10,10,11],
        [1,2,3,4,5,6,7,8,9,10,10,10,11]]

acount = 5000
count1 = 0
count2 = 0
player1 = []
player2 = []
player = 0
for i in range(4):
  row = random.randint(0,3)
  column = random.randint(0,11)
  if row == 0:
    type = "heart"
  elif row == 1:
    type = "spades"
  elif row == 2:
    type = "clubs"
  elif row == 3:
    type = "diamonds"
  
  if column == 9:
    value = "jack"
  elif column == 10:
    value = "Queen"
  elif column == 11:
    value = "king"
  elif column == 12:
    value = "Ace"
  else:
    value = str(cards[row][column])
  if player%2 ==0 :
    player1.append(value)
    player1.append(type)
    count1 = count1 + int(cards[row][column])
  if player%2 != 0:
    player2.append(value)
    player2.append(type)
    count2 = count2 + int(cards[row][column])
  player = player + 1
print("--------Player1--------")
print("Player 1 starts with" , player1)
print("Player 2 starts with" , player2)
print("Player 1's current total is" , count1)
choice1 = input("Player 1: Hit or Stand: ")
while choice1 == "Hit":
  row = random.randint(0,3)
  column = random.randint(0,11)
  if row == 0:
    type = "heart"
  elif row == 1:
    type = "spades"
  elif row == 2:
    type = "clubs"
  elif row == 3:
    type = "diamonds"
  
  if column == 9:
    value = "jack"
  elif column == 10:
    value = "Queen"
  elif column == 11:
    value = "king"
  elif column == 12:
    value = "Ace"
  else:
    value = str(cards[row][column])
  count1 = count1 + int(cards[row][column])
  print("You pulled a" , value , "of" , type)
  if count1 >21:
    print("Your total is" , count1)
    choice1 = "S"
    print("You have gone bust")
  elif count1 == 21:
    print("Player 1 has reached 21")
    choice1 = "S"
  elif count1< 21:
    print("Your total is" , count1)
    choice1 = input("Hit or Stand?: ")

cho = input("Would you like to swap to player 2?: ")
os.system('clear')

print("--------Player2--------")
print("Player 1 starts with" , player1)
print("Player 2 starts with" , player2)
print("Player 2's current total is" , count2)
choice2 = input("Player 2: Hit or Stand: ")
while choice2 == "Hit":
  row = random.randint(0,3)
  column = random.randint(0,11)
  if row == 0:
    type = "heart"
  elif row == 1:
    type = "spades"
  elif row == 2:
    type = "clubs"
  elif row == 3:
    type = "diamonds"
  
  if column == 9:
    value = "jack"
  elif column == 10:
    value = "Queen"
  elif column == 11:
    value = "king"
  elif column == 12:
    value = "Ace"
  else:
    value = str(cards[row][column])
  count2 = count2 + int(cards[row][column])
  print("You pulled a" , value , "of" , type)
  if count2 >21:
    print("Your total is" , count2)
    choice2 = "S"
    print("You have gone bust")
  elif count2 == 21:
    print("Player 2 has reached 21")
    choice2 = "S"
  elif count2< 21:
    print("Your total is" , count2)
    choice2 = input("Hit or Stand?: ")

print("--------FINAL--------")

print("Player 1's total is" , count1)
print("Player 2's total is" , count2)
if count1 > count2 :
  if count1 <22: 
    print("Player 1 Won")
if count2 > count1:
  if count2< 22:
    print("Player 2 Won")
if count1== count2:
  print("Push")
if count1>21 and count2>21:
  print("Double bust")
