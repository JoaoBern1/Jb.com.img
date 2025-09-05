import pygame
import os

# Inicialização o Pygame
pygame.init()

# Definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela com Imagem")

# definindo a cor do fundo
BG_COLOR = (86, 58, 35) # Cor de Fundo ( um tom esscuro)

# Carregar a imagem
image_file = "Theo.png" # coloque o nome da sua imagem aqui
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha() # carregar imagem
    img_rect= img.get_rect(center=(WIDTH // 2, HEIGHT // 2)) # Centralizar a imagem
else:
    print("Imagem não econtrada!")

# Velocidade de movimento
SPEED = 1 # pixels por movimento

# Loop principal do jogo
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False 

# Pega as teclas pressionadas
keys = pygame.key.get_pressed()

# Movimentação da imgaem
if keys[pygame.K_LAFT]:


    # Preencher o fundo
    screen.fill(BG_COLOR)

    # Desenhar a imagem na tela
    screen.Blit(img, img_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()

