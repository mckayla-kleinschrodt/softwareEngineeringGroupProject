# Import the pygame library and initialize the game engine
import pygame
from Paddle import Paddle
from Ball import Ball
from Bricks import Brick
 
pygame.init()

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
font = pygame.font.SysFont("Arial", 20)
pygame.display.set_caption("Welcome to Brick Pong!")

font = pygame.font.Font(None, 24)
text = font.render("Enter Number of Players: (1-2)", 1, WHITE)
screen.blit(text, (70,180))
text = font.render("Enter Lives: (1-10)", 1, WHITE)
screen.blit(text, (450,180))
text = font.render("Enter Difficulty Level: (1 Easy, 2 Normal, 3 Hard)", 1, WHITE)
screen.blit(text, (150,280))

# inputs for inital game screen 
user_input = ""
user_input_players = ""
user_input_lives = ""
user_input_difficulty = ""
players = 0
lives = 0
difficulty = 0
input_rect = pygame.Rect(100, 200, 140, 32)
input_rect_lives = pygame.Rect(450, 200, 140, 32)
input_rect_difficulty = pygame.Rect(170, 300, 140, 32)
input_players = False
input_lives = False
input_difficulty = False
index = True

# -------- Initial Program Loop -----------
while index:
    # --- Events for setting up the game
    for event in pygame.event.get(): # User did something
        if event.type == pygame.MOUSEBUTTONDOWN: # If user clicks in text box
            if input_rect.collidepoint(event.pos):
                input_players = True
                input_lives = False
                input_difficulty = False
            elif input_rect_lives.collidepoint(event.pos):
                input_lives = True
                input_players = False
                input_difficulty = False
            else:
                input_difficulty = True
                input_lives = False
                input_players = False
        if event.type ==pygame.KEYDOWN:
            if input_players:
                user_input_players += event.unicode 
                try:
                    players = int(user_input_players)
                    if players < 1 or players > 2:
                        print("Invalid player selection! Please input 1 or 2")
                        user_input_players = ""
                except:
                    print("Invalid player selection! Please input 1 or 2")
                    user_input_players = ""
            elif input_lives:
                user_input_lives += event.unicode
                try:
                    lives = int(user_input_lives)
                    if lives < 1 or lives > 10:
                        print("Invalid player lives selection! Please input 1-10")
                        user_input_lives = ""
                except:
                    print("Invalid player lives selection! Please input 1-10")
                    user_input_lives = ""
            else:
                user_input_difficulty += event.unicode 
                try:
                    difficulty = int(user_input_difficulty)
                    if difficulty < 1 or difficulty > 3:
                        print("Invalid difficulty selection! Please input 1 for easy mode, 2 for normal mode, 3 for hard mode")
                        user_input_difficulty = ""
                except:
                    print("Invalid difficulty selection! Please input 1 for easy mode, 2 for normal mode, 3 for hard mode")
                    user_input_difficulty = ""
        if event.type==pygame.K_RETURN:
            index = False
            break
        

    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, WHITE, input_rect)
    pygame.draw.rect(screen, WHITE, input_rect_lives)
    pygame.draw.rect(screen, WHITE, input_rect_difficulty)
    
    text_surface_players = font.render(user_input_players, True, BLACK)
    text_surface_lives = font.render(user_input_lives, True, BLACK)
    text_surface_difficulty = font.render(user_input_difficulty, True, BLACK)      

    # render at position stated in arguments
    screen.blit(text_surface_players, (input_rect.x+5, input_rect.y+5))
    screen.blit(text_surface_lives, (input_rect_lives.x+5, input_rect_lives.y+5))
    screen.blit(text_surface_difficulty, (input_rect_difficulty.x+5, input_rect_difficulty.y+5))

    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface_players.get_width()+10)
    input_rect_lives.w = max(100, text_surface_lives.get_width()+10)
    input_rect_difficulty.w = max(100, text_surface_difficulty.get_width()+10)

    pygame.display.flip()

    if players != 0 and lives != 0 and difficulty != 0:
        screen.fill(BLACK)
        index = False
        
# -------- END of Initial Program Loop -----------
# -------- BEGIN Game Play -----------
numPlay = players

if numPlay ==1 : 
    score = 0
    
    if difficulty == 1:
        paddleA = Paddle(WHITE, 10, 200)
        ball = Ball(WHITE,50, 50)
    elif difficulty == 3:
        paddleA = Paddle(WHITE, 10, 50)
        ball = Ball(WHITE, 5, 5)
    else:
        paddleA = Paddle(WHITE, 10, 100)
        ball = Ball(WHITE,10,10)

    paddleA.rect.x = 780
    paddleA.rect.y = 200
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

    lives = lives
    
    if difficulty == 1:
        paddleA = Paddle(WHITE, 10, 200)
        paddleB = Paddle(WHITE, 10, 200)
        ball = Ball(WHITE,50, 50)
        ballB = Ball(WHITE,50, 50)

    elif difficulty == 3:
        paddleA = Paddle(WHITE, 10, 50)
        paddleB = Paddle(WHITE, 10, 50)
        ball = Ball(WHITE, 5, 5)
        ballB = Ball(WHITE, 5, 5)
    else:
        paddleA = Paddle(WHITE, 10, 100)
        paddleB = Paddle(WHITE, 10, 100)
        ball = Ball(WHITE,10,10)
        ballB = Ball(WHITE,10,10)

    
    paddleA.rect.x = 20
    paddleA.rect.y = 200
    paddleB.rect.x = 780
    paddleB.rect.y = 200
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