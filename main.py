import pygame
import random
import math

pygame.init()

# Configuración de la pantalla
info_pantalla = pygame.display.Info()
ancho = int(info_pantalla.current_w * 0.9)
alto = int(info_pantalla.current_h * 0.9)
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('TACTICAL BATTLE')

# Fondo
fondo = pygame.image.load("imagenes/mapa.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Jugador
jugador = pygame.Rect(100, 100, 50, 50)
nuevo_ancho_jugador = 70
nuevo_alto_jugador = 70

# Cargar imagen y ajustar tamaño
jugador_imagen_original = pygame.image.load("imagenes/jugador.png")
jugador_imagen_original = pygame.transform.scale(jugador_imagen_original, (nuevo_ancho_jugador, nuevo_alto_jugador))

# Crear las imágenes rotadas para cada dirección
jugador_imagen_derecha = pygame.transform.flip(jugador_imagen_original, True, False)
jugador_imagen_izquierda = jugador_imagen_original
jugador_imagen_abajo = pygame.transform.rotate(jugador_imagen_original, 90)
jugador_imagen_arriba = pygame.transform.rotate(jugador_imagen_original, -90)

jugador_velocidad = 5
direccion_actual = 'abajo'

# Enemigos IA
num_enemigos = 5
enemigos = []
for _ in range(num_enemigos):
    x = random.randint(0, ancho - 50)
    y = random.randint(0, alto - 50)
    enemigo = {
        'rect': pygame.Rect(x, y, 50, 50),  # Rectángulo que representa la posición y tamaño del enemigo
        'tiempo_disparo': random.randint(30, 120)  # Tiempo para que dispare
    }
    enemigos.append(enemigo)

enemigo_velocidad = 2
enemigo_imagen = pygame.image.load("imagenes/enemigo.png")  # Imagen para los enemigos
enemigo_imagen = pygame.transform.scale(enemigo_imagen, (50, 50))

# Balas
balas = []
velocidad_bala = 10
balas_enemigo = []  # Lista para las balas de los enemigos
velocidad_bala_enemigo = 7

# Reloj
reloj = pygame.time.Clock()
corriendo = True

# Bucle del juego
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 3:  # Click derecho
            if direccion_actual == 'izquierda':
                bala = {'rect': pygame.Rect(jugador.x, jugador.y + jugador.height // 2, 10, 5),
                        'dir_x': -velocidad_bala, 'dir_y': 0}
            elif direccion_actual == 'derecha':
                bala = {'rect': pygame.Rect(jugador.x + jugador.width, jugador.y + jugador.height // 2, 10, 5),
                        'dir_x': velocidad_bala, 'dir_y': 0}
            elif direccion_actual == 'arriba':
                bala = {'rect': pygame.Rect(jugador.x + jugador.width // 2, jugador.y, 5, 10), 'dir_x': 0,
                        'dir_y': -velocidad_bala}
            elif direccion_actual == 'abajo':
                bala = {'rect': pygame.Rect(jugador.x + jugador.width // 2, jugador.y + jugador.height, 5, 10),
                        'dir_x': 0, 'dir_y': velocidad_bala}
            balas.append(bala)

    # Movimiento del jugador y actualización de dirección
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= jugador_velocidad
        direccion_actual = 'izquierda'
    if teclas[pygame.K_RIGHT]:
        jugador.x += jugador_velocidad
        direccion_actual = 'derecha'
    if teclas[pygame.K_UP]:
        jugador.y -= jugador_velocidad
        direccion_actual = 'arriba'
    if teclas[pygame.K_DOWN]:
        jugador.y += jugador_velocidad
        direccion_actual = 'abajo'

    # Movimiento de los enemigos (IA simple que sigue al jugador)
    for enemigo in enemigos:
        if enemigo['rect'].x < jugador.x:
            enemigo['rect'].x += enemigo_velocidad
        elif enemigo['rect'].x > jugador.x:
            enemigo['rect'].x -= enemigo_velocidad
        if enemigo['rect'].y < jugador.y:
            enemigo['rect'].y += enemigo_velocidad
        elif enemigo['rect'].y > jugador.y:
            enemigo['rect'].y -= enemigo_velocidad

        # Temporizador para disparo
        enemigo['tiempo_disparo'] -= 1
        if enemigo['tiempo_disparo'] <= 0:
            # Reinicia el temporizador y dispara
            enemigo['tiempo_disparo'] = random.randint(30, 120)

            # Calcular dirección hacia el jugador
            dx = jugador.x - enemigo['rect'].x
            dy = jugador.y - enemigo['rect'].y
            distancia = math.hypot(dx, dy)
            if distancia != 0:
                dir_x = (dx / distancia) * velocidad_bala_enemigo
                dir_y = (dy / distancia) * velocidad_bala_enemigo
                bala_enemigo = {'rect': pygame.Rect(enemigo['rect'].x, enemigo['rect'].y, 10, 10), 'dir_x': dir_x,
                                'dir_y': dir_y}
                balas_enemigo.append(bala_enemigo)

    # Mover balas del jugador
    for bala in balas[:]:
        bala['rect'].x += bala['dir_x']
        bala['rect'].y += bala['dir_y']
        if (bala['rect'].x < 0 or bala['rect'].x > ancho or bala['rect'].y < 0 or bala['rect'].y > alto):
            balas.remove(bala)

    # Mover balas de los enemigos
    for bala in balas_enemigo[:]:
        bala['rect'].x += bala['dir_x']
        bala['rect'].y += bala['dir_y']
        if (bala['rect'].x < 0 or bala['rect'].x > ancho or bala['rect'].y < 0 or bala['rect'].y > alto):
            balas_enemigo.remove(bala)

    # Seleccionar la imagen del jugador según la dirección
    if direccion_actual == 'izquierda':
        jugador_imagen = jugador_imagen_izquierda
    elif direccion_actual == 'derecha':
        jugador_imagen = jugador_imagen_derecha
    elif direccion_actual == 'arriba':
        jugador_imagen = jugador_imagen_arriba
    elif direccion_actual == 'abajo':
        jugador_imagen = jugador_imagen_abajo

    # Dibujar en pantalla
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(jugador_imagen, (jugador.x, jugador.y))

    # Dibujar enemigos
    for enemigo in enemigos:
        pantalla.blit(enemigo_imagen, (enemigo['rect'].x, enemigo['rect'].y))

    # Dibujar balas del jugador
    for bala in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), bala['rect'])

    # Dibujar balas de los enemigos
    for bala in balas_enemigo:
        pygame.draw.rect(pantalla, (0, 255, 0), bala['rect'])

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
