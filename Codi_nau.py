import time
from pygame.locals import *
import pygame


AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fondo.png'
WHITE = (255,255,255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
RED = (255,0,0)
GREEN = (51,153,102)
BLUE = (0,0,255)
INDIGO = (75, 0, 130)
VIOLET = (115, 49, 152)
VIOLET2 = (66, 35, 87)
GREY = (128,128,128)
MARRON = (128,0,0)
BLACK = (0,0,0)
OLIVE = (134,139,73)
CYAN = (0,255,255)
PINK = (255,163,177)
TAN = (210,180,140)
TEAL = (0,128,128)
guanyador = 0
bala1_imatge = pygame.image.load('assets/bala1.png')
bala2_imatge = pygame.image.load('assets/bala2.png')


# Pantalles del Joc2
# Pantalla 1 - Menú
# Pantalla 2 - Crèdits
# Pantalla 3 - Joc
# Pantalla 4 - Game Over

pantalla_actual = 1

pygame.init()
pygame.mixer.music.load('assets/music.mp3')
pygame.mixer.music.play()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Joc de naus")  # Arcade

# Variables globales para explosiones (partículas)
explosions = []
bullet_speed = 5
special_bullet_speed = 7
shot_cooldown = 225
winner = 0
current_screen = 1


# Jugador 1:
player_image = pygame.image.load('assets/nave_espacial.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 5


# Jugador 2:
player_image2 = pygame.image.load('assets/nave_enemiga.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 5

# vides:
vides_jugador1 = 6
vides_jugador2 = 6
vides_jugador1_image = pygame.image.load('assets/vida2.png')
vides_jugador2_image = pygame.image.load('assets/vida1.png')


# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(MAGENTA) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 5
temps_entre_bales = 225 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2

# Proyectil especial jugador 1 (tecla E)
                if event.key == K_e and not player1_special_used and player1_special_bullet is None:
                    player1_special_bullet = pygame.Rect(player1_rect.centerx - 5, player1_rect.top, 10, 20)
                    player1_special_used = True
                # Proyectil especial jugador 2 (tecla L)
                if event.key == K_l and not player2_special_used and player2_special_bullet is None:
                    player2_special_bullet = pygame.Rect(player2_rect.centerx - 5, player2_rect.bottom - 20, 10, 20)
                    player2_special_used = True

pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 60

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))


def show_menu():
    imprimir_pantalla_fons("assets/menuA.png")
    text1 = "1. Començar partida"
    text2 = "2. Veure crèdits"
    text3 = "3. Sortir"
    font1 = pygame.font.SysFont(None, 50)
    img1 = font1.render(text1, True, BLACK)
    img2 = font1.render(text2, True, BLACK)
    img3 = font1.render(text3, True, RED)
    pantalla.blit(img1, (248, 275))
    pantalla.blit(img2, (248, 365))
    pantalla.blit(img3, (248, 460))

def show_credits():
    imprimir_pantalla_fons("assets/credit.png")
    text1 = "Programació:"
    text2 = "Gràfics:"
    text3 = "Música:"
    text4 = "Sons:"
    text5 = "Joel de los Santos"
    text6 = "El Señor de la Noche - Don Omar"
    text7 = "Freesound.org"
    font1 = pygame.font.SysFont(None, 60)
    font2 = pygame.font.SysFont(None, 50)
    img1 = font1.render(text1, True, VIOLET)
    img2 = font1.render(text2, True, VIOLET)
    img3 = font1.render(text3, True, VIOLET)
    img4 = font1.render(text4, True, VIOLET)
    img5 = font2.render(text5, True, PINK)
    img6 = font2.render(text6, True, PINK)
    img7 = font2.render(text7, True, PINK)
    pantalla.blit(img1, (60, 215))
    pantalla.blit(img5, (160, 265))
    pantalla.blit(img2, (60, 315))
    pantalla.blit(img5, (160, 365))
    pantalla.blit(img3, (60, 415))
    pantalla.blit(img6, (160, 465))
    pantalla.blit(img4, (60, 515))
    pantalla.blit(img7, (160, 565))

while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        #crèdits
        if pantalla_actual == 2:
            show_credits()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pantalla_actual = 1

        #menu
        if pantalla_actual == 1:
            if event.type == KEYDOWN:
                if event.key == K_3:
                    pygame.quit()
                if event.key == K_1:
                    pantalla_actual = 3
                if event.key == K_2:
                    pantalla_actual = 2

        if pantalla_actual == 3:
            # controlar trets de les naus
            if event.type == KEYDOWN:
                #jugador 1
                if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time
                # jugador 2
                if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time

        if pantalla_actual == 4:
            for i in bales_jugador1:
                bales_jugador1.remove(i)
            for i in bales_jugador2:
                bales_jugador2.remove(i)
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    vides_jugador1 = 6
                    vides_jugador2 = 6
                    pantalla_actual = 1


    if pantalla_actual == 4:
        imprimir_pantalla_fons("assets/gameover.png")
        text = "Player " + str(guanyador) + " Wins!"
        font = pygame.font.SysFont(None, 100)
        img = font.render(text, True, WHITE)
        pantalla.blit(img,(150,40))

    if pantalla_actual == 1:
        show_menu()

    if pantalla_actual == 3:
        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_LEFT]:
            player_rect2.x -= velocitat_nau2
        if keys[K_RIGHT]:
            player_rect2.x += velocitat_nau2



        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())

        #dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        #Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1: # bucle que recorre totes les bales
            bala.y -= velocitat_bales # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_jugador1.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala2_imatge, bala)
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 1!")
                bales_jugador1.remove(bala)  # eliminem la bala
                vides_jugador2 = vides_jugador2 -1
                print("vides jugador 2:", vides_jugador2)
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala1_imatge, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 2!")
                bales_jugador2.remove(bala)  # eliminem la bala
                vides_jugador1 = vides_jugador1 - 1
                print("vides jugador 1:",vides_jugador1)
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)


        #dibuixar vides
        if vides_jugador1 >= 6:
            pantalla.blit(vides_jugador1_image,(730,520))
        if vides_jugador1 >= 5:
            pantalla.blit(vides_jugador1_image,(700,520))
        if vides_jugador1 >= 4:
            pantalla.blit(vides_jugador1_image,(670,520))
        if vides_jugador1 >= 3:
            pantalla.blit(vides_jugador1_image,(670,550))
        if vides_jugador1 >= 2:
            pantalla.blit(vides_jugador1_image, (700, 550))
        if vides_jugador1 >= 1:
            pantalla.blit(vides_jugador1_image, (730, 550))

        if vides_jugador2 >= 6:
            pantalla.blit(vides_jugador2_image,(40,60))
        if vides_jugador2 >= 5:
            pantalla.blit(vides_jugador2_image,(70,60))
        if vides_jugador2 >= 4:
            pantalla.blit(vides_jugador2_image,(100,60))
        if vides_jugador2 >= 3:
            pantalla.blit(vides_jugador2_image,(100,30))
        if vides_jugador2 >= 2:
            pantalla.blit(vides_jugador2_image, (70, 30))
        if (vides_jugador2 >= 1):
            pantalla.blit(vides_jugador2_image, (40, 30))

        if vides_jugador1 <= 0 or vides_jugador2 <= 0:
            guanyador = 1
            if vides_jugador1 <= 0:
                guanyador = 2

            pantalla_actual = 4


    pygame.display.update()
    clock.tick(fps)

