#!/usr/bin/env python
'''
This is the first milestone project for the Complete Python3 Bootcamp

	TIC TAC TOE

'''
import random

def display_board(board):
	'''
	Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
	'''
	print('\n'*100)
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-|-|-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-|-|-')
	print(board[1] + '|' + board[2] + '|' + board[3])

test_board = ['#','X','O','X','X','X','O','X','O','X']

display_board(test_board)

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

p1, p2 = player_input()


def place_marker(board, marker, position):
	'''
	Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
	'''
	pass

def choose_first():
	'''
	Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
	'''
	pass

def space_check(board, position):
	'''
	Write a function that returns a boolean indicating whether a space on the board is freely available
	'''
	pass

def full_board_check(board):
	'''
	Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
	'''
	pass

def player_choice(board):
	'''
	Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
	'''
	pass

def replay():
	'''
	Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
	'''

# Game starts below

print('Welcome to Tic Tac Toe!')

#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break