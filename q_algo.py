
import numpy as np
import random


# grid[1][0] = 1
# grid[2][0] = 2
# grid[3][0] = 3

# grid[0][1] = 100
# print (grid)

''' agent motions'''


def initial_random_policy_robot():
	
	rob_move = random.randrange(0,4,1)  
	rob_pos_x = random.randint(0,4)
	rob_pos_y = random.randint(0,9)
	#print(rob_pos)
	if (rob_move == 0) and (rob_pos_x >= 1):		#the robot can be anywhere except the zeroth column
		rob_pos_x += move_left[0]
		rob_pos_y += move_left[1]
		policy.append(rob_pos)
		#grid[rob_pos] = grid[rob_pos] - 1

	elif (rob_move == 0) and (rob_pos_y == 0):
		rob_pos_x += move_right[0]
		rob_pos_y +=  move_right[1]
		policy.append(rob_pos)
		#grid[rob_pos] = grid[rob_pos] - 1


	elif (rob_move == 1) and (rob_pos_x <= 8):		#if rand = 1
		rob_pos_x += move_right[0]
		rob_pos_y += move_right[1]
		policy.append(rob_pos)
		#grid[rob_pos] = grid[rob_pos] - 1

	elif (rob_move == 1) and (rob_pos_x == 9):
		rob_pos_x += move_left[0]
		rob_pos_y += move_left[1]
		policy.append(rob_pos)
		#grid[rob_pos] = grid[rob_pos] - 1


	elif (rob_move == 2) and (rob_pos_y >= 1):		#if rand = 2
		rob_pos_x += move_up[0]
		rob_pos_y += move_up[1]  
		policy.append(rob_pos)
		#grid[rob_pos] = grid[rob_pos] - 1

	elif (rob_move == 2) and (rob_pos_y == 0):
		rob_pos_x += move_down[0]
		rob_pos_y += move_down[1]
		policy.append(rob_pos)
		#grid[rob_pos] = grid[rob_pos] - 1


	elif (rob_move == 3) and (rob_pos_y <= 3):		#if rand = 3
		rob_pos_x += move_down[0]
		rob_pos_y += move_down[1]
		policy.append(rob_pos)
		#grid[rob_pos] = grid[rob_pos] - 1

	elif (rob_move == 3) and (rob_pos_y == 4):
		rob_pos_x += move_up[0]
		rob_pos_y += move_up[1]
		policy.append(rob_pos)
		#grid[rob_pos] = grid[rob_pos] - 1

	return rob_pos_x, rob_pos_y

def random_policy(rob_pos):
	print( type(rob_pos) )
	rob_pos_left = rob_pos + move_left[0],move_left[1]
	rob_pos_right = rob_pos + move_right[0], move_right[1]
	rob_pos_up = rob_pos + move_up[0], move_up[1]
	rob_pos_down = rob_pos + move_down[0], move_down[1]

	#print(rob_pos_left)

	next_rob_value = max(grid[rob_pos_left], grid[rob_pos_right], grid[rob_pos_up], grid[rob_pos_down]) 


	if (grid[rob_pos_left] == grid[rob_pos_right] == grid[rob_pos_up] == grid[rob_pos_down]):
		rob_pos = rob_pos + move_right[0], move_right[1] 
		#grid[rob_pos] = grid[rob_pos] - 1
		policy.append(rob_pos)
	
	elif grid[rob_pos_left] == next_rob_value:
		rob_pos = rob_pos + move_left[0], move_left[1]
		#grid[rob_pos] = grid[rob_pos] - 1
		policy.append(rob_pos_left)

	elif grid[rob_pos_right] == next_rob_value:
		rob_pos = rob_pos + move_right[0], move_right[1]
		#grid[rob_pos] = grid[rob_pos] - 1
		policy.append(rob_pos_right)

	elif grid[rob_pos_up] == next_rob_value:
		rob_pos = rob_pos + move_up[0], move_up[1]
		#grid[rob_pos] = grid[rob_pos] - 1
		policy.append(rob_pos_up)

	elif grid[rob_pos_down] == next_rob_value:
		rob_pos = rob_pos + move_down[0], move_down[1]
		#grid[rob_pos] = grid[rob_pos] - 1
		policy.append(rob_pos_down)


	rob_pos = policy[-1]
	return next_rob_value


def goal_position():	
	
	#print (grid[goal_pos[0]][goal_pos[1]])
	goal_move = random.randrange(0,4,1)		#the goal moves in any direction randonly

	if (goal_move == 0) and (goal_pos[0] >= 1):		#the goal can be anywhere except the zeroth column
		goal_pos += move_left[0],move_left[1]
	elif (goal_move == 0) and (goal_pos[0] == 0):
		goal_pos += move_right[0], move_right[1]

	elif (goal_move == 1) and (goal_pos[0] <= 8):
		goal_pos += move_right[0], move_right[1]
	elif (goal_move == 1) and (goal_pos[0] == 9):
		goal_pos += move_left[0], move_left[1]

	elif (goal_move == 2) and (goal_pos[1] >= 1):
		goal_pos += move_up[0], move_up[1]  
	elif (goal_move == 2) and (goal_pos[1] == 0):
		goal_pos += move_down[0], move_down[1]

	elif (goal_move == 3) and (goal_pos[1] <= 3):
		goal_pos += move_down[0], move_down[1]
	elif (goal_move == 3) and (goal_pos[1] == 4):
		goal_pos += move_up[0], move_up[1]

	return goal_pos


def next_state():

	rob_pos_left += move_left[0],move_left[1]
	rob_pos_right += move_right[0], move_right[1]
	rob_pos_up += move_up[0], move_up[1]
	rob_pos_down += move_down[0], move_down[1]

	next_rob_value = max(grid[rob_pos_left], grid[rob_pos_right], grid[rob_pos_up], grid[rob_pos_down]) 

	if grid[rob_pos_left] == next_rob_value:
		rob_pos = rob_pos + move_left[0], move_left[1]
		policy.append(rob_pos_left)

	elif grid[rob_pos_right] == next_rob_value:
		rob_pos = rob_pos + move_right[0], move_right[1]
		policy.append(rob_pos_right)

	elif grid[rob_pos_up] == next_rob_value:
		rob_pos = rob_pos + move_up[0], move_up[1]
		policy.append(rob_pos_up)

	elif grid[rob_pos_down] == next_rob_value:
		rob_pos = rob_pos + move_down[0], move_down[1]
		policy.append(rob_pos_down)

	global rob_pos

	return next_rob_value, rob_pos

def update_q_value():

	if rob_pos != goal_pos:
		reward = -1

	grid[rob_pos] = grid[rob_pos] + step_size * (reward + exploration_rate*next_state()[0] - grid[rob_pos])  
	next_state()[1]

def iterations():
	
	initial_random_policy_robot()

	while rob_pos != goal_pos:
		random_policy(rob_pos)
		goal_pos()

		update_q_value()
		print ("end state obtained with policy: ", policy)

		
		
move_left = (0,-1)
move_right = (0,1)
move_up = (-1,0)
move_down = (1,0)


grid = np.full((5,10),0)	#define gridworld
grid[3][9] = 20	

goal_pos = (3,9)		#initial state of the goal
policy = []
rob_pos = random.randint(0,4),random.randint(0,9)
#print (rob_pos)


#if __name__ == '__main__':
iterations()


