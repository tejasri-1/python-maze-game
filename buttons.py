import pygame

# Defining font and some useful colors
font1 = pygame.font.Font(None,73)
font2= pygame.font.Font(None,45)
font3=pygame.font.Font(None,27)
font4 = pygame.font.Font(None,18)

# Basic Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Main Headings to be placed
head1 = font1.render("Welcome to the Maze World!", True, YELLOW)
head3 = font1.render("Select level",True,WHITE)
footer1 = font2.render("Click ESC to exit game",True,WHITE)

""" Class defined for storing inputs related to the login page
And handling the events while typing the login information"""
class TextInput:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLUE
        self.text = ""
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = GREEN if self.active else BLUE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = BLUE
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        pygame.display.flip()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = font2.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))


""" The first entry page of the pygame """
def draw_page1(screen,wallpaper):
    swidth,sheight=screen.get_size()
    screen.blit(wallpaper,(0,0))
    screen.blit(head1, (0.23*swidth,0.16*sheight))
    button1_text = font2.render("PRESS ENTER TO GET STARTED", True, YELLOW)
    screen.blit(button1_text,(0.28*swidth,0.45*sheight))
    screen.blit(footer1,(0.36*swidth,0.67*sheight))
    pygame.display.flip()

""" After entering the game it redirects into login page , following is its contruction """
def loginpage(screen,loginwallpaper):
    
    swidth,sheight=screen.get_size()
    screen.fill(BLACK)
    screen.blit(loginwallpaper,(0,0))
    
    username_input = TextInput(0.542*swidth, 0.27*sheight, 200, 40)
    password_input = TextInput(0.542*swidth, 0.4*sheight, 200, 40)
    
    # Draw input labels
    username_label = font2.render("Username:", True, WHITE)
    screen.blit(username_label, (0.37*swidth, 220 - font2.get_height() // 2))
    password_label = font2.render("Password:", True, WHITE)
    screen.blit(password_label, (0.37*swidth, 320 - font2.get_height() // 2))
           
    # Draw login button
    login_button = pygame.Rect(0.433*swidth, 400,0.17*swidth, 50)
    pygame.draw.rect(screen, RED, login_button)
    login_label = font2.render("Login", True, BLACK)
    screen.blit(login_label, (0.483*swidth, 415))

    # Draw registration button
    register_button = pygame.Rect(0.433*swidth, 475,0.17*swidth, 50)
    pygame.draw.rect(screen, RED, register_button)
    register_label = font2.render("Register", True, BLACK)
    screen.blit(register_label, (0.47*swidth, 490))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                if register_button.collidepoint(mouse_pos):
                    with open("login_data.txt", "a") as file:
                        file.write(f"Username: {username_input.text}\n")
                        file.write(f"Password: {password_input.text}\n")
                        running=False
                        return True
                if login_button.collidepoint(mouse_pos):
                    with open('filename.txt', 'r') as file:
                        file_contents = file.read()
                        running=False
                        return True
            username_input.handle_event(event)
            password_input.handle_event(event)  
        username_input.draw(screen)        
        password_input.draw(screen)
        pygame.display.flip()
    
    
##### buttons - at the page 2
def switch_page2(screen,wallpaper2):
    swidth,sheight=screen.get_size()
    global beginner,medium,advance
    screen.fill(BLACK)
    screen.blit(wallpaper2,(0,0))
    beginner = pygame.Rect(swidth/6-50, 450, 100, 50)
    medium = pygame.Rect(swidth/2-50, 450, 100, 50)
    advance = pygame.Rect(5*swidth/6-50, 450, 100, 50)
    pygame.draw.rect(screen, GREY, beginner)
    pygame.draw.rect(screen, GREY, medium)
    pygame.draw.rect(screen, GREY, advance)
    beginner_text = font3.render("Beginner",True,BLACK)
    screen.blit(beginner_text,(swidth/6-40,460))
    medium_text = font3.render("Medium",True,BLACK)
    screen.blit(medium_text,(swidth/2-40,460))
    advance_text = font3.render("Advance",True,BLACK)
    screen.blit(advance_text,(5*swidth/6-40,460))
    screen.blit(footer1,(515,600))
    pygame.display.flip()
    
# GAME OVER WINDOW
def gameover(screen):
    swidth,sheight=screen.get_size()
    running=True
    while running:
        screen.fill(BLACK)
        head4 = font1.render("GAME OVER!",True,WHITE)
        screen.blit(head4,(0.42*swidth,0.133*sheight))
        # keeping play again button for restarting the game
        playagain = pygame.Rect(0.45*swidth,0.4*sheight,0.17*swidth,0.11*sheight)
        pygame.draw.rect(screen,GREY,playagain)
        playagain_text = font3.render("Play Again",True,BLACK) 
        screen.blit(playagain_text,(0.492*swidth,0.433*sheight))
        pygame.display.flip() 
        
# Timeup window
def timeup(screen):
    swidth,sheight=screen.get_size()
    running=True
    while running:
        screen.fill(BLACK)
        head6 = font1.render("TIME UP!",True,WHITE)
        screen.blit(head6,(0.42*swidth,0.133*sheight))
        # keeping play again button for restarting the game
        playagain = pygame.Rect(0.45*swidth,0.4*sheight,0.17*swidth,0.11*sheight)
        pygame.draw.rect(screen,GREY,playagain)
        playagain_text = font3.render("Play Again",True,BLACK) 
        screen.blit(playagain_text,(0.492*swidth,0.433*sheight))
        pygame.display.flip() 
        
# Livesup window
def livesup(screen):
    swidth,sheight=screen.get_size()
    running=True
    while running:
        screen.fill(BLACK)
        head6 = font1.render("Sorry, No lives..",True,WHITE)
        screen.blit(head6,(0.42*swidth,0.133*sheight))
        # keeping play again button for restarting the game
        playagain = pygame.Rect(0.45*swidth,0.4*sheight,0.17*swidth,0.11*sheight)
        pygame.draw.rect(screen,GREY,playagain)
        playagain_text = font3.render("Play Again",True,BLACK) 
        screen.blit(playagain_text,(0.492*swidth,0.433*sheight))
        pygame.display.flip() 
            
