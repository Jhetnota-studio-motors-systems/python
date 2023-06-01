import pygame
import sys
import random



pygame.init()
obraz = pygame.display.set_mode((960,720))

iveta = pygame.image.load('skicar/icon.png')
tablulka = pygame.image.load("skicar/bula1.png")
play = pygame.image.load("skicar/p.png")
sk = pygame.image.load("skicar/sk.png")
sl = pygame.image.load("skicar/sl.jpg")
r = pygame.image.load("skicar/r.png")
f = pygame.image.load("skicar/f.png")
x = pygame.image.load("skicar/X.png")
t = pygame.image.load("skicar/Tick.png")

vlajky = [sk,]
vlajky2 = [sl,]
vlajky3 = [r,]
vlajky4 = [f,]

vlajkyy = random.choice(vlajky)
vlajkyy2 = random.choice(vlajky2)
vlajkyy3 = random.choice(vlajky3)
vlajkyy4 = random.choice(vlajky4)

pygame.display.set_caption("Jesus Quiz")
pygame.display.set_icon(iveta) 
fpsl = pygame.time.Clock()

class tlacidlo():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.stlacene = True

	def draw(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.stlacene == True:
				self.stlacene = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.stlacene = True

		#draw button on screen
		obraz.blit(self.image, (self.rect.x, self.rect.y))

		return action

s = "Slovakia"
f = "France"
r = "Russia"
sl = "Slovenia"
pius = ["Slovakia","France","Russia","Slovenia"]

neviditelna = (0, 0, 0, 0)
bila = (255,255,255)

piuss = random.choice(pius)
font = pygame.font.Font("prst.ttf", 40)
text = font.render(piuss, True, bila)
textrect = text.get_rect()
textrect.center = (470,100)    

play_button = tlacidlo(57,320,vlajkyy,0.6)
play_button2 = tlacidlo(290,320,vlajkyy2,0.6)
play_button3 = tlacidlo(520,320,vlajkyy3,0.6)
play_button4 = tlacidlo(740,320,vlajkyy4,0.6)

run = True
while run:

	obraz.blit(tablulka,(0,0))
	for picka in pygame.event.get():
		if picka.type == pygame.QUIT:
			pygame.quit()
			exit()

		
	obraz.blit(text,textrect)

	if play_button2.draw() and piuss == "Slovenia":
		obraz.blit(t,(480,580))	

	if play_button3.draw() and piuss == "Russia":
		obraz.blit(t,(480,580))	

	if play_button4.draw() and piuss == "France":	
		obraz.blit(t,(480,580))	

	if play_button.draw() and piuss == "Slovakia":		
			obraz.blit(t,(480,580))

	pygame.display.update()
	fpsl.tick(60)