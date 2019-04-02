import pygame

pygame.init()

screen_width = 1000
screen_height = screen_width * 3 // 4
fps = 30

colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}

game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('My Game')
game_clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()


quit = False
while not quit:

	game_clock.tick(fps)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True

		print(event)


	## UPDATE 
	pygame.display.update()
	all_sprites.update()

	## DRAW
	game_display.fill(colors['white'])
	all_sprites.draw(game_display)

	game_display.blit(pygame.font.Font(None, 50).render('Please render me', True, colors['black']), (50, 50))

pygame.quit()
quit()