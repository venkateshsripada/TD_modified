
import numpy as np
import random

grid = np.full((5,10),0)	#define gridworld
# grid[1][0] = 1
# grid[2][0] = 2
# grid[3][0] = 3
grid[3][9] = 20	
# grid[0][1] = 100
print (grid)

''' agent motions'''
move_left = (0,-1)
move_right = (0,1)
move_up = (-1,0)
move_down = (1,0)

''' can be removed
agent_pos = grid[random.randint(0,4)][random.randint(0,9)]
print (agent_pos)
'''

rob_pos = random.randint(0,4),random.randint(0,9)
def random_policy_robot():
	
	rob_move = random.randrange(0,4,1)  

	if (rob_move == 0) and (rob_pos[0] >= 1):		#the robot can be anywhere except the zeroth column
		rob_pos += move_left[0],move_left[1]
	elif (rob_move == 0) and (rob_pos[0] == 0):
		rob_pos += move_right[0], move_right[1]

	elif (rob_move == 1) and (rob_pos[0] <= 8):
		rob_pos += move_right[0], move_right[1]
	elif (rob_move == 1) and (rob_pos[0] == 9):
		rob_pos += move_left[0], move_left[1]

	elif (rob_move == 2) and (rob_pos[1] >= 1):
		rob_pos += move_up[0], move_up[1]  
	elif (rob_move == 2) and (rob_pos[1] == 0):
		rob_pos += move_down[0], move_down[1]

	elif (rob_move == 3) and (rob_pos[1] <= 3):
		rob_pos += move_down[0], move_down[1]
	elif (rob_move == 3) and (rob_pos[1] == 4):
		rob_pos += move_up[0], move_up[1]

	next_state()
	return rob_pos

goal_pos = (3,9)		#initial state of the goal
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

policy = ()
def next_state():

	rob_pos_left += move_left[0],move_left[1]
	rob_pos_right += move_right[0], move_right[1]
	rob_pos_up += move_up[0], move_up[1]
	rob_pos_down += move_down[0], move_down[1]

	next_rob_value = max(grid[rob_pos_left], grid[rob_pos_right], grid[rob_pos_up], grid[rob_pos_down]) 

	if rob_pos_left == next_rob_value:
		policy.append(rob_pos_left)

	elif rob_pos_right == next_rob_value:
		policy.append(rob_pos_right)

	elif rob_pos_up == next_rob_value:
		policy.append(rob_pos_up)

	elif rob_pos_down == next_rob_value:
		policy.append(rob_pos_down)

	return next_rob_value

def update_q_value():

	grid[rob_pos] = grid[rob_pos] + step_size * (reward + exploration_rate*next_state() - grid[rob_pos])  

def iterations(episodes):
	random_policy_robot()
	for i in range(episodes):
		goal_pos()
		rob_pos = policy[-1]
		update_q_value()
		

if __name__ == '__main__':
	random_policy_robot()


