from scrabble import *
from string import ascii_uppercase
import pygame as py

py.init()

displayWidth = 800
displayHeight = 600

gameDisplay = py.display.set_mode((displayWidth, displayHeight))
py.display.set_caption("Scrabble")
clock = py.time.Clock()
crashed = False

scalex = 75
scaley = 75
letters = []

for i in ascii_uppercase:
    exec("tile" + i +  "= py.image.load(\'images/letter_" + i +".png\')")
    exec("tile" + i +  "= py.transform.scale(tile" + i + ", (scalex, scaley))")
    exec("letters.append(tile" + i + ")")

tile = py.image.load('images/letter.png')
tile = py.transform.scale(tile, (scalex, scaley))
letters.append(tile)

def A(x, y):
    gameDisplay.blit(tileA, (x, y))
def B(x, y):
    gameDisplay.blit(tileB, (x, y))
def C(x, y):
    gameDisplay.blit(tileC, (x, y))
def D(x, y):
    gameDisplay.blit(tileD, (x, y))
def E(x, y):
    gameDisplay.blit(tileE, (x, y))
def F(x, y):
    gameDisplay.blit(tileF, (x, y))
def G(x, y):
    gameDisplay.blit(tileG, (x, y))
def H(x, y):
    gameDisplay.blit(tileH, (x, y))
def I(x, y):
    gameDisplay.blit(tileI, (x, y))
def J(x, y):
    gameDisplay.blit(tileJ, (x, y))
def K(x, y):
    gameDisplay.blit(tileK, (x, y))
def L(x, y):
    gameDisplay.blit(tileL, (x, y))
def M(x, y):
    gameDisplay.blit(tileM, (x, y))
def N(x, y):
    gameDisplay.blit(tileN, (x, y))
def O(x, y):
    gameDisplay.blit(tileO, (x, y))
def P(x, y):
    gameDisplay.blit(tileP, (x, y))
def Q(x, y):
    gameDisplay.blit(tileQ, (x, y))
def R(x, y):
    gameDisplay.blit(tileR, (x, y))
def S(x, y):
    gameDisplay.blit(tileS, (x, y))
def T(x, y):
    gameDisplay.blit(tileT, (x, y))
def U(x, y):
    gameDisplay.blit(tileU, (x, y))
def V(x, y):
    gameDisplay.blit(tileV, (x, y))
def W(x, y):
    gameDisplay.blit(tileW, (x, y))
def X(x, y):
    gameDisplay.blit(tileX, (x, y))
def Y(x, y):
    gameDisplay.blit(tileY, (x, y))
def Z(x, y):
    gameDisplay.blit(tileZ, (x, y))
def blank(x, y):
    gameDisplay.blit(tile, (x, y))

x = 60
y = 450


game = Scrabble()
hand = game.get_hand()
possible_words = game.possible_words(hand)

gameDisplay.fill((255, 255, 255))

textx = 10
texty = 0

font = py.font.Font('freesansbold.ttf', 16)
text = font.render("Possible Words:", True, (0,0,0), (255, 255, 255))
gameDisplay.blit(text, (textx, texty))
texty = texty + 20
for i in game.blank_list:
    gameDisplay.blit(font.render((i), True, (0,0,0), (255, 255, 255)), (textx, texty))
    texty = texty + 20
    if texty > 400:
        texty = 20
        textx = textx + 100


while not crashed:
    for event in py.event.get():
        if event.type == py.QUIT:
            crashed = True

    while x < 750:
        for i in hand:
            if i in ascii_uppercase:
                exec(i + '(' + str(x) + ',' + str(y) + ')')
            else:
                exec('blank('+ str(x)+','+str(y)+')')
            
            x = x + 100
        
    py.display.update()
    clock.tick(60)

py.quit()
quit()