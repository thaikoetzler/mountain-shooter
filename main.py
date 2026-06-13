import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup Finish')

print('Loop Start')
while True:
    # Observação de todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Fechar a janela
            quit() # Finalizar pygame
