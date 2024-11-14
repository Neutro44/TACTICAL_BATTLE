import pygame

pygame.init()

# Obtener las dimensiones de la pantalla y hacer la ventana más grande
info_pantalla = pygame.display.Info()
ancho = int(info_pantalla.current_w * 0.9)  # 90% del ancho de la pantalla
alto = int(info_pantalla.current_h * 0.8)   # 90% del alto de la pantalla
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

# Balas
balas = []
velocidad_bala = 10

# Reloj
reloj = pygame.time.Clock()
corriendo = True

# Bucle del juego
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 3:  # Click derecho
            # Crear bala en la dirección actual
            if direccion_actual == 'izquierda':
                bala = {'rect': pygame.Rect(jugador.x, jugador.y + jugador.height // 2, 10, 5), 'dir': 'izquierda'}
            elif direccion_actual == 'derecha':
                bala = {'rect': pygame.Rect(jugador.x + jugador.width, jugador.y + jugador.height // 2, 10, 5), 'dir': 'derecha'}
            elif direccion_actual == 'arriba':
                bala = {'rect': pygame.Rect(jugador.x + jugador.width // 2, jugador.y, 5, 10), 'dir': 'arriba'}
            elif direccion_actual == 'abajo':
                bala = {'rect': pygame.Rect(jugador.x + jugador.width // 2, jugador.y + jugador.height, 5, 10), 'dir': 'abajo'}
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

    # Mover balas
    for bala in balas[:]:
        if bala['dir'] == 'izquierda':
            bala['rect'].x -= velocidad_bala
        elif bala['dir'] == 'derecha':
            bala['rect'].x += velocidad_bala
        elif bala['dir'] == 'arriba':
            bala['rect'].y -= velocidad_bala
        elif bala['dir'] == 'abajo':
            bala['rect'].y += velocidad_bala

        # Eliminar la bala si sale de la pantalla
        if (bala['rect'].x < 0 or bala['rect'].x > ancho or
                bala['rect'].y < 0 or bala['rect'].y > alto):
            balas.remove(bala)

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

    # Dibujar balas
    for bala in balas:
        pygame.draw.rect(pantalla, (0, 0, 0), bala['rect'])

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
