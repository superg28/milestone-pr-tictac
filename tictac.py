#!/usr/bin/env python
'''
This is the first milestone project for the Complete Python3 Bootcamp

	TIC TAC TOE

Started using VSCode today - 2018-11-09
'''
import random

def clear():
	print('\n'*100)

def display_board(board, cl=False):
	'''
	Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
	'''
	if cl:
		clear()
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-|-|-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-|-|-')
	print(board[1] + '|' + board[2] + '|' + board[3])
	print('\n')

test_board = ['#', 'O', ' ', 'X', 'X', 'O', ' ', 'O', ' ', ' ']

# display_board(test_board) # TEST

def player_input():
	'''
	Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
	'''
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('Player 1, choose X or O: ')
	        
	p1_mark = marker
	   
	if p1_mark == 'X':
		p2_mark = 'O'
	else:
		p2_mark = 'X'
	        
	return (p1_mark, p2_mark)

# p1, p2 = player_input() # TESTING

def win_check(board, mark):
	'''
	Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won
	'''

	# Check diagonals
	if board[5] == mark:
		if (board[1] == mark and board[9] == mark) or (board[3] == mark and board[7] == mark):
			return True
		elif (board[2] == mark and board[8] == mark) or (board[4] == mark and board[6] == mark):
			return True
		else:
			return False
	# Check vert and horiz
	elif board[1] == mark and board[3] == mark and board[2] == mark:
		return True
	elif board[1] == mark and board[7] == mark and board[4] == mark:
		return True
	elif board[7] == mark and board[8] == mark and board[9] == mark:
		return True
	elif board[3] == mark and board[6] == mark and board[9] == mark:
		return True
	else:
		return False
	pass

# print('win_check {}'.format(win_check(test_board,p1))) # TESTING

def place_marker(board, marker, position):
	'''
	Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
	'''
	board[position] = marker
	return board

# place_marker(test_board,p1,1) # TESTING
# place_marker(test_board,p2,5) # TESTING
# display_board(test_board) # TESTING

def choose_first():
	'''
	Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
	'''
	num = random.randint(1,30)
	if num % 2 == 0:
		return 'p2'
	else:
		return 'p1'

# print(choose_first())

def space_check(board, position):
	'''
	Write a function that returns a boolean indicating whether a space on the board is freely available
	'''
	space = False
	if board[position] == ' ':
		space = True
	return space
	pass

# print(space_check(test_board, 1))
# print(space_check(test_board, 8))

def full_board_check(board):
	'''
	Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
	'''
	if ' ' in board:
		is_full = False
	else:
		is_full = True
	return is_full

# print(full_board_check(test_board))

def player_choice(board):
	'''
	Write a function that asks for a player's next position (as a number 1-9) and then uses the function space_check to check if it's a free position. If it is, then return the position for later use.
	'''
	position = 0
	while not position in range(1,10):
		position = int(input('Pick a spot(1-9): '))
	
	if space_check(board,position):
		return position
	else:
		print('That spot is taken, try again')
		player_choice(board)

# player_choice(test_board)

def replay():
	'''
	Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
	'''
	replay = ''
	while replay != 'Y' and replay != 'N':
		replay = input('Want to play again? Y or N: ')

	if replay == 'Y':
		return True
	else:
		return False

#replay() # TESTING


# Game starts below

print('Welcome to Tic Tac Toe!')

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

while True:
	# Set the game up here
	p1, p2 = player_input()
	clear()
	who = choose_first()
    
	if who =='p1':
		turn = True
	else:
		turn = False

	game_on = True

	while game_on:
		# print(board)
		if turn:
			print('Player1\'s Turn\n')
			mark = player_choice(board)
			board = place_marker(board,p1,mark)
			if win_check(board,p1):
				print('Player1 Wins!!!')
				display_board(board)
				break
			display_board(board, True)
			turn = False
		# Player2's turn.
		else:
			print('Player2\'s Turn\n')
			mark = player_choice(board)
			board = place_marker(board,p2,mark)
			if win_check(board,p2):
				print('Player2 Wins!!!')
				display_board(board)
				break
			display_board(board, True)
			turn = True
		game_on = not full_board_check(board)
	
	if not replay():
		break
	else:
		board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']