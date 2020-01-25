import math
import copy


jumps = []

def dfs(state,position, visited,color):
	global jumps
	if len(position) > 1:
		#print(position)
		initial_pos_black = [[0,0], [0,1], [0,2], [0,3], [0,4], [1,0], [1,1], [1,2], [1,3], [1,4], [2,0], [2,1], [2,2], [2,3], [3,0], [3,1], [3,2], [4,0], [4,1]]
		initial_pos_white = [[11,15], [11,14], [12,15], [12,14], [12,13], [13,15], [13,14], [13,13], [13,12], [14,15], [14,14], [14,13], [14,12], [14,11], [15,15], [15,14], [15,13], [15,12], [15,11]]
		
		if color == 'B':
			if position[0] in initial_pos_black:
				if position[-1][0] >= position[0][0] and position[-1][1] >= position[0][1]:
					jumps.append(position)
			if position[0] in initial_pos_black and position[-1] not in initial_pos_black:
				jumps.append(position)
			if position[0] not in initial_pos_black and position[-1] not in initial_pos_black:
				jumps.append(position)
			if position[0] in initial_pos_white and position[-1] in initial_pos_white:
				jumps.append(position)
		
		if color == 'W':
			if position[0] in initial_pos_white:
				if position[-1][0] <= position[0][0] and position[-1][1] <= position[0][1]:
					jumps.append(position)
			if position[0] in initial_pos_white and position[-1] not in initial_pos_white:
				jumps.append(position)
			if position[0] not in initial_pos_white and position[-1] not in initial_pos_white:
				jumps.append(position)
			if position[0] in initial_pos_black and position[-1] in initial_pos_black:
				jumps.append(position)

	#if len(position) > 1:
		#print(position[-1][0])
	p = copy.deepcopy(position)
	last = p[-1]
	x = last[0]
	y = last[1]
	visited[x][y] = True

	if x-1 >= 0 and x-1 < 16 and y-1 >=0 and y-1 < 16 and x-2 >= 0 and x-2 < 16 and y-2 >=0 and y-2 < 16 and state[x-1][y-1] != '.' and state[x-2][y-2] == '.' and not visited[x-2][y-2]:
		p = copy.deepcopy(position)
		p.append([x-2,y-2])
		dfs(state,p,visited,color)
	if x-1 >= 0 and x-1 < 16 and x-2 >= 0 and x-2 < 16 and state[x-1][y] != '.' and state[x-2][y] == '.' and not visited[x-2][y]:
		p = copy.deepcopy(position)
		p.append([x-2,y])
		dfs(state,p,visited,color)
	if x-1 >= 0 and x-1 < 16 and y+1 >=0 and y+1 < 16 and x-2 >= 0 and x-2 < 16 and y+2 >=0 and y+2 < 16 and state[x-1][y+1] != '.' and state[x-2][y+2] == '.' and not visited[x-2][y+2]:
		p = copy.deepcopy(position)
		p.append([x-2,y+2])
		dfs(state,p,visited,color)
	if y-1 >=0 and y-1 < 16 and y-2 >=0 and y-2 < 16 and state[x][y-1] != '.' and state[x][y-2] == '.' and not visited[x][y-2]:
		p = copy.deepcopy(position)
		p.append([x,y-2])
		dfs(state,p,visited,color)
	if y+1 >=0 and y+1 < 16 and y+2 >=0 and y+2 < 16 and state[x][y+1] != '.' and state[x][y+2] == '.' and not visited[x][y+2]:
		p = copy.deepcopy(position)
		p.append([x,y+2])
		dfs(state,p,visited,color)
	if x+1 >= 0 and x+1 < 16 and y-1 >=0 and y-1 < 16 and x+2 >= 0 and x+2 < 16 and y-2 >=0 and y-2 < 16 and state[x+1][y-1] != '.' and state[x+2][y-2] == '.' and not visited[x+2][y-2]:
		p = copy.deepcopy(position)
		p.append([x+2,y-2])
		dfs(state,p,visited,color)
	if x+1 >= 0 and x+1 < 16 and x+2 >= 0 and x+2 < 16 and state[x+1][y] != '.' and state[x+2][y] == '.' and not visited[x+2][y]:
		p = copy.deepcopy(position)
		p.append([x+2,y])
		dfs(state,p,visited,color)
	if x+1 >= 0 and x+1 < 16 and y+1 >=0 and y+1 < 16 and x+2 >= 0 and x+2 < 16 and y+2 >=0 and y+2 < 16 and state[x+1][y+1] != '.' and state[x+2][y+2] == '.' and not visited[x+2][y+2]:
		p = copy.deepcopy(position)
		p.append([x+2,y+2])
		dfs(state,p,visited,color)

def actions(state,color):
	global jumps
	if color == 'B':
		initial_pos = [[0,0], [0,1], [0,2], [0,3], [0,4], [1,0], [1,1], [1,2], [1,3], [1,4], [2,0], [2,1], [2,2], [2,3], [3,0], [3,1], [3,2], [4,0], [4,1]]
		oppose_camp = [[11,15], [11,14], [12,15], [12,14], [12,13], [13,15], [13,14], [13,13], [13,12], [14,15], [14,14], [14,13], [14,12], [14,11], [15,15], [15,14], [15,13], [15,12], [15,11]]
	else:
		initial_pos = [[11,15], [11,14], [12,15], [12,14], [12,13], [13,15], [13,14], [13,13], [13,12], [14,15], [14,14], [14,13], [14,12], [14,11], [15,15], [15,14], [15,13], [15,12], [15,11]]
		oppose_camp = [[0,0], [0,1], [0,2], [0,3], [0,4], [1,0], [1,1], [1,2], [1,3], [1,4], [2,0], [2,1], [2,2], [2,3], [3,0], [3,1], [3,2], [4,0], [4,1]]
	position_list = []
	for i in range(16):
		for j in range(16):
			if state[i][j] == color:
				position_list.append([i,j])
	moves = []
	moves1 = []
	moves2 = []
	final_state = []

	if color == 'B':

		for i in range(len(position_list)):
			#print(position_list[i])
			

			if position_list[i] in initial_pos:


				valid_moves = []
				position = position_list[i]
				for x in range(-1,2):
					for y in range(-1,2):
						if x == -1 or y == -1:
							continue
						

						x1 = position[0] + x
						y1 = position[1] + y
						if x1 >= 0 and x1 < 16 and y1 >= 0 and y1 < 16 and state[x1][y1] == '.':
							valid_moves.append([position,[x1,y1]])
				visited = [[False for i in range(16)] for j in range(16)]
				jumps = []
				dfs(state,[position], visited, color)
				#print(jumps)

				moves1.extend(valid_moves)
				moves1.extend(jumps)

			else:
				valid_moves = []
				position = position_list[i]
				for x in range(-1,2):
					for y in range(-1,2):
						if position in oppose_camp and not(position[0]+x and position[1]+y in oppose_camp):
							continue
						x1 = position[0] + x
						y1 = position[1] + y
						if x1 >= 0 and x1 < 16 and y1 >= 0 and y1 < 16 and state[x1][y1] == '.':
							valid_moves.append([position,[x1,y1]])
				visited = [[False for i in range(16)] for j in range(16)]
				jumps = []
				dfs(state,[position], visited, color)
				moves2.extend(valid_moves)
				moves2.extend(jumps)
	else:

		

		for i in range(len(position_list)):
			#print(position_list[i])
			

			if position_list[i] in initial_pos:


				valid_moves = []
				position = position_list[i]
				for x in range(-1,2):
					for y in range(-1,2):
						if x == +1 or y == +1:
							continue
						

						x1 = position[0] + x
						y1 = position[1] + y
						if x1 >= 0 and x1 < 16 and y1 >= 0 and y1 < 16 and state[x1][y1] == '.':
							valid_moves.append([position,[x1,y1]])
				visited = [[False for i in range(16)] for j in range(16)]
				jumps = []
				dfs(state,[position], visited, color)
				#print(jumps)
				moves1.extend(valid_moves)
				moves1.extend(jumps)

			else:
				valid_moves = []
				position = position_list[i]
				for x in range(-1,2):
					for y in range(-1,2):
						if position in oppose_camp and not(position[0]+x and position[1]+y in oppose_camp):
							continue
						x1 = position[0] + x
						y1 = position[1] + y
						if x1 >= 0 and x1 < 16 and y1 >= 0 and y1 < 16 and state[x1][y1] == '.':
							valid_moves.append([position,[x1,y1]])
				visited = [[False for i in range(16)] for j in range(16)]
				jumps = []
				dfs(state,[position], visited, color)
				moves2.extend(valid_moves)
				moves2.extend(jumps)


			#print(moves)
			#print(visited)
	#print(moves1)
	#print(moves2)
	#print(len(moves1)

	if len(moves1) == 0:
		moves = moves2
	else:
		move11, move22 = [],[]
		for move in moves1:
			if move[-1] not in initial_pos:
				move11.append(move)
			else:
				move22.append(move)
		if move11:
			moves = move11
		else:
			moves = move22



	for i in range(len(moves)):
		state1 = copy.deepcopy(state)
		state1[moves[i][0][0]][moves[i][0][1]] = '.'
		state1[moves[i][-1][0]][moves[i][-1][1]] = color
		final_state.append(state1)
		#print(state1)
	#print(moves)
	#print(final_state)
	return moves, final_state



def max_value(state, alpha, beta, depth,color):
	if terminal_test(depth):
		return eval_fn(state,color)
	value = -math.inf
	act, s = actions(state,color)
	for a,s in zip(act,s):
		if color == 'B':
			value = max(value, min_value(s, alpha, beta, depth-1,'W'))
			if value >= beta:
				return value
			alpha = max(alpha,value)
		if color == 'W':
			value = max(value, min_value(s, alpha, beta, depth-1,'B'))
			if value >= beta:
				return value
			alpha = max(alpha,value)
	return value



def min_value(state, alpha, beta, depth,color):
	if terminal_test(depth):
		return eval_fn(state,color)
	value = math.inf
	act,s = actions(state,color)
	for a,s in zip(act,s):
		if color == 'B':
			value = min(value, max_value(s,alpha,beta,depth-1,'W'))
			if value <= alpha:
				return value
			beta = min(beta, value)
		if color == 'W':
			value = min(value, max_value(s,alpha,beta,depth-1,'B'))
			if value <= alpha:
				return value
			beta = min(beta, value)

	return value

def eval_fn(state,color):
	#for i in range(len(state)):
	#	print(state[i])
	#print(state)
	count1 = 0
	count2 = 0
	count3 = 0
	#for i in range(16):
		#for j in range(16):
			#print([i,j])
	
	if color == 'B':
		initial_pos = [[0,0], [0,1], [0,2], [0,3], [0,4], [1,0], [1,1], [1,2], [1,3], [1,4], [2,0], [2,1], [2,2], [2,3], [3,0], [3,1], [3,2], [4,0], [4,1]]
		oppose_camp = [[11,15], [11,14], [12,15], [12,14], [12,13], [13,15], [13,14], [13,13], [13,12], [14,15], [14,14], [14,13], [14,12], [14,11], [15,15], [15,14], [15,13], [15,12], [15,11]]

	else:
		initial_pos = [[11,15], [11,14], [12,15], [12,14], [12,13], [13,15], [13,14], [13,13], [13,12], [14,15], [14,14], [14,13], [14,12], [14,11], [15,15], [15,14], [15,13], [15,12], [15,11]]
		oppose_camp = [[0,0], [0,1], [0,2], [0,3], [0,4], [1,0], [1,1], [1,2], [1,3], [1,4], [2,0], [2,1], [2,2], [2,3], [3,0], [3,1], [3,2], [4,0], [4,1]]
		
	for i in range(16):
		for j in range(16):
			if [i,j] in initial_pos and state[i][j] == color: 
				count1 +=1
			elif [i,j] in oppose_camp and state[i][j] == color:
				count3 +=1
			elif [i,j] not in initial_pos and [i,j] not in oppose_camp and state[i][j] == color:
				count2 += 1


	count = (count1 * 15) + (count2 * 30) + (count3 * 45)
	return count


def terminal_test(depth):
	if depth == 0:
		return True
	return False

def alphabetamax(state,depth,color):
	val = max_value(state, -math.inf, math.inf, depth,color)
	#print(val)
	action, s  = actions(state,color)
	for i in range(len(s)):
		v = eval_fn(s[i],color)
		if v == val:
			return action[i]
	

def alphabetamin(state,depth,color):
	val = min_value(state, -math.inf, math.inf, depth,color)
	action, s = actions(state,colour)
	for i in range(len(s)):
		v = eval_fn(s[i],color)
		if v == val:
			return action[i]

final = []
inputfile = open("input.txt")
inputfile_string = inputfile.read().split('\n')
game_type = inputfile_string[0]
#print(game_type)
color_play = inputfile_string[1]
if color_play == "BLACK":
	color = 'B'
if color_play == "WHITE":
	color = 'W'
#print(color_play)
time_remaining = float(inputfile_string[2])
#print(time_remaining)
graph1 = []
for i in range(16):
    a = inputfile_string[3+i]
    graph1.append(a)
#print(graph1)
graph = [list(word) for word in graph1]
#print(graph)

#print(len(graph), len(graph[0]))
#moves, STATES = actions(graph,'W')
#for i in moves:
#	print(i)
#print(len(STATES))
#print(STATES)
#print(eval_fn(graph,'W'))
x =alphabetamax(graph,2,color)
#print(x)
'''
for i in range(len(x)):
		#final.append([x[i][1],x[i][0]])
		print(x[i][1],x[i][0])
#print(final)
'''
#for i in range(len(x) - 1):
	#print("E" + " " + str(x[i][1]),str(x[i][0]) + "," +  str(x[i+1][1]),str(x[i+1][0]))


flag = False

for i in range(-1,2):
	for j in range(-1,2):
		x1 = x[0][0]
		y1 = x[0][1]
		if x1 + i == x[-1][0] and y1 + j == x[-1][1]:
			flag = True

if flag == True:
	with open('output.txt','w') as f:
			out = "E" + " " + str(x[0][1]) + "," + str(x[0][0]) + " " + str(x[1][1]) + "," + str(x[1][0])
			f.write(out)
else:
	with open('output.txt','w') as f:
		for i in range(len(x) - 1):
			out = "J" + " " + str(x[i][1]) + "," + str(x[i][0]) + " " + str(x[i+1][1]) + "," + str(x[i+1][0])
			#print(out)
			if i == len(x)-2:
				f.write(out)
			else:		
				f.write(out + "\n")





