import pygame
 
# Define colors in RGB
WHITE  = ( 255, 255, 255)
BLACK  = (   0,   0,   0)
BLUE   = (   0,   0, 255)
RED    = ( 255,   0,   0)
 
pygame.init()
  
# Set the height and width of the screen
size = [720, 480]
screen = pygame.display.set_mode(size)

# Set the game window name
pygame.display.set_caption("Bouncing Ball")
 
# Run the game until the user clicks the close button
exit = False

# Game status
game_status = "ready"

# Continue the game while the user has lives
lives = 3
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Paddle starting position and dimensions
pad_width = 270
pad_height = 10
pad_x = size[0]/2 - pad_width/2
pad_y = 460

# Ball size (radius)
ball_rad = 8

# Speed and direction of the ball
ball_change_x = 0
ball_change_y = 0

def ShowMessage(text, color, size, position):
	myfont = pygame.font.Font(None, size)
	message = myfont.render(text, True, color)
	
	screen.blit(message, position)


# --------- Main Game Loop ---------
while exit == False:
	for event in pygame.event.get(): # User did something
		# print event				--> show what user did
		if event.type == pygame.QUIT: # If user clicked close
			exit = True # Flag that we want to exit this loop
 
	# Set the screen background color
	screen.fill(WHITE)
	
	# Hide mouse pointer
	pygame.mouse.set_visible(0)
	
	# Keyboard input
	key = pygame.key.get_pressed()

	# Ready to play
	if game_status == "ready":
		# Ball starting position
		ball_x = pad_x + pad_width/2
		ball_y = pad_y - ball_rad
		
		ShowMessage("Press space to launch the ball", BLACK, 50, (100, 200))
		
		if key[pygame.K_SPACE] == True:
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
			ShowMessage("GAME OVER", RED, 120, (100, 200))
			# game_status = "game over"
	
	

	# Move the paddle		
	if key[pygame.K_LEFT] == True and pad_left > 0:
		pad_x -= 2
	elif key[pygame.K_RIGHT] == True and pad_right < size[0]:
		pad_x += 2
	
	pad_left = pad_x
	pad_right = pad_x + pad_width
	
	
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
				if ball_x > pad_x + 5/6 * pad_width:
					ball_change_x = 1.22
					ball_change_y = -0.70
				elif ball_x > pad_x + 4/6 * pad_width:
					ball_change_x = 1
					ball_change_y = -1
				else:
					ball_change_x = 0.70
					ball_change_y = -1.22
			
			# Bounce to the left
			if ball_x >= pad_x and ball_x <= pad_x + pad_width/2:
				if ball_x < pad_x + 1/6 * pad_width:
					ball_change_x = -1.22
					ball_change_y = -0.70
				elif ball_x < pad_x + 2/6 * pad_width:
					ball_change_x = -1
					ball_change_y = -1
				else:
					ball_change_x = -0.70
					ball_change_y = -1.22


	# Draw the ball around the center point
	pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_rad)
	
	# Draw the paddle
	paddle = pygame.Rect(pad_x, pad_y, pad_width, pad_height)
	pygame.draw.rect(screen, RED, paddle)
	
	# Show angle
	if ball_change_x == 0:
		angle = 0	
	elif ball_change_x == 1.22:
		angle = 60
	elif ball_change_x == -1.22:
		angle = -60
	elif ball_change_x == 1:
		angle = 45
	elif ball_change_x == -1:
		angle = -45
	elif ball_change_x == 0.70:
		angle = 30
	elif ball_change_x == -0.70:
		angle = -30
	
	# Show current position of the ball and paddle
	print "X: %d Y: %d PAD_x: %d PAD RIGHT: %d GAME STATUS: %s ANGLE: %d" % (ball_x, ball_y, pad_x, pad_right, game_status, angle)
	
	# Limit updates to 120 frames per second
	clock.tick(120)
 
	# Update the entire area of the display to the screen 
	pygame.display.update()
     
pygame.quit()