import pygame

import os

 

# These are the dimensions of the background image for our game

screenLength = 800

screenHeight = 427 

dim_field = (screenLength, screenHeight)



def main():
    #------screen set up-----#
    screen = pygame.display.set_mode(dim_field)
    clock = pygame.time.Clock()
    background = pygame.image.load(os.path.join("assets","background.jpg"))
    background = pygame.transform.scale(background, dim_field)

    playerSprite = pygame.image.load(os.path.join("assets", "playerSprite.png")).convert()
    playerSprite.set_colorkey((101, 141, 209))

    flagSprite = pygame.image.load(os.path.join('assets','flagSprite.png'))
    
    flagSprite = pygame.transform.scale(flagSprite, (50,50))

    #----Player Mechanics----#
    
    # Location 1
    platforms = []
    flagList = []
    rect_player = pygame.Rect(200, 200, 24, 26)
    rect_platform1 = pygame.Rect(200,250,300,5)
    rect_platform2 = pygame.Rect(200,180,300,5)
    rect_flag = pygame.Rect(600,200,50,50)
    flagList.append(rect_flag)
    platforms.append(rect_platform1)
    platforms.append(rect_platform2)


    FPS = 60
    stepSize = 12
    running = True
    isJumping = False
    isGrounded = False
    isFalling = True
    while running:
        clock.tick(FPS)

        keys = pygame.key.get_pressed() #list of keys that are being pressed
        for event in pygame.event.get():
            # Quit game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    print("Quit game")
                if isGrounded:
                    if event.key == pygame.K_SPACE:
                        isJumping = True
                        print("yeet")

                
                #Horiz Mvmt
                #if event.key == pygame.K_d:#move right
            
            #while rect_player.left >=0 and rect_player.right <= screenLength:

            
            if keys[pygame.K_d]:
                rect_player.move_ip(stepSize,0)
                #if event.key == pygame.K_a:#move left
            if keys[pygame.K_a]:
                rect_player.move_ip(-stepSize,0)
            '''if keys[pygame.K_s]:
                rect_player.move_ip(0,stepSize)
                #if event.key == pygame.K_a:#move left
            if keys[pygame.K_w]:
                rect_player.move_ip(0,-stepSize)'''


            #if isGrounded:
                #if keys[ pygame.K_SPACE]:
                    #isJumping = True
                #isFalling = False
            if isGrounded:
                if rect_player.collidelist(platforms) == -1:
                    isFalling = True
                    isGrounded = False
            if isFalling:
                fall(rect_player,6)
                if rect_player.collidelist(platforms) != -1:
                    isGrounded = True
                    isFalling = False
            
            if isJumping:#Player Jumping Mechanics
                jump(rect_player)
                isFalling = True
                isJumping = False
            '''
                rect_player.move_ip(0,-10)
                jumpCounter += 1
                isGrounded = False
                if jumpCounter == 10:
                    isJumping = False
                    isFalling = True
                    jumpCounter = 0
            '''
        
                     
        
        if rect_player.left <= 0:
            rect_player.move_ip(stepSize,0)
        if rect_player.right >= screenLength:
            rect_player.move_ip(-stepSize,0)
        if rect_player.bottom >= screenHeight:
            #rect_player.move_ip(0,-3)
            jump(rect_player)
            running = False
            print("rip")
        if rect_player.top <= 0:
            rect_player.move_ip(0,3)
        

        if rect_player.colliderect(rect_flag): 
            running = False
            print("poggers")

        screen.blit(background, (0,0)) 
        #pygame.draw.rect(screen, (255,0,0), rect_player)

        screen.blit(playerSprite, rect_player)
        screen.blit(flagSprite,rect_flag)
        
        for a in range(len(platforms)):
            pygame.draw.rect(screen, (255,255,0), platforms[a])
        pygame.display.update()

def jump(rect):
    for jumpCounter in range(10):
        rect.move_ip(0,-5)
        jumpCounter += 1
    

def fall(rect,stepsizeY):
    rect.move_ip(0,stepsizeY)

if __name__ ==  '__main__':
    main()
