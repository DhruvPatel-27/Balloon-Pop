import pygame, random

#Pygame Global Variables
WIDTH, HEIGHT = (1280, 720)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60 #frames per second of the game

def init():
    initColour()
    timer()
    loadBalloon()
    initScore()
    initLives()
    initSound()
    initLevel()

def initColour():
    global WHITE, BLACK, GREEN, RED, BLUE, TURQUOISE
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (51, 255, 51)
    RED = (255, 51, 51)
    BLUE = (51, 153, 255)
    TURQUOISE = (51, 255, 255)

def timer():
    global timer, fontTimer
    timer = 5.0
    fontTimer = pygame.font.SysFont("Comic Sans ms", 20)

def loadBalloon():
    global balloons, randIndex, xLocation, yLocation
    balloons = []
    randIndex = random.randint(0, 6) #used to change colours of the balloon
    xLocation = 200
    yLocation = 200

    balloon = pygame.image.load("blueballoon.png")
    balloons.append(balloon)                            #adds to the list
    balloon = pygame.image.load("greenballoon.png")
    balloons.append(balloon)
    balloon = pygame.image.load("brownballoon.png")
    balloons.append(balloon)
    balloon = pygame.image.load("yellowballoon.png")
    balloons.append(balloon)
    balloon = pygame.image.load("orangeballoon.png")
    balloons.append(balloon)
    balloon = pygame.image.load("darkballoon.png")
    balloons.append(balloon)
    balloon = pygame.image.load("redballoon.png")
    balloons.append(balloon)

def initScore():
    global score, font
    score = 0
    font = pygame.font.SysFont("Comic Sans ms", 20)

def initLives():
    global lives, fontLives
    lives = 3
    fontLives = pygame.font.SysFont("Comic Sans ms", 20)

def initSound():
    global popSound
    popSound = pygame.mixer.Sound("balloonpop.wav")


def initLevel():
    global level, fontLevel
    level = 1
    fontLevel = pygame.font.SysFont("Comic Sans ms", 20)


def update():
    '''This function is used to modify the data portions of things shown on screen'''
    updateTimerNLives()
    updateLevel()
    updateBalloonColour()


def updateTimerNLives():
    global timer, isRunning, lives, xLocation, yLocation
    timer = timer - 1/60
    if timer <= 0:
        xLocation = random.randint(100, 1200)
        yLocation = random.randint(100, 600)
        resetClockNLevel1_10()
        resetClockNLevel11_20()
        resetClockNLevel21_30()
        resetClockNLevel31_45()
        lives = lives - 1
    if lives == 0:
        isRunning = False


def updateLevel():
    global level, score
    if score % 3 == 0:
       level = 1 + (score//3)


def updateBalloonColour():
    global balloonImg
    balloonImg = balloons[randIndex]


def resetClockNLevel1_10():
    global timer
    if level == 1:
        timer = 5.0
    if level == 2:
        timer = 4.5
    if level == 3:
        timer = 4.1
    if level == 4:
        timer = 3.6
    if level == 5:
        timer = 3.3
    if level == 6:
        timer = 3.0
    if level == 7:
        timer = 2.7
    if level == 8:
        timer = 2.4
    if level == 9:
        timer = 2.2
    if level == 10:
        timer = 1.9

def resetClockNLevel11_20():
    global timer
    if level == 11:
        timer = 1.7
    if level == 12:
        timer = 1.6
    if level == 13:
        timer = 1.4
    if level == 14:
        timer = 1.3
    if level == 15:
        timer = 1.1
    if level == 16:
        timer = 1.0
    if level == 17:
        timer = 0.9
    if (level == 18) or (level == 19):
        timer = 0.8
    if level == 20:
        timer = 0.7

def resetClockNLevel21_30():
    global timer
    if level == 21:
        timer = 0.6
    if (level == 22) or (level == 23):
        timer = 0.5
    if (level == 24) or (level == 25) or (level == 26):
        timer = 0.4
    if (level == 27) or (level == 28) or (level == 29):
        timer = 0.3
    if level == 30:
        timer = 0.2

def resetClockNLevel31_45():
    global timer, isRunning
    if (level == 31) or (level == 32) or (level == 33) or (level == 34):
        timer = 0.2
    if (level == 35) or (level == 36) or (level == 37) or (level == 38) or (level == 39) or (level == 40) or (level == 41) or (level == 42) or (level == 43) or (level == 44):
        timer = 0.1
    if level == 45:
        isRunning = False


def draw():
    pygame.draw.rect(SCREEN, BLACK, (0, 0, WIDTH, HEIGHT))
    drawBalloon()
    drawScore()
    drawLives()
    drawLevel()
    drawClock()
    pygame.display.flip()

def drawBalloon():
    SCREEN.blit(balloonImg, (xLocation, yLocation))

def drawScore():
    scoreImg = font.render("Score: " + str(score), True, GREEN)
    SCREEN.blit(scoreImg, (20, 20))

def drawLives():
    livesImg = fontLives.render("Lives: " + str(lives), True, RED)
    SCREEN.blit(livesImg, (20, 40))


def drawLevel():
    levelImg = fontLevel.render("Level: " + str(level), True, BLUE)
    SCREEN.blit(levelImg, (20, 60))

def drawClock():
    timeImg = fontTimer.render("Timer: " + str(format(timer, ".1f")), True, TURQUOISE)
    SCREEN.blit(timeImg, (20, 80))


def reset():
    global mousex, mousey, xLocation, yLocation, score, timer, balloonImg, randIndex
    mousex, mousey = pygame.mouse.get_pos()
    if xLocation <= mousex <= xLocation + 46 and yLocation <= mousey <= yLocation + 63:
        print("found the balloon")
        popSound.play()
        score = score + 1
        xLocation = random.randint(100, 1200)  #changes the x value randomly
        yLocation = random.randint(100, 600)   #changes the y value randomly
        randIndex = random.randint(0, 6)      #changes the balloon colour randomly each time the balloon is popped
        resetClockNLevel1_10()
        resetClockNLevel11_20()
        resetClockNLevel21_30()
        resetClockNLevel31_45()
    else:
        print("no balloon here")


def main():
    global gameState, isRunning
    pygame.init()
    init()
    isRunning = True #this variable controls whether the game runs or not
    clock = pygame.time.Clock()

    while isRunning:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                '''changes position & colour of balloon, adds score, plays a sound if a balloon pops, and resets the timer if a balloon pops'''
                reset()

        update()
        draw()
    pygame.quit()

if __name__ == "__main__":
    main()