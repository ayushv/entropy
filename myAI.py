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


def mobility():
	init_space=0
	for i in xrange(N):
		j=0
		temp_space=0
		while (j<N):
			if (board[i][j]=='-'):
				if (j==N-1):
					init_space += temp_space+1
				temp_space += 1
				j = j+1
			else:
				if (j-1==temp_space):
					init_space += temp_space
				else:
					init_space += 2*temp_space
				temp_space=0
				j = j+1

	for j in xrange(N):
		i=0
		temp_space=0
		while (i<N):
			if (board[i][j]=='-'):
				if (i==N-1):
					init_space += temp_space+1
				temp_space += 1
				i=i+1
			else:
				if (i-1==temp_space):
					init_space += temp_space
				else:
					init_space += 2*temp_space
				temp_space=0
				i=i+1
	return init_space


def fastLongestPalindromes(seq):
    """
    Behaves identically to naiveLongestPalindrome (see below), but
    runs in linear time.
    """
    seqLen = len(seq)
    l = []
    i = 0
    palLen = 0
    # Loop invariant: seq[(i - palLen):i] is a palindrome.
    # Loop invariant: len(l) >= 2 * i - palLen. The code path that
    # increments palLen skips the l-filling inner-loop.
    # Loop invariant: len(l) < 2 * i + 1. Any code path that
    # increments i past seqLen - 1 exits the loop early and so skips
    # the l-filling inner loop.
    while i < seqLen:
        # First, see if we can extend the current palindrome.  Note
        # that the center of the palindrome remains fixed.
        if i > palLen and seq[i - palLen - 1] == seq[i]:
            palLen += 2
            i += 1
            continue

        # The current palindrome is as large as it gets, so we append
        # it.
        l.append(palLen)

        # Now to make further progress, we look for a smaller
        # palindrome sharing the right edge with the current
        # palindrome.  If we find one, we can try to expand it and see
        # where that takes us.  At the same time, we can fill the
        # values for l that we neglected during the loop above. We
        # make use of our knowledge of the length of the previous
        # palindrome (palLen) and the fact that the values of l for
        # positions on the right half of the palindrome are closely
        # related to the values of the corresponding positions on the
        # left half of the palindrome.

        # Traverse backwards starting from the second-to-last index up
        # to the edge of the last palindrome.
        s = len(l) - 2
        e = s - palLen
        for j in xrange(s, e, -1):
            # d is the value l[j] must have in order for the
            # palindrome centered there to share the left edge with
            # the last palindrome.  (Drawing it out is helpful to
            # understanding why the - 1 is there.)
            d = j - e - 1

            # We check to see if the palindrome at l[j] shares a left
            # edge with the last palindrome.  If so, the corresponding
            # palindrome on the right half must share the right edge
            # with the last palindrome, and so we have a new value for
            # palLen.
            if l[j] == d: # *
                palLen = d
                # We actually want to go to the beginning of the outer
                # loop, but Python doesn't have loop labels.  Instead,
                # we use an else block corresponding to the inner
                # loop, which gets executed only when the for loop
                # exits normally (i.e., not via break).
                break

            # Otherwise, we just copy the value over to the right
            # side.  We have to bound l[i] because palindromes on the
            # left side could extend past the left edge of the last
            # palindrome, whereas their counterparts won't extend past
            # the right edge.
            l.append(min(d, l[j]))
        else:
            # This code is executed in two cases: when the for loop
            # isn't taken at all (palLen == 0) or the inner loop was
            # unable to find a palindrome sharing the left edge with
            # the last palindrome.  In either case, we're free to
            # consider the palindrome centered at seq[i].
            palLen = 1
            i += 1

    # We know from the loop invariant that len(l) < 2 * seqLen + 1, so
    # we must fill in the remaining values of l.

    # Obviously, the last palindrome we're looking at can't grow any
    # more.
    l.append(palLen)

    # Traverse backwards starting from the second-to-last index up
    # until we get l to size 2 * seqLen + 1. We can deduce from the
    # loop invariants we have enough elements.
    lLen = len(l)
    s = lLen - 2
    e = s - (2 * seqLen + 1 - lLen)
    for i in xrange(s, e, -1):
        # The d here uses the same formula as the d in the inner loop
        # above.  (Computes distance to left edge of the last
        # palindrome.)
        d = i - e - 1
        # We bound l[i] with min for the same reason as in the inner
        # loop above.
        l.append(min(d, l[i]))
    sum=0
    for i in xrange(len(l)):
        if (l[i]!=1):
            sum=sum+l[i]
    return sum

def utility():
	board_score=0
	for x in xrange(N):
		temp_s=''
		y=0
		while (y<N):
			if (board[x][y]=='-'):
				board_score=board_score+fastLongestPalindromes(temp_s)
				temp_s=''
				y=y+1
			else:
				temp_s=temp_s+board[x][y]
				if (y==N-1):
					board_score=board_score+fastLongestPalindromes(temp_s)
				y=y+1

	for y in xrange(N):
		temp_s=''
		x=0
		while (x<N):
			if (board[x][y]=='-'):
				board_score=board_score+fastLongestPalindromes(temp_s)
				temp_s=''
				x=x+1
			else:
				temp_s=temp_s+board[x][y]
				if (x==N-1):
					board_score=board_score+fastLongestPalindromes(temp_s)
				x=x+1
	return board_score


def Expectiminimax_decision_chaos(Color):
	alpha=Inf_max
	(actionx,actiony)=(-1,-1)
	for x in xrange(N):
		for y in xrange(N):
			if board[x][y]=="-":
				board[x][y]=Color
				value=Expectiminimax_value(board,0,"max",Color,Inf_min,Inf_max,0)
				alpha=min(alpha,value)
				if(alpha==value):
					(actionx,actiony)=(x,y)
				board[x][y]="-"

	return (actionx,actiony)

def Expectiminimax_decision_order():
	al=Inf_min;
	be=Inf_max;
	beta=Inf_min
	max_move=(0,0,0,0)
	Ordermoves=Omoveshelper(board)
	for move in Ordermoves:
		(a,b,c,d)=move
		board[c][d] = board[a][b]
		board[a][b] = '-'
		value=Expectiminimax_value(board,0,"chance",'A',al,be,1)
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

def scoreHelp(row):
	MAX = len(row)
	isOk = lambda x: True if x >= 0 and x < MAX and row[x] != '-' else False
	score = 0 
	for ind in range(1, MAX):
		# epicenter b/w ind-1 and ind
		length = 0
		scoreX = 0
		right = ind
		left = ind - 1
		while isOk(right) and isOk(left) and row[left] == row[right]:
			scoreX += (length+2); length += 2; right += 1; left -= 1
		score += scoreX
		
		# epicenter at ind
		length = 1 
		scoreX = 0
		right = ind + 1
		left = ind - 1
		while isOk(right) and isOk(left) and row[left] == row[right]:
			scoreX += (length + 2); length += 2; right += 1; left -= 1
		score += scoreX
	return score

def calculateScore():
	
	score = 0
	for rowList in board:
		score += scoreHelp(rowList)
	
	for col in range(0, N):
		colList = []
		for row in range(0, N):
			colList.append(board[row][col])
		score += scoreHelp(colList)
	
	return score



def Expectiminimax_value(board,depth,player,Color,alp,bet,switch):
	cutoff=3
	ordercoff=0.3
	if(depth==cutoff):
		if(switch==1):
			return utility()+ordercoff*mobility()
		else:
			return utility()
	else:
		if(player=="max"):
			v=Inf_min
			Ordermoves=Omoveshelper(board)
			for move in Ordermoves:
				(a,b,c,d)=move
				board[c][d] = board[a][b]
				board[a][b] = '-'
				v=max(v, Expectiminimax_value(board,depth+1,"chance",Color,alp,bet,switch))
				alp=max(alp,v)
				board[a][b] = board[c][d]
				board[c][d] = '-'
				if (bet<=alp):
					break
			return v

		elif(player=="chance"):
			mycolor=['A','B','C','D','E','-']
			chance_sum=0
			Prob=0.2
			for char in mycolor:
				chance_sum=chance_sum+Prob*Expectiminimax_value(board,depth+1,"min",char,alp,bet,switch)
			return chance_sum
		
		elif(player=="min"):
			v=Inf_max
			for x in xrange(N):
				for y in xrange(N):
					if board[x][y]=="-":
						board[x][y]=Color
						v=min(v,Expectiminimax_value(board,depth+1,"max",Color,alp,bet,switch))
						bet=min(bet,v)
						board[x][y]="-"
						if (bet<=alp):
							break
			return v

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



