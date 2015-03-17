import pygame
 
# Define colors in RGB
WHITE  = ( 255, 255, 255)
BLUE   = (   0,   0, 255)
RED    = ( 255,   0,   0)
 
pygame.init()
  
# Set the height and width of the screen
size = [720, 480]
screen = pygame.display.set_mode(size)

# Set the game window name
pygame.display.set_caption("Bouncing Ball")
 
# Loop until the user clicks the close button
exit = False

# Continue the game while the user has lives
game_over = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Starting position of the ball
ball_x = 300
ball_y = 200

# Paddle starting position and dimensions
pad_width = 70
pad_height = 10
pad_x = size[0]/2 - pad_width/2
pad_y = 460
 
# Speed and direction of the ball
ball_change_x = 1
ball_change_y = 1

 
# --------- Main Program Loop ---------
while exit == False:
	for event in pygame.event.get(): # User did something
		# print event				--> show what user did
		if event.type == pygame.QUIT: # If user clicked close
			exit = True # Flag that we want to exit this loop
 
	# Set the screen background color
	screen.fill(WHITE)
 
	# Draw the ball around the center point, radius = 8 pixels
	pygame.draw.circle(screen, BLUE, (ball_x, ball_y), 8)
	
	# Draw the paddle
	paddle = pygame.Rect(pad_x, pad_y, pad_width, pad_height)
	pygame.draw.rect(screen, RED, paddle)
     
	# Move the ball
	ball_x += ball_change_x
	ball_y += ball_change_y
 
	# Bounce the ball if needed
	if ball_y >= 470 or ball_y <= 10:
		ball_change_y *= -1
	if ball_x >= 710 or ball_x <= 10:
		ball_change_x *= -1

	# Show current position of the ball
	print "X: %d Y: %d" % (ball_x, ball_y)
	
	# Limit updates to 120 frames per second
	clock.tick(120)
 
	# Update the entire area of the display to the screen 
	pygame.display.update()
     
pygame.quit()