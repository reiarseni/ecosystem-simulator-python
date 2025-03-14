import pygame
import random
import time
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Simulación de Ecosistema")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Clases para organismos
class Organismo:
    def __init__(self, x, y, energia=100):
        self.x = x
        self.y = y
        self.energia = energia
        
    def mover(self):
        # Movimiento aleatorio
        self.x += random.randint(-5, 5)
        self.y += random.randint(-5, 5)
        
        # Mantenerse dentro de los límites
        self.x = max(0, min(ancho, self.x))
        self.y = max(0, min(alto, self.y))
        
        # Gastar energía
        self.energia -= 1
        
    def esta_vivo(self):
        return self.energia > 0

class Planta(Organismo):
    def __init__(self, x, y):
        super().__init__(x, y, energia=200)
        self.tamano = 5
        
    def dibujar(self):
        pygame.draw.circle(pantalla, VERDE, (self.x, self.y), self.tamano)
        
    def crecer(self):
        if random.random() < 0.01:
            self.tamano += 1
            self.tamano = min(12, self.tamano)
    
    def reproducir(self):
        if random.random() < 0.005 and self.tamano > 8:
            self.tamano -= 3
            return Planta(
                self.x + random.randint(-20, 20),
                self.y + random.randint(-20, 20)
            )
        return None

class Presa(Organismo):
    def __init__(self, x, y):
        super().__init__(x, y, energia=100)
        
    def dibujar(self):
        pygame.draw.circle(pantalla, AZUL, (self.x, self.y), 7)
    
    def buscar_comida(self, plantas):
        planta_cercana = None
        distancia_minima = 100
        
        for planta in plantas:
            dx = abs(self.x - planta.x)
            dy = abs(self.y - planta.y)
            distancia = (dx**2 + dy**2)**0.5
            
            if distancia < distancia_minima:
                distancia_minima = distancia
                planta_cercana = planta
        
        if planta_cercana:
            # Moverse hacia la planta
            if self.x < planta_cercana.x:
                self.x += 2
            elif self.x > planta_cercana.x:
                self.x -= 2
                
            if self.y < planta_cercana.y:
                self.y += 2
            elif self.y > planta_cercana.y:
                self.y -= 2
                
            # Comer la planta si está suficientemente cerca
            if distancia_minima < 10 and planta_cercana.tamano > 0:
                self.energia += 20
                planta_cercana.tamano -= 2
                if planta_cercana.tamano <= 0:
                    plantas.remove(planta_cercana)
        else:
            self.mover()
    
    def reproducir(self):
        if self.energia > 150 and random.random() < 0.03:
            self.energia -= 50
            return Presa(
                self.x + random.randint(-10, 10),
                self.y + random.randint(-10, 10)
            )
        return None

class Depredador(Organismo):
    def __init__(self, x, y):
        super().__init__(x, y, energia=150)
        
    def dibujar(self):
        pygame.draw.circle(pantalla, ROJO, (self.x, self.y), 9)
    
    def buscar_presa(self, presas):
        presa_cercana = None
        distancia_minima = 150
        
        for presa in presas:
            dx = abs(self.x - presa.x)
            dy = abs(self.y - presa.y)
            distancia = (dx**2 + dy**2)**0.5
            
            if distancia < distancia_minima:
                distancia_minima = distancia
                presa_cercana = presa
        
        if presa_cercana:
            # Moverse hacia la presa
            if self.x < presa_cercana.x:
                self.x += 3
            elif self.x > presa_cercana.x:
                self.x -= 3
                
            if self.y < presa_cercana.y:
                self.y += 3
            elif self.y > presa_cercana.y:
                self.y -= 3
                
            # Comer la presa si está suficientemente cerca
            if distancia_minima < 12:
                self.energia += 70
                presas.remove(presa_cercana)
                return True
        else:
            self.mover()
        return False
    
    def reproducir(self):
        if self.energia > 200 and random.random() < 0.02:
            self.energia -= 70
            return Depredador(
                self.x + random.randint(-10, 10),
                self.y + random.randint(-10, 10)
            )
        return None

# Crear organismos iniciales
plantas = [Planta(random.randint(0, ancho), random.randint(0, alto)) for _ in range(30)]
presas = [Presa(random.randint(0, ancho), random.randint(0, alto)) for _ in range(15)]
depredadores = [Depredador(random.randint(0, ancho), random.randint(0, alto)) for _ in range(5)]

# Fuente para estadísticas
fuente = pygame.font.SysFont(None, 24)

# Ciclo principal del juego
reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    # Procesar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    # Limpiar pantalla
    pantalla.fill(NEGRO)
    
    # Actualizar y dibujar plantas
    nuevas_plantas = []
    for planta in plantas:
        planta.crecer()
        nueva_planta = planta.reproducir()
        if nueva_planta:
            nuevas_plantas.append(nueva_planta)
        planta.dibujar()
    plantas.extend(nuevas_plantas)
    
    # Actualizar y dibujar presas
    nuevas_presas = []
    for presa in presas[:]:
        presa.buscar_comida(plantas)
        nueva_presa = presa.reproducir()
        if nueva_presa:
            nuevas_presas.append(nueva_presa)
        if not presa.esta_vivo():
            presas.remove(presa)
        else:
            presa.dibujar()
    presas.extend(nuevas_presas)
    
    # Actualizar y dibujar depredadores
    nuevos_depredadores = []
    for depredador in depredadores[:]:
        depredador.buscar_presa(presas)
        nuevo_depredador = depredador.reproducir()
        if nuevo_depredador:
            nuevos_depredadores.append(nuevo_depredador)
        if not depredador.esta_vivo():
            depredadores.remove(depredador)
        else:
            depredador.dibujar()
    depredadores.extend(nuevos_depredadores)
    
    # Agregar plantas automáticamente si hay pocas
    if len(plantas) < 10 and random.random() < 0.1:
        plantas.append(Planta(random.randint(0, ancho), random.randint(0, alto)))
    
    # Mostrar estadísticas
    texto_plantas = fuente.render(f"Plantas: {len(plantas)}", True, VERDE)
    texto_presas = fuente.render(f"Presas: {len(presas)}", True, AZUL)
    texto_depredadores = fuente.render(f"Depredadores: {len(depredadores)}", True, ROJO)
    
    pantalla.blit(texto_plantas, (10, 10))
    pantalla.blit(texto_presas, (10, 40))
    pantalla.blit(texto_depredadores, (10, 70))
    
    # Actualizar pantalla
    pygame.display.flip()
    
    # Controlar velocidad
    reloj.tick(30)
    
    # Pausar si el ecosistema colapsa
    if len(plantas) == 0 and len(presas) == 0 and len(depredadores) == 0:
        mensaje = fuente.render("¡Ecosistema colapsado!", True, BLANCO)
        pantalla.blit(mensaje, (ancho//2 - 100, alto//2))
        pygame.display.flip()
        time.sleep(3)
        ejecutando = False

# Finalizar pygame
pygame.quit()
sys.exit()
