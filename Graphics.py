import pygame, sys

pygame.init()
Surface = pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption("Mirror Test")
Surface.fill((120,120,120))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
