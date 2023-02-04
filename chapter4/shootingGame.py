import pygame
import sys
import random

def showScore(score, x, y, screen):
    font = pygame.font.Font(None, 24)
    text = font.render('Score: ' + str(score).zfill(6), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    screen.blit(text, textRect)

pygame.init()
screen = pygame.display.set_mode((480, 640))

FPS = 30  # Frames Per Second
fpsClock = pygame.time.Clock()

asteroidtimer = 100

asteroids = [[20, 0, 0]] # x좌표, y좌표, 소행성 타입(0,1,2)

score = 0

try:
    spaceshipimg = pygame.image.load('./img/spaceship.png')
    asteroid0 = pygame.image.load('./img/asteroid00.png')
    asteroid1 = pygame.image.load('./img/asteroid01.png')
    asteroid2 = pygame.image.load('./img/asteroid02.png')
    asteroidimgs = (asteroid0, asteroid1, asteroid2)
    gameover = pygame.image.load('./img/gameover.jpg')

    takeoffsound = pygame.mixer.Sound('./audio/takeoff.wav')
    landingsound = pygame.mixer.Sound('./audio/landing.wav')
    takeoffsound.play()
except Exception as err:
    print('그림 또는 효과음 삽입에 문제가 있습니다', err)
    pygame.quit()
    sys.exit(0)


running = True
while running:
    fpsClock.tick(FPS)  # 프레임 제한(최소 사양)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 화면 종료(X) 클릭
            pygame.quit()
            sys.exit(0)

    screen.fill((255, 255, 255))  # 루프마다 화면을 초기화한다
    
    score += 1 # 매 프레임 마다 점수 누적
    showScore(score, 400, 10, screen)
    if score % 100 == 0:
        FPS += 2 # 난이도 상승

    position = pygame.mouse.get_pos()
    spaceshippos = (position[0] - 10, 600)
    screen.blit(spaceshipimg, spaceshippos)

    # 우주선의 경계(직사각형)
    spaceshipRect = pygame.Rect(spaceshipimg.get_rect())
    spaceshipRect.left = spaceshippos[0]
    spaceshipRect.top = spaceshippos[1]

    asteroidtimer -= 10
    if asteroidtimer <= 0:
        randomX = random.randint(5, 475)
        asteroidType = random.randint(0, 2)
        asteroids.append([randomX, 0, asteroidType])
        asteroidtimer = random.randint(50, 200)

    for index, stone in enumerate(asteroids):
        stone[1] += 10 # y좌표 10증가(낙하)

        if stone[1] > 640:
            asteroids.pop(index)

        # 소행성의 경계(충돌 여부 확인)
        stoneRect = pygame.Rect(asteroidimgs[stone[2]].get_rect())
        stoneRect.left = stone[0]
        stoneRect.top = stone[1]
        if stoneRect.colliderect(spaceshipRect):
            asteroids.pop(index)
            running = False

        screen.blit(asteroidimgs[stone[2]], (stone[0], stone[1]))

    pygame.display.flip()  # 화면에 변경 사항을 반영

    landingsound.play()

screen.blit(gameover, (0, 0))
showScore(score, screen.get_rect().centerx, screen.get_rect().centery, screen)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)