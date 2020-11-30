import pygame
from pygame.locals import *
from pygame import mixer
pygame.init()

class Button:
    def __init__(self, color, x, y, width, height, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    def draw(self, display):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.SysFont('arial', 16)
            text = font.render(self.text, 1, (202, 103, 145))
            display.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    def over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

class Entity:
    def __init__(self):
        pass
    def draw(self, i):
        pass
    def update(self):
        pass
    def pause(self):
        pass
    def reset(self, x, y, z):
        pass
    
class Ship(Entity):
    def __init__(self, x, y, z, display):
        self.Shuttle_X = x
        self.Shuttle_Y = y
        self.Shuttle_Z = z
        self.velocity = 2
        self.change = 0
        self.surface = display
    def draw(self, i):
        pygame.draw.polygon(self.surface, (200, 250, 255),[(self.Shuttle_X, i-30), (self.Shuttle_Y, i-50), (self.Shuttle_Z, i-30)])
    def moveleft(self):
        self.change -= self.velocity
    def moveright(self):
        self.change += self.velocity
    def stopleft(self):
        self.change += self.velocity
    def stopright(self):
        self.change -= self.velocity
    def update(self):
        self.Shuttle_X += self.change
        self.Shuttle_Y += self.change
        self.Shuttle_Z += self.change
        if self.Shuttle_X < 10:
            self.Shuttle_X = 10
            self.Shuttle_Y = 30
            self.Shuttle_Z = 50
        if self.Shuttle_Z > 710:
            self.Shuttle_X = 670
            self.Shuttle_Y = 690
            self.Shuttle_Z = 710
    def reset(self, x, y, z):
        self.Shuttle_X = x
        self.Shuttle_Y = y
        self.Shuttle_Z = z
        
mixer.music.load("DarkCity.wav")
#mixer.music.load("NightDweller.wav")
#mixer.music.load("Rebels.wav")
#mixer.music.load("Inception.wav")
pygame.mixer.music.play()
#mixer.music.queue("DarkCity.wav")
#mixer.music.queue("NightDweller.wav")
mixer.music.queue("Rebels.wav")
#mixer.music.queue("Inception.wav")


pygame.display.set_caption("CybrPnK")
icon = pygame.image.load('retro.png')
pygame.display.set_icon(icon)

gameExit = False
clock = pygame.time.Clock()
i=720
state = 0
surface = pygame.display.set_mode((i,i))
g = 'Adventure'
pause = 0
back = 0
music = True

darkerblue = (2, 9, 35)
darkblue = (0, 17, 61)
violet = (53, 20, 108)
blue = (0, 50, 251)
celestite = (200, 250, 255)
neonpink = (202, 103, 145)
neonorange = (255, 131, 0)


button = Button(violet, 240, 240, 240, 60, 'Play')
button2 = Button(violet, 240, 400, 240, 60, 'Settings')
button3 = Button(violet, 240, 480, 240, 60, 'Quit')
button4 = Button(violet, 240, 240, 240, 60, 'Continue')
button5 = Button(violet, 240, 320, 240, 60, 'Main Menu')
button6 = Button(violet, 240, 320, 240, 60, 'Gamemode')
button7 = Button(violet, 480, 320, 120, 60, 'Adventure')
button8 = Button(violet, 480, 380, 120, 60, 'Multiplayer')
button9 = Button(violet, 240, 440, 240, 60, 'Music')
button10 = Button(violet, 240, 320, 240, 60, 'Back')

ship = Ship(i/2-20, i/2, i/2+20, surface)
ship2 = Ship(i/2-20, i/2, i/2+20, surface)
entities = []

while not gameExit:
    if state == 0:
        surface.fill(pygame.Color(darkblue))
        button.draw(surface)
        button2.draw(surface)
        button3.draw(surface)
        button6.draw(surface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.over(pos):
                    if g == 'Adventure':
                        entities.append(ship)
                        state = 3
                    elif g == 'MultiPl':
                        entities.append(ship)
                        entities.append(ship2)
                        state = 4
                elif button2.over(pos):
                    back = state
                    state = 2
                elif button3.over(pos):
                    gameExit = True
                if button6.over(pos):
                    state = 1
            if event.type == pygame.MOUSEMOTION:
                if button.over(pos):
                    button.color = neonorange
                else:
                    button.color = violet
                if button2.over(pos):
                    button2.color = neonorange
                else:
                    button2.color = violet
                if button3.over(pos):
                    button3.color = neonorange
                else:
                    button3.color = violet
                if button6.over(pos):
                    button6.color = neonorange
                else:
                    button6.color = violet
    elif state == 1: 
        button7.draw(surface)
        button8.draw(surface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button7.over(pos):
                    g = 'Adventure'
                elif button8.over(pos):
                    g = 'MultiPl'
                state = 0
            if event.type == pygame.MOUSEMOTION:
                if button7.over(pos):
                    button7.color = neonpink
                else:
                    button7.color = blue
                if button8.over(pos):
                    button8.color = neonpink
                else:
                    button8.color = blue
    elif state == 2:
        surface.fill(pygame.Color(darkblue))
        button10.draw(surface)
        button9.draw(surface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button10.over(pos):
                    state = back
                if button9.over(pos):
                    music = not music
                    if music == False:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)
            if event.type == pygame.MOUSEMOTION:
                if button10.over(pos):
                    button10.color = neonorange
                else:
                    button10.color = violet
                if button9.over(pos):
                    button9.color = neonorange
                else:
                    button9.color = violet
    elif state == 3:
        surface.fill(pygame.Color(darkblue))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = 3
                    state = 5
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    ship.moveleft()
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    ship.moveright()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    ship.stopleft()
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    ship.stopright()
        if entities is not None:
            for entity in entities:
                entity.update()
                entity.draw(i)
    elif state == 4:
        surface.fill(pygame.Color(darkblue))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = 4
                    state = 5
                if event.key == pygame.K_a:
                    ship.moveleft()
                if event.key == pygame.K_LEFT:
                    ship2.moveleft()
                if event.key == pygame.K_d:
                    ship.moveright()
                if event.key == pygame.K_RIGHT:
                    ship2.moveright()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    ship.stopleft()
                if event.key == pygame.K_d:
                    ship.stopright()
                if event.key == pygame.K_LEFT:
                    ship2.stopleft()
                if event.key == pygame.K_RIGHT:
                    ship2.stopright()
        if entities is not None:
            for entity in entities:
                entity.update()
                entity.draw(i)
    if state == 5:
        surface.fill(pygame.Color(darkerblue))
        button4.draw(surface)
        button5.draw(surface)
        button3.draw(surface)
        button2.draw(surface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = pause
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button4.over(pos):
                    state = pause
                if button5.over(pos):
                    entity.reset(i/2-20, i/2, i/2+20)
                    entities.clear()
                    state = 0
                if button2.over(pos):
                    back = state
                    state = 2
                if button3.over(pos):
                    gameExit = True
            if event.type == pygame.MOUSEMOTION:
                if button4.over(pos):
                    button4.color = neonorange
                else:
                    button4.color = violet
                if button5.over(pos):
                    button5.color = neonorange
                else:
                    button5.color = violet
                if button2.over(pos):
                    button2.color = neonorange
                else:
                    button2.color = violet
                if button3.over(pos):
                    button3.color = neonorange
                else:
                    button3.color = violet
    pygame.display.update()
    clock.tick(128)