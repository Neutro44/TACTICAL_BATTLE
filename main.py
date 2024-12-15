import pygame
import random
# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
info_pantalla = pygame.display.Info()
ancho = int(info_pantalla.current_w * 0.9)
alto = int(info_pantalla.current_h * 0.9)
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('TACTICAL BATTLE')

# Configuración del mapa
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

tamaño_celda = 50

# Cargar imágenes
imagen_pared = pygame.image.load("imagenes/chullpas.png  ")
imagen_pared = pygame.transform.scale(imagen_pared, (tamaño_celda, tamaño_celda))
imagen_camino = pygame.image.load("imagenes/pisoo.png")
imagen_camino = pygame.transform.scale(imagen_camino, (tamaño_celda, tamaño_celda))

# Jugador
tamaño_jugador = 40
jugador = pygame.Rect(150, 150, tamaño_celda, tamaño_celda)
jugador_velocidad = 4

jugador_imagen_original = pygame.image.load("imagenes/jugador4.png")
jugador_imagen_original = pygame.transform.scale(jugador_imagen_original, (tamaño_jugador, tamaño_jugador))
jugador_imagen_derecha = pygame.transform.flip(jugador_imagen_original, True, False)
jugador_imagen_izquierda = jugador_imagen_original
jugador_imagen_abajo = pygame.transform.rotate(jugador_imagen_original, 90)
jugador_imagen_arriba = pygame.transform.rotate(jugador_imagen_original, -90)
direccion_actual = 'abajo'

# Proyectiles
proyectiles = []
velocidad_proyectil = 8
proyectil_tamaño = 10
color_proyectil = (0, 0, 255)  # Rojo


# Función para verificar movimiento válido
def puede_moverse(x, y):
    fila = y // tamaño_celda
    columna = x // tamaño_celda
    if 0 <= fila < len(mapa) and 0 <= columna < len(mapa[0]):
        return mapa[fila][columna] == 0
    return False

# Enemigos IA
num_enemigos = 3
enemigos = []


for _ in range(num_enemigos):
    x = random.randint(1, len(mapa[0]) - 2) * tamaño_celda
    y = random.randint(1, len(mapa) - 2) * tamaño_celda
    enemigos.append({'rect': pygame.Rect(x, y, tamaño_celda, tamaño_celda),
                     'direccion': random.choice(['izquierda', 'derecha', 'arriba', 'abajo'])})

enemigo_velocidad = 1
enemigo_imagen_original = pygame.image.load("imagenes/enemigo3.png")
enemigo_imagen_original = pygame.transform.scale(enemigo_imagen_original, (tamaño_jugador, tamaño_jugador))
enemigo_imagen_derecha = pygame.transform.flip(enemigo_imagen_original, True, False)
enemigo_imagen_izquierda = enemigo_imagen_original
enemigo_imagen_abajo = pygame.transform.rotate(enemigo_imagen_original, 90)
enemigo_imagen_arriba = pygame.transform.rotate(enemigo_imagen_original, -90)

enemigos = []
for _ in range(num_enemigos):
    x = random.randint(1, len(mapa[0]) - 2) * tamaño_celda
    y = random.randint(1, len(mapa) - 2) * tamaño_celda
    enemigos.append({
        'rect': pygame.Rect(x, y, tamaño_celda, tamaño_celda),
        'direccion': random.choice(['izquierda', 'derecha', 'arriba', 'abajo']),
        'imagen': enemigo_imagen_abajo  # Imagen inicial
    })


# Función para mover enemigos
def mover_enemigos():
    for enemigo in enemigos:
        if tiene_linea_vision(enemigo, jugador):
            # Apuntar directamente hacia el jugador
            if enemigo['rect'].x < jugador.x:
                enemigo['direccion'] = 'derecha'
            elif enemigo['rect'].x > jugador.x:
                enemigo['direccion'] = 'izquierda'
            elif enemigo['rect'].y < jugador.y:
                enemigo['direccion'] = 'abajo'
            elif enemigo['rect'].y > jugador.y:
                enemigo['direccion'] = 'arriba'
        # Si no ve al jugador, mantener la dirección actual
        # No cambiar a aleatorio, simplemente mantener la dirección que ya tiene
        else:
            pass

        # Mover enemigo en la dirección actual
        if enemigo['direccion'] == 'izquierda' and puede_moverse(enemigo['rect'].x - enemigo_velocidad, enemigo['rect'].y):
            enemigo['rect'].x -= enemigo_velocidad
            enemigo['imagen'] = enemigo_imagen_izquierda
        elif enemigo['direccion'] == 'derecha' and puede_moverse(enemigo['rect'].x + enemigo_velocidad, enemigo['rect'].y):
            enemigo['rect'].x += enemigo_velocidad
            enemigo['imagen'] = enemigo_imagen_derecha
        elif enemigo['direccion'] == 'arriba' and puede_moverse(enemigo['rect'].x, enemigo['rect'].y - enemigo_velocidad):
            enemigo['rect'].y -= enemigo_velocidad
            enemigo['imagen'] = enemigo_imagen_arriba
        elif enemigo['direccion'] == 'abajo' and puede_moverse(enemigo['rect'].x, enemigo['rect'].y + enemigo_velocidad):
            enemigo['rect'].y += enemigo_velocidad
            enemigo['imagen'] = enemigo_imagen_abajo
        else:
            # Si no puede moverse, mantener su dirección
            pass


# Reloj para FPS
reloj = pygame.time.Clock()
corriendo = True
# Variables globales para contar bloques destruidos
cuadrados_destruidos_jugador = 0
cuadrados_destruidos_enemigos = 0

# Función para dibujar el mapa
def dibujar_mapa(pantalla, mapa):
    for fila in range(len(mapa)):
        for columna in range(len(mapa[fila])):
            x = columna * tamaño_celda
            y = fila * tamaño_celda
            if mapa[fila][columna] == 1:
                pantalla.blit(imagen_pared, (x, y))
            elif mapa[fila][columna] == 0:
                pantalla.blit(imagen_camino, (x, y))





# Función para mover proyectiles
def mover_proyectiles():
    global proyectiles
    proyectiles_actualizados = []
    for proyectil in proyectiles:
        nuevo_rect = proyectil['rect'].copy()  # Copiamos la posición actual
        if proyectil['direccion'] == 'arriba':
            nuevo_rect.y -= velocidad_proyectil
        elif proyectil['direccion'] == 'abajo':
            nuevo_rect.y += velocidad_proyectil
        elif proyectil['direccion'] == 'izquierda':
            nuevo_rect.x -= velocidad_proyectil
        elif proyectil['direccion'] == 'derecha':
            nuevo_rect.x += velocidad_proyectil

        # Verificar si el proyectil no colisiona con una pared
        fila = nuevo_rect.centery // tamaño_celda
        columna = nuevo_rect.centerx // tamaño_celda
        if 0 <= fila < len(mapa) and 0 <= columna < len(mapa[0]) and mapa[fila][columna] == 0:
            proyectil['rect'] = nuevo_rect
            proyectiles_actualizados.append(proyectil)

    proyectiles = proyectiles_actualizados


# Función para verificar colisiones entre proyectiles y enemigos
def verificar_colisiones():
    global enemigos, proyectiles
    nuevos_enemigos = []
    proyectiles_restantes = []

    for enemigo in enemigos:
        enemigo_destruido = False  # Control por cada enemigo
        for proyectil in proyectiles:
            if enemigo['rect'].colliderect(proyectil['rect']):
                enemigo_destruido = True
                break  # Salimos del bucle de proyectiles si destruimos al enemigo
        if not enemigo_destruido:
            nuevos_enemigos.append(enemigo)

    # Filtrar proyectiles que no impactaron enemigos
    proyectiles_restantes = [p for p in proyectiles if not any(p['rect'].colliderect(e['rect']) for e in enemigos)]

    # Actualizamos las listas principales
    enemigos = nuevos_enemigos
    proyectiles = proyectiles_restantes

# Lista de proyectiles enemigos
proyectiles_enemigos = []
velocidad_proyectil_enemigo = 3

# Función para verificar si el enemigo ve al jugador o un cuadrado amarillo
def tiene_linea_vision(enemigo, objetivo):
    ex, ey = enemigo['rect'].centerx, enemigo['rect'].centery
    jx, jy = objetivo.centerx, objetivo.centery

    dx, dy = jx - ex, jy - ey
    pasos = max(abs(dx), abs(dy))  # Número de pasos que da el raycasting

    stepx = dx / pasos if pasos != 0 else 0
    stepy = dy / pasos if pasos != 0 else 0

    # Empezamos desde la posición del enemigo
    x, y = ex, ey

    for i in range(pasos):
        x += stepx
        y += stepy
        columna, fila = int(x // tamaño_celda), int(y // tamaño_celda)

        # Comprobar si estamos fuera del mapa o si hay un muro (valor 1 en el mapa)
        if fila < 0 or fila >= len(mapa) or columna < 0 or columna >= len(mapa[0]) or mapa[fila][columna] == 1:
            return False  # Hay un muro en el camino
    return True  # No hay muros en el camino
# Función de disparo de proyectiles enemigos hacia el jugador o un cuadrado amarillo
def disparar_proyectil_enemigo(enemigo, objetivo):
    if tiene_linea_vision(enemigo, objetivo):
        # Obtener la dirección actual del enemigo
        direccion = enemigo['direccion']
        if direccion == 'arriba':
            proyectil_rect = pygame.Rect(enemigo['rect'].centerx - proyectil_tamaño // 2,
                                         enemigo['rect'].top - proyectil_tamaño, proyectil_tamaño, proyectil_tamaño)
        elif direccion == 'abajo':
            proyectil_rect = pygame.Rect(enemigo['rect'].centerx - proyectil_tamaño // 2,
                                         enemigo['rect'].bottom, proyectil_tamaño, proyectil_tamaño)
        elif direccion == 'izquierda':
            proyectil_rect = pygame.Rect(enemigo['rect'].left - proyectil_tamaño,
                                         enemigo['rect'].centery - proyectil_tamaño // 2, proyectil_tamaño, proyectil_tamaño)
        elif direccion == 'derecha':
            proyectil_rect = pygame.Rect(enemigo['rect'].right,
                                         enemigo['rect'].centery - proyectil_tamaño // 2, proyectil_tamaño, proyectil_tamaño)
        # Añadir proyectil a la lista
        proyectiles_enemigos.append({'rect': proyectil_rect, 'direccion': direccion})
# Mover proyectiles enemigos
def mover_proyectiles_enemigos():
    global proyectiles_enemigos
    proyectiles_actualizados = []
    for proyectil in proyectiles_enemigos:
        nuevo_rect = proyectil['rect'].copy()  # Copiamos la posición actual
        if proyectil['direccion'] == 'arriba':
            nuevo_rect.y -= velocidad_proyectil_enemigo
        elif proyectil['direccion'] == 'abajo':
            nuevo_rect.y += velocidad_proyectil_enemigo
        elif proyectil['direccion'] == 'izquierda':
            nuevo_rect.x -= velocidad_proyectil_enemigo
        elif proyectil['direccion'] == 'derecha':
            nuevo_rect.x += velocidad_proyectil_enemigo

        # Verificar si el proyectil no colisiona con una pared
        fila = nuevo_rect.centery // tamaño_celda
        columna = nuevo_rect.centerx // tamaño_celda
        if 0 <= fila < len(mapa) and 0 <= columna < len(mapa[0]) and mapa[fila][columna] == 0:
            proyectil['rect'] = nuevo_rect
            proyectiles_actualizados.append(proyectil)

    proyectiles_enemigos = proyectiles_actualizados


# Función para verificar colisiones entre proyectiles enemigos y los cuadrados destructibles
def verificar_colisiones_proyectiles_enemigos_cuadrados():
    global proyectiles_enemigos, cuadrados_destructibles, cuadrados_destruidos_enemigos
    for proyectil in proyectiles_enemigos[:]:
        for cuadrado in cuadrados_destructibles[:]:
            if proyectil['rect'].colliderect(cuadrado):
                cuadrados_destructibles.remove(cuadrado)  # Eliminar cuadrado
                proyectiles_enemigos.remove(proyectil)  # Eliminar proyectil
                cuadrados_destruidos_enemigos += 1  # Incrementar contador de enemigos
                break  # Salir del bucle después de la colisión
# Función para actualizar los enemigos (disparando si ven al jugador o cuadrado amarillo)
def actualizar_enemigos():
    for enemigo in enemigos:
        if tiene_linea_vision(enemigo, jugador):
            # Los enemigos disparan solo si ven al jugador
            if random.random() < 0.009:
                disparar_proyectil_enemigo(enemigo, jugador)
        else:
            # Verificar si el enemigo ve algún cuadrado amarillo (destructible)
            for cuadrado in cuadrados_destructibles:
                if tiene_linea_vision(enemigo, cuadrado):
                    if random.random() < 0.009:
                        disparar_proyectil_enemigo(enemigo, cuadrado)
                    break  # Salir después de disparar a un cuadrado amarillo

# Lista de cuadrados destructibles
cuadrados_destructibles = []

# Función para inicializar cuadrados destructibles
def inicializar_cuadrados(cantidad):
    global cuadrados_destructibles
    posibles_posiciones = []

    # Encontrar todas las posiciones caminables (0 en el mapa)
    for fila in range(len(mapa)):
        for columna in range(len(mapa[fila])):
            if mapa[fila][columna] == 0:
                posibles_posiciones.append((columna * tamaño_celda, fila * tamaño_celda))

    # Seleccionar posiciones aleatorias para los cuadrados destructibles
    seleccionadas = random.sample(posibles_posiciones, min(cantidad, len(posibles_posiciones)))

    # Crear cuadrados destructibles en las posiciones seleccionadas
    cuadrados_destructibles = [pygame.Rect(x, y, tamaño_celda, tamaño_celda) for x, y in seleccionadas]

# Inicializar una cantidad fija de cuadrados destructibles
inicializar_cuadrados(50)  # Ajusta la cantidad para depuración

# Función para dibujar cuadrados destructibles
def dibujar_cuadrados(pantalla):
    for cuadrado in cuadrados_destructibles:
        pygame.draw.rect(pantalla, pygame.Color("yellow"), cuadrado)  # Cambiar a amarillo temporalmente

def verificar_colisiones_cuadrados():
    global cuadrados_destructibles, proyectiles, cuadrados_destruidos_jugador
    for proyectil in proyectiles[:]:
        for cuadrado in cuadrados_destructibles[:]:
            if proyectil['rect'].colliderect(cuadrado):
                cuadrados_destructibles.remove(cuadrado)  # Eliminar cuadrado
                proyectiles.remove(proyectil)  # Eliminar proyectil
                cuadrados_destruidos_jugador += 1  # Incrementar contador
                break


# Función para verificar colisiones entre proyectiles del jugador y cuadrados destructibles
def verificar_colisiones_proyectiles_jugador_cuadrados():
    global cuadrados_destructibles, proyectiles, cuadrados_destruidos_jugador
    for proyectil in proyectiles[:]:
        for cuadrado in cuadrados_destructibles[:]:
            if proyectil['rect'].colliderect(cuadrado):
                cuadrados_destructibles.remove(cuadrado)  # Eliminar cuadrado
                proyectiles.remove(proyectil)  # Eliminar proyectil
                cuadrados_destruidos_jugador += 1  # Incrementar el contador
                break  # Salir del bucle después de destruir un cuadrado


# Fuente para los puntajes
fuente_puntaje = pygame.font.Font(None, 36)  # Fuente predeterminada, tamaño 36


# Función para dibujar el puntaje
def mostrar_puntajes(pantalla):
    texto_jugador = fuente_puntaje.render(f"Jugador: {cuadrados_destruidos_jugador}", True, (255, 255, 255))
    texto_enemigo = fuente_puntaje.render(f"Enemigos: {cuadrados_destruidos_enemigos}", True, (255, 255, 255))

    pantalla.blit(texto_jugador, (20, 20))  # Mostrar puntaje del jugador
    pantalla.blit(texto_enemigo, (20, 60))  # Mostrar puntaje del enemigo

# Función para mostrar el mensaje de "Perdiste"
def mostrar_mensaje(texto, color):
    fuente = pygame.font.Font(None, 74)  # Fuente de tamaño 74
    texto_renderizado = fuente.render(texto, True, color)
    texto_rect = texto_renderizado.get_rect(center=(ancho // 2, alto // 2))  # Centrar el texto
    pantalla.blit(texto_renderizado, texto_rect)
    pygame.display.flip()  # Actualizar la pantalla
# Función para verificar colisiones entre los proyectiles enemigos y el jugador
# Función para verificar colisiones entre los proyectiles enemigos y el jugador
def verificar_colisiones_proyectiles_enemigos_jugador():
    global proyectiles_enemigos, jugador, corriendo
    for proyectil in proyectiles_enemigos[:]:
        if proyectil['rect'].colliderect(jugador):
            # El proyectil impactó al jugador
            mostrar_mensaje("¡Perdiste!", (255, 0, 0))  # Rojo para el mensaje
            corriendo = False  # Detener el bucle principal
            tiempo_perdido = pygame.time.get_ticks()  # Guardar el tiempo en que se mostró el mensaje
            while pygame.time.get_ticks() - tiempo_perdido < 2000:  # Esperar 2 segundos (2000 ms)
                pygame.event.pump()  # Procesar eventos para evitar que el juego se congele
            break  # Salir del bucle después de la colisión

# Función para verificar si no quedan cuadrados destructibles
def verificar_fin_juego():
    if len(cuadrados_destructibles) == 0:
        global corriendo
        corriendo = False
        # Mostrar ganador
        if cuadrados_destruidos_jugador > cuadrados_destruidos_enemigos:
            mensaje = "¡El jugador ha ganado!"
        elif cuadrados_destruidos_jugador < cuadrados_destruidos_enemigos:
            mensaje = "¡Los enemigos han ganado!"
        else:
            mensaje = "¡Es un empate!"
        mostrar_mensaje_fin_juego(mensaje)

# Función para mostrar mensaje de fin de juego
def mostrar_mensaje_fin_juego(mensaje):
    fuente = pygame.font.SysFont('Arial', 48)
    texto = fuente.render(mensaje, True, (255, 255, 255))
    pantalla.blit(texto, (ancho // 2 - texto.get_width() // 2, alto // 2 - texto.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # Espera de 3 segundos antes de cerrar
#______________________________


# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

dificultad = "baja"  # Se puede cambiar a 'media' o 'dificil' según la elección


# Configurar la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tactical Battle")

# Función para mostrar texto en pantalla
def mostrar_texto(texto, fuente, color, x, y):
    etiqueta = fuente.render(texto, True, color)
    pantalla.blit(etiqueta, (x, y))

# Función para crear el menú principal
def menu_principal():
    fuente = pygame.font.SysFont('Arial', 40)
    while True:
        pantalla.fill(BLANCO)
        mostrar_texto("Tactical Battle", fuente, NEGRO, 300, 150)
        mostrar_texto("1. Jugar", fuente, NEGRO, 350, 250)
        mostrar_texto("2. Salir", fuente, NEGRO, 350, 300)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:  # El jugador elige jugar
                    seleccionar_dificultad()
                    return
                elif evento.key == pygame.K_2:  # El jugador elige salir
                    pygame.quit()
                    return
        
        pygame.display.update()

# Función para seleccionar la dificultad
def seleccionar_dificultad():
    fuente = pygame.font.SysFont('Arial', 40)
    while True:
        pantalla.fill(BLANCO)
        mostrar_texto("Seleccionar Dificultad", fuente, NEGRO, 250, 150)
        mostrar_texto("1. Baja", fuente, NEGRO, 350, 250)
        mostrar_texto("2. Media", fuente, NEGRO, 350, 300)
        mostrar_texto("3. Difícil", fuente, NEGRO, 350, 350)
        mostrar_texto("Escoge una opción", fuente, NEGRO, 250, 450)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:  # Dificultad baja
                    dificultad = "baja"
                    iniciar_juego(dificultad)
                    return
                elif evento.key == pygame.K_2:  # Dificultad media
                    dificultad = "media"
                    iniciar_juego(dificultad)
                    return
                elif evento.key == pygame.K_3:  # Dificultad difícil
                    dificultad = "dificil"
                    iniciar_juego(dificultad)
                    return

def iniciar_juego(dificultad):
    if dificultad == "baja":
        velocidad_enemigos = 2
        numero_enemigos = 5
    elif dificultad == "media":
        velocidad_enemigos = 4
        numero_enemigos = 10
    elif dificultad == "dificil":
        velocidad_enemigos = 6
        numero_enemigos = 15

    # Iniciar el juego con las configuraciones de dificultad
    jugar(velocidad_enemigos, numero_enemigos)
# Función para iniciar el juego
def iniciar_juego(dificultad):
    direccion_actual = 'abajo'
    print(f"Iniciando juego con dificultad {dificultad}")
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                # Crear un nuevo proyectil del jugador
                proyectil_rect = pygame.Rect(jugador.centerx - proyectil_tamaño // 2,
                                             jugador.centery - proyectil_tamaño // 2, proyectil_tamaño,
                                             proyectil_tamaño)
                proyectiles.append({'rect': proyectil_rect, 'direccion': direccion_actual})


    # Mover proyectiles
    mover_proyectiles()
    mover_proyectiles_enemigos()
    # Verificar colisiones entre los proyectiles enemigos y los cuadrados destructibles
    verificar_colisiones_proyectiles_enemigos_cuadrados()

    # Verificar colisiones
    verificar_colisiones()

    verificar_colisiones_cuadrados()

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and puede_moverse(jugador.x - jugador_velocidad, jugador.y):
        jugador.x -= jugador_velocidad
        direccion_actual = 'izquierda'
    if teclas[pygame.K_RIGHT] and puede_moverse(jugador.x + jugador.width + jugador_velocidad - 1, jugador.y):
        jugador.x += jugador_velocidad
        direccion_actual = 'derecha'
    if teclas[pygame.K_UP] and puede_moverse(jugador.x, jugador.y - jugador_velocidad):
        jugador.y -= jugador_velocidad
        direccion_actual = 'arriba'
    if teclas[pygame.K_DOWN] and puede_moverse(jugador.x, jugador.y + jugador.height + jugador_velocidad - 1):
        jugador.y += jugador_velocidad
        direccion_actual = 'abajo'

    # Mover y actualizar enemigos
    mover_enemigos()
    actualizar_enemigos()
    # Verificar colisiones entre proyectiles del jugador y enemigos
    verificar_colisiones()


    # Movimiento de los enemigos (IA)
    for enemigo in enemigos:
        if enemigo['direccion'] == 'izquierda' and puede_moverse(enemigo['rect'].x - enemigo_velocidad, enemigo['rect'].y):
            enemigo['rect'].x -= enemigo_velocidad
        elif enemigo['direccion'] == 'derecha' and puede_moverse(enemigo['rect'].x + enemigo['rect'].width + enemigo_velocidad - 1, enemigo['rect'].y):
            enemigo['rect'].x += enemigo_velocidad
        elif enemigo['direccion'] == 'arriba' and puede_moverse(enemigo['rect'].x, enemigo['rect'].y - enemigo_velocidad):
            enemigo['rect'].y -= enemigo_velocidad
        elif enemigo['direccion'] == 'abajo' and puede_moverse(enemigo['rect'].x, enemigo['rect'].y + enemigo['rect'].height + enemigo_velocidad - 1):
            enemigo['rect'].y += enemigo_velocidad
        else:
            enemigo['direccion'] = random.choice(['izquierda', 'derecha', 'arriba', 'abajo'])

    # Actualizar los disparos de los enemigos
    actualizar_enemigos()  # Hacer que los enemigos disparen con probabilidad

    # Selección de la imagen del jugador
    if direccion_actual == 'izquierda':
        jugador_imagen = jugador_imagen_izquierda
    elif direccion_actual == 'derecha':
        jugador_imagen = jugador_imagen_derecha
    elif direccion_actual == 'arriba':
        jugador_imagen = jugador_imagen_arriba
    elif direccion_actual == 'abajo':
        jugador_imagen = jugador_imagen_abajo

    verificar_colisiones_proyectiles_enemigos_jugador()
    verificar_fin_juego()  # Verificar si el juego ha terminado
    # Dibujar elementos
    pantalla.fill((0, 0, 0))
    dibujar_mapa(pantalla, mapa)
    dibujar_cuadrados(pantalla)
    pantalla.blit(jugador_imagen_abajo if direccion_actual == 'abajo' else
                  jugador_imagen_arriba if direccion_actual == 'arriba' else
                  jugador_imagen_izquierda if direccion_actual == 'izquierda' else
                  jugador_imagen_derecha, (jugador.x, jugador.y))
    for enemigo in enemigos:
        pantalla.blit(enemigo['imagen'], (enemigo['rect'].x, enemigo['rect'].y))
    mover_proyectiles_enemigos()

    # Dibujar proyectiles
    for proyectil in proyectiles:
        pygame.draw.rect(pantalla, color_proyectil, proyectil['rect'])

    # Dibujar proyectiles enemigos
    for proyectil in proyectiles_enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), proyectil['rect'])  # Proyectiles enemigos en rojo

        # Mostrar puntajes
    mostrar_puntajes(pantalla)
    pygame.display.flip()
    reloj.tick(30)

    pygame.display.update()
    pygame.quit()


# Ejecutar el juego
if __name__ == "__main__":
    menu_principal()
