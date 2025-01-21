import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Jeu de collecte")

# Chargement des ressources
player = pygame.image.load("player.png")  # Image du joueur
player_rect = player.get_rect()
player_rect.x = window_width // 2
player_rect.y = window_height - player_rect.height
player_speed = 8

object = pygame.image.load("object.png")  # Image des objets
object = pygame.transform.scale(object, (50, 50))  # Redimensionner à 50x50 pixels
object_rect = object.get_rect()

# Vérifiez que l'objet rentre dans la fenêtre
if object_rect.width > window_width:
    raise ValueError("La largeur de l'objet dépasse la largeur de la fenêtre.")
if object_rect.height > window_height:
    raise ValueError("La hauteur de l'objet dépasse la hauteur de la fenêtre.")

object_rect.x = random.randint(0, window_width - object_rect.width)
object_rect.y = 0
object_speed = 4

# Variables de jeu
score = 0
font = pygame.font.SysFont('Arial', 36)
clock = pygame.time.Clock()

# Boucle principale
running = True
while running:
    # Limite la vitesse de la boucle (FPS)
    clock.tick(30)

    # Remplissage de l'arrière-plan
    screen.fill((0, 0, 0))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouvement du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.x < window_width - player_rect.width:
        player_rect.x += player_speed

    # Mise à jour des objets
    object_rect.y += object_speed
    if object_rect.y > window_height:
        # Fin de la partie si l'objet touche le bas de l'écran
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.fill((0, 0, 0))
        screen.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)  # Attendre 3 secondes avant de quitter
        running = False

    # Vérification des collisions
    if player_rect.colliderect(object_rect):
        score += 1
        object_speed += 0.5  # Augmente la vitesse de l'objet
        object_rect.y = 0
        object_rect.x = random.randint(0, window_width - object_rect.width)

    # Affichage des éléments
    screen.blit(player, player_rect)
    screen.blit(object, object_rect)

    # Affichage du score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Mise à jour de l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
