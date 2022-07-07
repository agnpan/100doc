# Link to the maze:  tinyurl.com/3kkt9zh3

def turn_around():
	turn_left()
	turn_left()


def turn_right():
	turn_around()
	turn_left()


while not is_facing_north():
	turn_left()

while not at_goal():
	if right_is_clear():
		turn_right()
		move()
	elif front_is_clear():
		move()
	else:
		turn_left()