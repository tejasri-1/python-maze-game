import pygame
from pygame.locals import *
import maze_generation as m
import mouse_detec as detec
import level 
import portionview as pv
import buttons as bt

# Defining font and some useful colors
font1 = pygame.font.Font(None, 54)
font2= pygame.font.Font(None,45)
font3=pygame.font.Font(None,27)
font4 = pygame.font.Font(None,18)
WHITE=(255,255,255)
BLACK=(0,0,0)
GREY=(200,200,200)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)     

# this playing enables the gamers to play again , which repeart the entire code
playing=True
while playing==True:
    
    """Starting the pygame and creating a display.
    Next importing all the sounds and songs needed for the game.
    Importing all the images required for the game."""
    pygame.init()
    swidth=1200
    sheight=750
    screen = pygame.display.set_mode((swidth, sheight))
    pygame.display.set_caption("Maze through")  
                    
    bgm_music=pygame.mixer.music.load('BGM1.ogg')   
    pygame.mixer.music.play(-1)
    
    importwall=pygame.image.load("Wood2.jpg").convert_alpha()
    grass=pygame.image.load("Grass1.jpg")
    wallpaper=pygame.image.load("Wallpaper.jpeg")
    wallpaper=pygame.transform.scale(wallpaper,(swidth,sheight))
    loginwallpaper=pygame.image.load("Loginwallpaper.jpg")
    loginwallpaper=pygame.transform.scale(loginwallpaper,(swidth,sheight))
    wallpaper2=pygame.image.load("Chooselevel.jpeg")
    wallpaper2=pygame.transform.scale(wallpaper2,(swidth,sheight))
    chooselevelnum=pygame.image.load("choselevelnum.jpeg")
    chooselevelnum=pygame.transform.scale(chooselevelnum,(swidth,sheight))
    

    """Draw an entry screen which directs onto the login page"""
    bt.draw_page1(screen,wallpaper)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_RETURN: 
                    playing=bt.loginpage(screen,loginwallpaper)
                    running = False
                if event.key==K_ESCAPE:
                    playing = False
                    running= False
            if event.type == QUIT:
                playing = False
                running = False
    if playing == False:
        break
    
    
    """Saving the user input into a text based based on the button clicked
    And shifting to the new screen"""
    """Go to main level selection page after storing the information"""
    """ Choose level number is a background pic used which will display after choosing the main level asking to choose the sublevel"""
    bt.switch_page2(screen,wallpaper2)  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if bt.beginner.collidepoint(mouse_pos):
                    level.beglevel(screen,chooselevelnum)
                    grade=1
                    running=False
                elif bt.medium.collidepoint(mouse_pos):
                    level.medlevel(screen,chooselevelnum)
                    grade=2
                    running=False
                elif bt.advance.collidepoint(mouse_pos):
                    level.advlevel(screen,chooselevelnum)
                    grade=3
                    running=False
            if event.type == QUIT:
                playing=False
                running=False
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    playing=False
                    running=False
    if playing==False:
        break
    
    """ Choosing of sublevel in any of the selected main level Beginner, Medium, Advanced """
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                playing=False
                running=False
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                running=detec.detec_level(mouse_pos,grade,screen,importwall)
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    playing=False
                    running=False
    if playing==False:
        break           
                
    # Movement loop
    running = True
    if grade==1: 
        """ Bringing Redpanda as the player in the game """ 
        i=m.startx
        j=m.starty
        posx = i*m.dist
        posy = j*m.dist
        
        redpanda=pygame.image.load("Redpanda.png")
        redpanda=pygame.transform.scale(redpanda,(0.8*m.dist,0.8*m.dist))
        panda_rect=redpanda.get_rect()
        panda_rect.center = (posx+m.dist/2, posy+m.dist/2)   
        pygame.time.wait(5000) 
        copiedscreen = pygame.Surface(screen.get_size())
        copiedscreen.blit(screen, (0, 0))
        screen.blit(redpanda,panda_rect)
        screen=pygame.display.set_mode((int(6*m.dist)+200,int(4*m.dist)))
        swidth,sheight=screen.get_size()
        
        """ Setting the timer and keeping track of lives , 
        with detecting a life when player collides with the wall """
        lives=bt.font3.render("Lives:",True,RED)
        pygame.draw.circle(screen,RED,(0.9*swidth,30),10,10)
        pygame.draw.circle(screen,RED,(0.921*swidth,30),10,10)
        pygame.draw.circle(screen,RED,(0.942*swidth,30),10,10)
        screen.blit(lives,(1010,20))
        
        beforetime=pygame.time.get_ticks()
        timepassed=pygame.time.get_ticks()-beforetime
        timetext="Time Left:"+str(int(20-timepassed))
        timer=bt.font3.render(timetext,True,bt.BLUE)
        screen.blit(timer,(0.842*swidth,60))
        lives=3
        pygame.display.flip()
        if (int(100-timepassed/1000))==0:
            bt.timeup()
            running=False   
            
        while running:
            for event in pygame.event.get():   
                if event.type == QUIT:
                    playing=False
                    running = False
                elif i==m.endx and j==m.endy:
                    bt.gameover(screen)
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        playing=False
                        running=False
                    if event.key == K_DOWN:
                        if m.maze[j+1][i] == 0: 
                            panda_rect.move_ip(0,m.dist)
                            j+=1
                        elif m.maze[j+1][i]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,bt.WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,bt.WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1
                    elif event.key == K_UP:
                        if m.maze[j-1][i]==0:
                            panda_rect.move_ip(0,-m.dist)
                            j-=1
                        elif m.maze[j-1][i]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1
                    elif event.key == K_LEFT:
                        if m.maze[j][i-1]==0:
                            panda_rect.move_ip(-m.dist,0)
                            i -= 1
                        elif m.maze[j][i-1]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1
                    elif event.key == K_RIGHT:
                        if m.maze[j][i+1]==0:
                            panda_rect.move_ip(m.dist,0)
                            i += 1
                        elif m.maze[j][i+1]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1     
                posx = i*m.dist
                posy = j*m.dist
                screen.blit(redpanda,panda_rect)
                
            pv.gamescreen(screen,i,j,m.dist,grade,copiedscreen)             
            # updating the timer outside the events
            eraseoldtime=pygame.Rect(0.833*swidth,50,200,50)
            pygame.draw.rect(screen,WHITE,eraseoldtime)
            
            # writing current time left
            timepassed=pygame.time.get_ticks()-beforetime
            timetext="Time Left:"+str(int(20-timepassed/1000))
            timer=font3.render(timetext,True,BLUE)
            screen.blit(timer,(0.842*swidth,60))
            pygame.display.flip()
            if (int(20-timepassed/1000))==0 :
                running=False
                bt.timeup(screen)
            if lives==0:
                running=False
                bt.livesup(screen)
        if playing==False:
            running=False  
            break      
    elif grade==2: 
        """ Setting the timer and keeping track of lives , 
        with detecting a life when player collides with the wall """
        lives=bt.font3.render("Lives:",True,RED)
        pygame.draw.circle(screen,RED,(0.9*swidth,30),10,10)
        pygame.draw.circle(screen,RED,(0.921*swidth,30),10,10)
        pygame.draw.circle(screen,RED,(0.942*swidth,30),10,10)
        screen.blit(lives,(1010,20))
        
        beforetime=pygame.time.get_ticks()
        timepassed=pygame.time.get_ticks()-beforetime
        timetext="Time Left:"+str(int(20-timepassed))
        timer=bt.font3.render(timetext,True,bt.BLUE)
        screen.blit(timer,(0.842*swidth,60))
        lives=3
        pygame.display.flip()
        if (int(20-timepassed/1000))==0:
            bt.timeup()
            running=False   
            
        """ Bringing Redpanda as the player in the game """ 
        i=m.startx
        j=m.starty
        posx = i*m.dist
        posy = j*m.dist
        
        redpanda=pygame.image.load("Redpanda.png")
        redpanda=pygame.transform.scale(redpanda,(0.8*m.dist,0.8*m.dist))
        panda_rect=redpanda.get_rect()
        panda_rect.center = (posx+m.dist/2, posy+m.dist/2) 
        screen.blit(redpanda,panda_rect)       
         
        while running:
            for event in pygame.event.get():   
                if event.type == QUIT:
                    playing=False
                    running = False
                elif i==m.endx and j==m.endy:
                    bt.gameover(screen)
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        playing=False
                        running=False
                    if event.key == K_DOWN:
                        if m.maze[j+1][i] == 0: 
                            panda_rect.move_ip(0,m.dist)
                            j+=1
                        elif m.maze[j+1][i]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,bt.WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,bt.WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1
                    elif event.key == K_UP:
                        if m.maze[j-1][i]==0:
                            panda_rect.move_ip(0,-m.dist)
                            j-=1
                        elif m.maze[j-1][i]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1
                    elif event.key == K_LEFT:
                        if m.maze[j][i-1]==0:
                            panda_rect.move_ip(-m.dist,0)
                            i -= 1
                        elif m.maze[j][i-1]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1
                    elif event.key == K_RIGHT:
                        if m.maze[j][i+1]==0:
                            panda_rect.move_ip(m.dist,0)
                            i += 1
                        elif m.maze[j][i+1]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1     
                posx = i*m.dist
                posy = j*m.dist
                screen.blit(redpanda,panda_rect) 
                                        
            # updating the timer outside the events
            eraseoldtime=pygame.Rect(0.833*swidth,50,200,50)
            pygame.draw.rect(screen,WHITE,eraseoldtime)
            
            # writing current time left
            timepassed=pygame.time.get_ticks()-beforetime
            timetext="Time Left:"+str(int(100-timepassed/1000))
            timer=font3.render(timetext,True,BLUE)
            screen.blit(timer,(0.842*swidth,60))
            pygame.display.flip()
            if (int(100-timepassed/1000))==0 :
                running=False
                bt.timeup(screen)
            if lives==0:
                running=False
                bt.livesup(screen)
        if playing==False:
            running=False  
            break      
        
    elif grade==3: 
        """ Setting the timer and keeping track of lives , 
        with detecting a life when player collides with the wall """
        lives=bt.font3.render("Lives:",True,RED)
        pygame.draw.circle(screen,RED,(0.9*swidth,30),10,10)
        pygame.draw.circle(screen,RED,(0.921*swidth,30),10,10)
        pygame.draw.circle(screen,RED,(0.942*swidth,30),10,10)
        screen.blit(lives,(1010,20))
        
        beforetime=pygame.time.get_ticks()
        timepassed=pygame.time.get_ticks()-beforetime
        timetext="Time Left:"+str(int(20-timepassed))
        timer=bt.font3.render(timetext,True,bt.BLUE)
        screen.blit(timer,(0.842*swidth,60))
        lives=3
        pygame.display.flip()
        if (int(20-timepassed/1000))==0:
            bt.timeup()
            running=False   
            
        """ Bringing Redpanda as the player in the game """ 
        i=m.startx
        j=m.starty
        posx = i*m.dist
        posy = j*m.dist
        
        redpanda=pygame.image.load("Redpanda.png")
        redpanda=pygame.transform.scale(redpanda,(0.8*m.dist,0.8*m.dist))
        panda_rect=redpanda.get_rect()
        panda_rect.center = (posx+m.dist/2, posy+m.dist/2) 
        screen.blit(redpanda,panda_rect)       
         
        while running:
            for event in pygame.event.get():   
                if event.type == QUIT:
                    playing=False
                    running = False
                elif i==m.endx and j==m.endy:
                    bt.gameover(screen)
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        playing=False
                        running=False
                    if event.key == K_DOWN:
                        if m.maze[j+1][i] == 0: 
                            panda_rect.move_ip(0,m.dist)
                            j+=1
                        elif m.maze[j+1][i]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,bt.WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,bt.WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1
                    elif event.key == K_UP:
                        if m.maze[j-1][i]==0:
                            panda_rect.move_ip(0,-m.dist)
                            j-=1
                        elif m.maze[j-1][i]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1
                    elif event.key == K_LEFT:
                        if m.maze[j][i-1]==0:
                            panda_rect.move_ip(-m.dist,0)
                            i -= 1
                        elif m.maze[j][i-1]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1
                    elif event.key == K_RIGHT:
                        if m.maze[j][i+1]==0:
                            panda_rect.move_ip(m.dist,0)
                            i += 1
                        elif m.maze[j][i+1]==1:
                            print("One life lost")
                            if lives==3:
                                pygame.draw.circle(screen,WHITE,(0.942*swidth,30),10,10)
                            elif lives==2:
                                pygame.draw.circle(screen,WHITE,(0.921*swidth,30),10,10)
                            elif lives==1:
                                pygame.draw.circle(screen,WHITE,(0.9*swidth,30),10,10)
                            lives=lives-1     
                posx = i*m.dist
                posy = j*m.dist
                screen.blit(redpanda,panda_rect)                         
            # updating the timer outside the events
            eraseoldtime=pygame.Rect(0.833*swidth,50,200,50)
            pygame.draw.rect(screen,WHITE,eraseoldtime)
            
            # writing current time left
            timepassed=pygame.time.get_ticks()-beforetime
            timetext="Time Left:"+str(int(20-timepassed/1000))
            timer=font3.render(timetext,True,BLUE)
            screen.blit(timer,(0.842*swidth,60))
            pygame.display.flip()
            if (int(20-timepassed/1000))==0 :
                running=False
                bt.timeup(screen)
            if lives==0:
                running=False
                bt.livesup(screen)
        if playing==False:
            running=False  
            break      
               
    # after completion of that level, now the code either enters
    # 1. Gameover screen
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==quit():
                running=False
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if playagain.collidepoint(mouse_pos):
                    playing=True
                if exitgame.pygame.Rect.collidepoint(mouse_pos):
                    playing=False
    # 2. Livesup screen
    # 3. Timeup screen        
    
pygame.quit()