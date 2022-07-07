# Link to the maze:  tinyurl.com/3kkt9zh3
def move():
	pass


def turn_left():
	pass


def front_is_clear():
	pass


def at_goal():
	pass


def right_is_clear():
	pass


def turn_around():
	turn_left()
	turn_left()


def turn_right():
	turn_around()
	turn_left()


while front_is_clear():
	move()
turn_right()

while not at_goal():
	if right_is_clear():
		turn_right()
		move()
	elif front_is_clear():
		move()
	else:
		turn_left()