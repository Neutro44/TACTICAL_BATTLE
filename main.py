import pygame

pygame.init()

# Configuración de la pantalla
ancho = 800
alto = 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('TACTICAL BATTLE')

# Fondo
fondo = pygame.image.load("imagenes/mapa.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Jugador
jugador = pygame.Rect(100, 100, 50, 50)
nuevo_ancho_jugador = 70  # Nuevo ancho del jugador
nuevo_alto_jugador = 70   # Nuevo alto del jugador

# Cargar imagen y ajustar tamaño
jugador_imagen_original = pygame.image.load("imagenes/jugador.png")
jugador_imagen_original = pygame.transform.scale(jugador_imagen_original, (nuevo_ancho_jugador, nuevo_alto_jugador))

# Crear las imágenes rotadas para cada dirección
jugador_imagen_derecha = pygame.transform.flip(jugador_imagen_original, True, False)
jugador_imagen_izquierda = jugador_imagen_original
jugador_imagen_abajo = pygame.transform.rotate(jugador_imagen_original, 90)
jugador_imagen_arriba = pygame.transform.rotate(jugador_imagen_original, -90)

jugador_velocidad = 5
direccion_actual = 'abajo'  # Dirección inicial

# Reloj
reloj = pygame.time.Clock()
corriendo = True

# Bucle del juego
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

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
    pantalla.blit(jugador_imagen, (jugador.x, jugador.y))  # Dibujar la imagen del jugador en su posición

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
