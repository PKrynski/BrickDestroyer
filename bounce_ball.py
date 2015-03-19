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

# Continue the game while the user has lives
lives = 3
game_over = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Ball starting position and size (radius)
ball_rad = 8
ball_x = 150
ball_y = 200

# Paddle starting position and dimensions
pad_width = 68
pad_height = 10
pad_x = size[0]/2 - pad_width/2
pad_y = 460
 
# Speed and direction of the ball
ball_change_x = 1
ball_change_y = 1

 
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
 
	# Draw the ball around the center point
	pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_rad)
	
	# Draw the paddle
	paddle = pygame.Rect(pad_x, pad_y, pad_width, pad_height)
	pygame.draw.rect(screen, RED, paddle)
     
	# Move the ball
	ball_x += ball_change_x
	ball_y += ball_change_y
	
	ball_left = ball_x - ball_rad
	ball_right = ball_x + ball_rad
	ball_top = ball_y - ball_rad
	ball_bottom = ball_y + ball_rad
 
	# Move the paddle
	key = pygame.key.get_pressed()
	
	if key[pygame.K_LEFT] == True and pad_left > 0:
		pad_x -= 2
	elif key[pygame.K_RIGHT] == True and pad_right < size[0]:
		pad_x += 2
	
	pad_left = pad_x
	pad_right = pad_x + pad_width
	
	# Bounce the ball off the sides
	if ball_x >= 710 or ball_x <= 10:
		ball_change_x *= -1
	if  ball_y <= 10:
		ball_change_y *= -1
	
	# Bounce the ball off the paddle
	if ball_bottom == pad_y and ball_x > pad_left and ball_x < pad_right:
		ball_change_y *= -1
	
	# Show current position of the ball and paddle
	print "X: %d Y: %d    PAD LEFT: %d  PAD RIGHT: %d" % (ball_x, ball_y, pad_left, pad_right)
	
	# Limit updates to 120 frames per second
	clock.tick(120)
 
	# Update the entire area of the display to the screen 
	pygame.display.update()
     
pygame.quit()