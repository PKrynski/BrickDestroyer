from random import randint
import pygame
 
# Define colors in RGB
WHITE  = ( 255, 255, 255)
BLACK  = (   0,   0,   0)
BLUE   = (   0,   0, 255)
RED    = ( 255,   0,   0)
GRAY   = ( 200, 200, 200)
 
pygame.init()
  
# Set the height and width of the screen
size = [720, 480]
screen = pygame.display.set_mode(size)

# Set the game window name
pygame.display.set_caption("Bouncing Ball")
 
def ShowMessage(text, color, size, position):
	myfont = pygame.font.Font("AGENCYB.ttf", size)
	message = myfont.render(text, True, color)
	
	screen.blit(message, position)

def MovePaddle(pad_x, pad_width, key):
	pad_left = pad_x
	pad_right = pad_x + pad_width

	if key[pygame.K_LEFT] == True and pad_left > 0:
		pad_x -= 2
	elif key[pygame.K_RIGHT] == True and pad_right < size[0]:
		pad_x += 2
	
	return pad_x

def generate_colors():
	colors = []
	for i in range(0, 300):
		colors.append(randint(0, 200))
	return colors

def CreateBricks():
	y_ofs = 35
	bricks = []
	for i in range(7):
		x_ofs = 5
		for j in range(10):
			bricks.append([x_ofs, y_ofs, 70, 20])
			x_ofs += 70 + 1
		y_ofs += 20 + 1
	return bricks

def DrawBricks(screen, bricks, colors):
	a = 0
	b = 1
	c = 2	
	for brick in bricks:
		if brick == None:
			colors[a] = None
			colors[b] = None
			colors[c] = None
		else:
			if colors[a] == None:
				a += 3
				b += 3
				c += 3
			
			oneBrick = pygame.Rect(brick)
			pygame.draw.rect(screen, (colors[a], colors[b], colors[c]), brick)
			a += 3
			b += 3
			c += 3

def RemoveBricks(ball_x, ball_y, ball_rad, bricks, ball_change_x, ball_change_y):
	
	ball_top = ball_y - ball_rad
	ball_bottom = ball_y + ball_rad
	
	for brick in bricks:
		try:
			if brick !=  None:
				brick_left = brick[0]
				brick_right = brick[0] + 70
				
				if int(ball_top) == brick[1] + 20:
					if ball_x >= brick_left and ball_x <= brick_right:
						
						ball_change_y *= -1
						i = bricks.index(brick)
						bricks[i] = None

		except ValueError:
			pass

	

	return (bricks, ball_change_x, ball_change_y)


def show_list(bricks): #--------------------------------------------------
	for brick in bricks:
		print brick

def RunGame():	
	
	# Run the game until the user clicks the close button
	exit = False

	# Game status
	game_status = "ready"

	# Continue the game while the user has lives
	lives = 1

	# Generate random color values list:
	colors = generate_colors()

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()
	
	# Paddle starting position and dimensions
	pad_width = 68
	pad_height = 10
	pad_x = size[0]/2 - pad_width/2
	pad_y = 460

	# Ball size (radius)
	ball_rad = 8

	# Speed and direction of the ball
	ball_change_x = 0
	ball_change_y = 0
	
	# Create bricks
	bricks = CreateBricks()

	show_list(bricks) # ---------------------------
	
	
	# --------- Main Game Loop ---------
	while exit == False:
		for event in pygame.event.get(): # User did something
			# print event				--> show what user did
			if event.type == pygame.QUIT: # If user clicked close
				exit = True # Flag that we want to exit this loop
	 
		while game_status == "game over":
			
			screen.fill(BLACK)
			
			ShowMessage("GAME OVER", RED, 120, (120, 140))
			ShowMessage("Press Enter to play again", GRAY, 36, (210, 290))
			ShowMessage("Press Escape to quit", GRAY, 36, (240, 330))
			
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_status = "quit"
					exit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						game_status = "quit"
						exit = True
					if event.key == pygame.K_RETURN:
						RunGame()

		
		# Set the screen background color
		screen.fill(WHITE)
		
		# Hide mouse pointer
		pygame.mouse.set_visible(0)
		
		# Keyboard input
		pressed_key = pygame.key.get_pressed()
		
		# Ready to play
		if game_status == "ready":
			# Ball starting position
			ball_x = pad_x + pad_width/2
			ball_y = pad_y - ball_rad
			
			ShowMessage("Press space to launch the ball", BLACK, 50, (100, 250))
			
			if pressed_key[pygame.K_SPACE] == True:
				ball_change_x = 1
				ball_change_y = -1
				game_status = "playing"
		
		
		# Lose a life and reset the game if the ball has gone past the paddle
		ball_top = ball_y - ball_rad

		if game_status == "playing" and ball_top >= size[1]:
			lives -= 1
			
			if lives > 0:
				game_status = "ready"
			else:
				game_status = "game over"
		
		
		# Move the paddle
		pad_x = MovePaddle(pad_x, pad_width, pressed_key)

		# Playing
		if game_status == "playing":
			
			# Move the ball
			ball_x += ball_change_x
			ball_y += ball_change_y
			
			ball_left = ball_x - ball_rad
			ball_right = ball_x + ball_rad
			ball_top = ball_y - ball_rad
			ball_bottom = ball_y + ball_rad
			
			# Bounce the ball off the sides
			if ball_x >= size[0] - ball_rad or ball_x <= ball_rad:
				ball_change_x *= -1
			if  ball_y <= ball_rad:
				ball_change_y *= -1

			
			# Bounce the ball off the paddle
			if ball_bottom >= pad_y and ball_bottom < pad_y + 1:
				
				# Vary the angle depending on where the ball hit the paddle
				
				# Bounce to the right
				if ball_x >= pad_x + pad_width/2 and ball_x <= pad_x + pad_width:
					if ball_x > pad_x + 5.0/6 * pad_width:		# +60
						ball_change_x = 1.22
						ball_change_y = -0.70
					elif ball_x > pad_x + 4.0/6 * pad_width:	# +45
						ball_change_x = 1
						ball_change_y = -1
					else:										# +30
						ball_change_x = 0.70
						ball_change_y = -1.22
				
				# Bounce to the left
				if ball_x >= pad_x and ball_x <= pad_x + pad_width/2:
					if ball_x < pad_x + 1.0/6 * pad_width:		# -60
						ball_change_x = -1.22
						ball_change_y = -0.70
					elif ball_x < pad_x + 2.0/6 * pad_width:	# -45
						ball_change_x = -1
						ball_change_y = -1
					else:										# -30
						ball_change_x = -0.70
						ball_change_y = -1.22


			# Check if any bricks have been hit ----------------------------------------------------------
			#check_hit(bricks)
			
			
		# Remove bricks if hit
		bricks, ball_change_x, ball_change_y = RemoveBricks(ball_x, ball_y, ball_rad, bricks, ball_change_x, ball_change_y)
		
		# Draw the bricks
		DrawBricks(screen, bricks, colors)
		
		# Draw the ball around the center point
		pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_rad)
		
		# Draw the paddle
		paddle = pygame.Rect(pad_x, pad_y, pad_width, pad_height)
		pygame.draw.rect(screen, RED, paddle)
		
		# Show current position of the ball and paddle
		#print "X: %d Y: %d PAD LEFT: %d PAD RIGHT: %d GAME STATUS: %s" % (ball_x, ball_y, pad_left, pad_right, game_status)
		
		# Limit updates to 120 frames per second
		clock.tick(120)
	 
		# Update the entire area of the display to the screen 
		pygame.display.update()

	pygame.quit()

RunGame()