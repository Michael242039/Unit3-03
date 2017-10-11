#Created by: Michael Taylor
#Created on:October 10, 2017
#Created for ICS3U
#This program is a rock paper scissors game

import ui
from numpy import random

def computer_assign_decision():
	computer_choice = random.randint(1,4)
	
	if computer_choice == 1:
		view['opponent_image'].image = ui.Image('rock.PNG')
		view['opponent_choice_label'].text = 'Your opponent chooses... ROCK'
		return('rock')
		
	elif computer_choice == 2:
		view['opponent_image'].image = ui.Image('paper.PNG')
		view['opponent_choice_label'].text = 'Your opponent chooses... PAPER'
		return('paper')
		
	elif computer_choice == 3:
		view['opponent_image'].image = ui.Image('scissors.PNG')
		view['opponent_choice_label'].text = 'Your opponent chooses... SCISSORS'
		return('scissors')
		
	else:
		view['opponent_choice_label'].text = 'BAD'
		return('bad')

def choice_touch_up_inside(sender):
	computer_choice = computer_assign_decision()
	
	if sender.title == "ROCK":
		#rock outcomes
		view['user_image'].image = ui.Image('rock.PNG')
		user_choice = 'rock'
	
	if sender.title == "PAPER":
		#paper outcomes
		view['user_image'].image = ui.Image('paper.PNG')
		user_choice = 'paper'
		
	if sender.title == "SCISSORS":
		#scissors outcomes
		view['user_image'].image = ui.Image('scissors.PNG')
		user_choice = 'scissors'
	
	view['outcome_label'].text = str(process_outcome(user_choice, computer_choice))

def process_outcome(user_choice, computer_choice):
	if user_choice == computer_choice:
		return('TIE')
		
	if user_choice == 'rock':
		if computer_choice == 'paper':
			return('YOU LOSE')
		elif computer_choice == 'scissors':
			return('YOU WIN')
		else:
			return('BAD')
			
	if user_choice == 'paper':
		if computer_choice == 'rock':
			return('YOU WIN')
		elif computer_choice == 'scissors':
			return('YOU LOSE')
		else:
			return('BAD')
			
	if user_choice == 'scissors':
		if computer_choice == 'rock':
			return('YOU LOSE')
		elif computer_choice == 'paper':
			return('YOU WIN')
		else:
			return('BAD')
		
		

view = ui.load_view()
view['background'].image = ui.Image("background.JPG")
view.present('sheet')
