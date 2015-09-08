# myAI.py
import sys
from random import random, choice

def printX(*message):
	for msg in message:
		sys.stderr.write(repr(msg) + ' ') 
	sys.stderr.write('\n') 

N = int(raw_input())
ROLE = raw_input()
board = []
avail_colors=N*N
num_colors=[]

for i in xrange(N):
	num_colors.append(N)



for i in range(0, N):
	boardRow = []
	for j in range(0, N):
		boardRow.append('-')
	board.append(boardRow)

def isGameOver():
	for i in range(0, N):
		for j in range(0, N):
			if (board[i][j] == '-'):
				return False
	return True


## --------------------


Inf_min=-100
Inf_max=100

def prob(colour):
	if (colour=='-'):
		return 0
	index = ord(colour) - ord('A')
	return num_colors[index]/avail_colors


def getPossibleOrderMoves(x, y):
	possibleMoves = []

	for iterator in range(x-1,-1,-1):
		if board[iterator][y]=='-':
			possibleMoves.append((iterator,y))
		else:
			break

	for iterator in range(y-1,-1,-1):
		if board[x][iterator]=='-':
			possibleMoves.append((x,iterator))
		else:
			break

	for iterator in range(x+1,N):
		if board[iterator][y]=='-':
			possibleMoves.append((iterator,y))
		else:
			break

	for iterator in range(y+1,N):
		if board[x][iterator]=='-':
			possibleMoves.append((x,iterator))
		else:
			break

	return possibleMoves

def getPossibleOrderMoves(x, y):
	possibleMoves = []

	for iterator in range(x-1,-1,-1):
		if board[iterator][y]=='-':
			possibleMoves.append((iterator,y))
		else:
			break

	for iterator in range(y-1,-1,-1):
		if board[x][iterator]=='-':
			possibleMoves.append((x,iterator))
		else:
			break

	for iterator in range(x+1,N):
		if board[iterator][y]=='-':
			possibleMoves.append((iterator,y))
		else:
			break

	for iterator in range(y+1,N):
		if board[x][iterator]=='-':
			possibleMoves.append((x,iterator))
		else:
			break

	return possibleMoves

def Expectiminimax_decision_chaos( Color):
	alpha=100
	global avail_colors
	avail_colors -= 1
	index = ord(Color) - ord('A')
	num_colors[index] -= 1

	(actionx,actiony)=(-1,-1)
	for x in xrange(N):
		for y in xrange(N):
			if board[x][y]=="-":
				board[x][y]=Color
				value=Expectiminimax_value(board,0,"max",Color)
				alpha=min(alpha,value)
				if(alpha==value):
					(actionx,actiony)=(x,y)
				board[x][y]="-"

	return (actionx,actiony)


def Expectiminimax_decision_order():
	beta=Inf_min
	max_move=(0,0,0,0)
	Ordermoves=Omoveshelper(board)
	for move in Ordermoves:
		(a,b,c,d)=move
		board[c][d] = board[a][b]
		board[a][b] = '-'
		value=Expectiminimax_value(board,0,"chance",'A')
		beta=max(beta,value)
		if(value==beta):
			max_move=move
		board[a][b] = board[c][d]
		board[c][d] = '-'
		
	return max_move


def Omoveshelper(board):
	capturedSquares=[]
	for x in xrange(N):
		for y in xrange(N):
			if board[x][y]!="-":
				capturedSquares.append((x,y,board[x][y]))

	capturedSquares = sorted(capturedSquares, key=lambda t:(t[0],t[1]))
	i=0
	ans=[]
	while(i<len(capturedSquares)):
		fromPosition = capturedSquares[i]
		i=i+1
		possibleMoves = getPossibleOrderMoves(fromPosition[0], fromPosition[1])
		if len(possibleMoves)!=0:
			j=0
			while(j<len(possibleMoves)):
				mv =possibleMoves[j]
				j+=1
				ans.append((fromPosition[0], fromPosition[1], mv[0], mv[1]))
				

	return ans

def evaluation(){
	
	
}




def Expectiminimax_value(board,depth,player,Color):
	cutoff=3
	if(depth==cutoff):
<<<<<<< HEAD
		return 1
=======
		a=[1,2,3,4,5]
		return choice(a)
>>>>>>> 090fbe66ff1103ccdb273ee873447981e631dbfa
	else:
		if(player=="max"):
			beta=Inf_min
			Ordermoves=Omoveshelper(board)
			for move in Ordermoves:
				(a,b,c,d)=move
				board[c][d] = board[a][b]
				board[a][b] = '-'
				beta=max(beta, Expectiminimax_value(board,depth+1,"chance",Color))
				board[a][b] = board[c][d]
				board[c][d] = '-'
			return beta

		elif(player=="chance"):
			mycolor=['A','B','C','D','E','-']
			chance_sum=0
			Prob=0.2
			for char in mycolor:
				chance_sum=chance_sum+Prob*Expectiminimax_value(board,depth+1,"min",char)
			return chance_sum
		
		elif(player=="min"):
			alpha=Inf_max
			for x in xrange(N):
				for y in xrange(N):
					if board[x][y]=="-":
						board[x][y]=Color
						alpha=min(alpha,Expectiminimax_value(board,depth+1,"max",Color))
						board[x][y]="-"
			return alpha

#returns x,y for next piece 
def chaosAI(piece):
	openSquares=[]
	for x in xrange(N):
		for y in xrange(N):
			if board[x][y]=="-":
				openSquares.append((x,y))
	openSquares
	return choice(openSquares)

#returns a,b,c,d -> move a,b piece to c,d : abhi random hai , isko machana h. 
def orderAI():
	capturedSquares=[]
	for x in xrange(N):
		for y in xrange(N):
			if board[x][y]!="-":
				capturedSquares.append((x,y,board[x][y]))

	capturedSquares = sorted(capturedSquares, key=lambda t:(t[0],t[1]))

	while(True):
		fromPosition = choice(capturedSquares)
		possibleMoves = getPossibleOrderMoves(fromPosition[0], fromPosition[1])
		if len(possibleMoves)!=0:
			mv = choice(possibleMoves)
			ans = (fromPosition[0], fromPosition[1], mv[0], mv[1])
			break

	return ans


## --------------------
import os, sys
sys.path.insert(0, os.path.realpath('../utils'))
from log import *
import minimax
COLORS = [bcolors.OKRED, bcolors.OKCYAN, bcolors.OKGREEN, bcolors.OKBLUE, bcolors.OKYELLOW, bcolors.OKWHITE]
TEXTCONV = {'A': 'R', 'B': 'C', 'C': 'G','D':'B', 'E':'Y', '-':'-'}
def color(tile): # character
	index = ord(tile) - ord('A')
	if (tile == '-'):
		index = 5
	return COLORS[index] + TEXTCONV[tile] + bcolors.ENDC

def printBoard():
	for x in xrange(N):
		print >>sys.stderr,  "".join( list( map( lambda x: color(x), board[x] ) ) )
	print >>sys.stderr, '\n'


# returns if the move was successful or not
def makeChaosMove(x, y, color):
	global board
	if (board[x][y] != '-'):
		return False
	board[x][y] = color 
	return True
	
# returns if the move was successful or not
def makeOrderMove(a, b, c, d):
	global board	
	board[c][d] = board[a][b]
	board[a][b] = '-'
	return True

def playAsOrder():
	global board
	printX('ORDER')
	while True:
		printBoard()
		line = raw_input()
		# printX ('LINE:', line)
		(x, y, color) = line.split(' ')
		(x, y) = (int(x), int(y))
		board[x][y] = color
		if (isGameOver()):
			return
	
		(a, b, c, d) = Expectiminimax_decision_order()
		makeOrderMove(a, b , c, d)
		printBoard()
		print '%d %d %d %d' % (a, b, c, d)
		sys.stdout.flush()

	
def playAsChaos():
	global board
	printX('CHAOS')
	color = raw_input()
	(x, y) = Expectiminimax_decision_chaos(color)
	board[x][y] = color
	print '%d %d' %(x, y)
	printBoard()

	while True:
		if (isGameOver()):
			return

		his_move = raw_input()
		# printX ('his move: %s'%his_move)
		(a, b, c, d) = map(lambda x: int(x), his_move.split(' '))
		makeOrderMove(a, b, c, d)
		color = raw_input()
		(x, y) = Expectiminimax_decision_chaos(color)
		board[x][y] = color
		printBoard()
		print '%d %d' %(x, y)
			

if (ROLE == 'ORDER'):
	playAsOrder()
elif(ROLE == 'CHAOS'):
	playAsChaos()
else:
	print >> sys.stderr, 'I am not intelligent for this role: %s' %ROLE
	
printX ('--graceful exit by myAI--')



