import pygame
 
# Define colors in RGB
white  = ( 255, 255, 255)
blue   = (   0,   0, 255)
 
pygame.init()
  
# Set the height and width of the screen
size = [720, 480]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Bouncing Ball")
 
#Loop until the user clicks the close button.
exit = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Starting position of the ball
ball_x = 300
ball_y = 200
 
# Speed and direction of the ball
ball_change_x = 1
ball_change_y = 1
 
# -------- Main Program Loop -----------
while exit == False:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			exit = True # Flag that we are done so we exit this loop
 
	# Set the screen background
	screen.fill(white)
 
	# Draw the ball
	pygame.draw.circle(screen, blue, (ball_x, ball_y), 10)
     
	# Move the ball
	ball_x += ball_change_x
	ball_y += ball_change_y
 
	# Bounce the ball if needed
	if ball_y >= 470 or ball_y <= 10:
		ball_change_y *= -1
	if ball_x >= 710 or ball_x <= 10:
		ball_change_x *= -1

	# Limit to 120 frames per second
	clock.tick(120)
 
	# Show current position of the ball
	print "X: %d Y: %d" % (ball_x, ball_y)
 
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
     
pygame.quit()