# Import the pygame library and initialise the game engine
import pygame
from Paddle import Paddle
from Ball import Ball
from Bricks import Brick
 
pygame.init()
 
#Ask the player(s) for their inputs in number of players and lives; validate their inputs to be legal
numPlay = -1
while (numPlay < 0):
    try:
        numPlay = int(input("Please enter number of players (1-2): "))
    except ValueError as e:
        print("Please enter a valid integer in the range 1-2! ")
    except (numPlay != 1 or numPlay != 2) as n:
        print("Please enter a value in the range 1-2! ")

lives = -1
while (lives < 1):
    try:
        lives = int(input("How many lives would you like to start with (1 - 10): "))
    except ValueError as e:
        print("Please enter a valid integer in the range 1-15! ")
    except (lives < 1 or lives > 10) as l:
        print("Please enter a value in the range 1-10! ")


# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 155, 0)
 
# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakaway -- 1 or 2 players")


if numPlay ==1 : 
    score = 0
    
    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.x = 780
    paddleA.rect.y = 200

    ball = Ball(WHITE,10,10)
    ball.rect.x = 195
    ball.rect.y = 195

    all_sprites_list = pygame.sprite.Group()
    
    # Add the 2 paddles and the ball to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(ball)
    all_bricks = pygame.sprite.Group()

    #player 1 bricks
    for i in range(20):
        brick = Brick(RED,15,30)
        brick.rect.x = 15
        brick.rect.y = 0 + i *30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(BLUE, 15, 30)
        brick.rect.x = 30
        brick.rect.y = 0 + i*30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(YELLOW,15,30)
        brick.rect.x = 45
        brick.rect.y = 0 + i*30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(GREEN,15,30)
        brick.rect.x = 60
        brick.rect.y = 0 + i*30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(ORANGE,15,30)
        brick.rect.x = 75
        brick.rect.y = 0 + i * 30
        all_sprites_list.add(brick)
        all_bricks.add(brick)


    carryOn = True
    
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddleA.moveUp(7)
        if keys[pygame.K_DOWN]:
            paddleA.moveDown(7)


        all_sprites_list.update()
    
        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=790:
            ball.velocity[0] = -ball.velocity[0]
            lives -= 1
            if lives == 0:
                #Display Game Over Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, WHITE)
                screen.blit(text, (250,300))
                pygame.display.flip()
                pygame.time.wait(3000)
    
                #Stop the Game
                carryOn=False
    
        if ball.rect.x<=60:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>590:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<60:
            ball.velocity[1] = -ball.velocity[1]
    
        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()
    
        #Check if there is the ball collides with any of bricks
        brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
        for brick in brick_collision_list:
            ball.bounce()
            score += 1
            brick.kill()
        if len(all_bricks)==0:
            #Display Level Complete Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("YOU WIN!", 1, WHITE)
                screen.blit(text, (200,300))
                pygame.display.flip()
                pygame.time.wait(3000)
    
                #Stop the Game
                carryOn=False
    
        # --- Drawing code should go here
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [80, 60], [800, 60], 2)
    
        #Display the score and the number of lives at the top of the screen
        font = pygame.font.Font(None, 24)
        text = font.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (100,10))
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (650,10))
    
        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
        # --- Limit to 60 frames per second
        clock.tick(60)

elif numPlay == 2:
    scoreA = 0
    scoreB = 0

    #ask about lives
    lives = 3
    
    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = 200
    
    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = 780
    paddleB.rect.y = 200
    
    ball = Ball(WHITE,10,10)
    ball.rect.x = 425
    ball.rect.y = 195



    
    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    
    # Add the 2 paddles and the ball to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

    all_bricks = pygame.sprite.Group()

    #player 1 bricks
    for i in range(20):
        brick = Brick(RED,15,30)
        brick.rect.x = 270
        brick.rect.y = 0 + i *30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(BLUE, 15, 30)
        brick.rect.x = 285
        brick.rect.y = 0 + i*30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(YELLOW,15,30)
        brick.rect.x = 300
        brick.rect.y = 0 + i*30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(GREEN,15,30)
        brick.rect.x = 315
        brick.rect.y = 0 + i*30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(ORANGE,15,30)
        brick.rect.x = 330
        brick.rect.y = 0 + i*30
        all_sprites_list.add(brick)
        all_bricks.add(brick)


    #player 2 bricks
    for i in range(20):
        brick = Brick(RED,15,30)
        brick.rect.x = 425
        brick.rect.y = 0 + i * 30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(BLUE, 15, 30)
        brick.rect.x = 410
        brick.rect.y = 0 + i* 30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(YELLOW,15,30)
        brick.rect.x = 395
        brick.rect.y = 0 + i* 30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(GREEN,15,30)
        brick.rect.x = 380
        brick.rect.y = 0 + i* 30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(20):
        brick = Brick(ORANGE,15,30)
        brick.rect.x = 365
        brick.rect.y = 0 + i* 30
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    
    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carryOn = True
    
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)  
    
        # --- Game logic should go here
        all_sprites_list.update()
    
        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=790:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=60:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>590:
            ball.velocity[1] = -ball.velocity[1]
            lives -= 1
            if lives == 0:
                #Display Game Over Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, WHITE)
                screen.blit(text, (250,300))
                pygame.display.flip()
                pygame.time.wait(3000)
    
                #Stop the Game
                carryOn=False
    
        if ball.rect.y<40:
            ball.velocity[1] = -ball.velocity[1]
    
        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleB):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()
    
        #Check if there is the ball collides with any of bricks
        brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
        for brick in brick_collision_list:
            ball.bounce()
            scoreA += 1
            brick.kill()
        if len(all_bricks)==0:
            #Display Level Complete Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("YOU WIN!", 1, WHITE)
                screen.blit(text, (200,300))
                pygame.display.flip()
                pygame.time.wait(3000)
    
                #Stop the Game
                carryOn=False
    
        # --- Drawing code should go here
        # First, clear the screen to dark blue.
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [0, 60], [800, 60], 2)
    
        #Display the score and the number of lives at the top of the screen
        font = pygame.font.Font(None, 24)
        text = font.render("Score Player 1: " + str(scoreA), 1, WHITE)
        screen.blit(text, (20,10))
        text = font.render("Score Player 2: " + str(scoreB), 1, WHITE)
        screen.blit(text, (20,40))
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (650,10))
    
        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
        # --- Limit to 60 frames per second
        clock.tick(60)
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()