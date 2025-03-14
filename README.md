## 🌱 Simulador de Ecosistema en Python 🐺

### Descripción
ecosystem-simulator-python es un simulador visual de un ecosistema en tiempo real que muestra la interacción entre plantas, herbívoros y depredadores. Esta aplicación permite observar cómo los cambios en las poblaciones de cada especie afectan el equilibrio del ecosistema, demostrando conceptos básicos de dinámica poblacional y cadenas alimenticias.

### Características
- **Visualización en tiempo real**: Observa el comportamiento de los organismos en un entorno 2D utilizando Pygame.
- **Tres niveles tróficos**: 
  - 🌱 Plantas (productores)
  - 🐰 Presas (consumidores primarios)
  - 🐺 Depredadores (consumidores secundarios)
- **Comportamientos realistas**:
  - Las plantas crecen y se reproducen según condiciones específicas
  - Las presas buscan alimento y evitan depredadores
  - Los depredadores cazan presas siguiendo patrones de comportamiento
- **Sistema de energía**: Cada organismo tiene un nivel de energía que aumenta al alimentarse y disminuye con actividades como movimiento y reproducción.
- **Equilibrio dinámico**: El ecosistema puede alcanzar diferentes estados de equilibrio o colapsar dependiendo de las interacciones entre especies.

### Requisitos
- Python 3.6 o superior
- Pygame 2.0.0 o superior

### Instalación
1. Clona este repositorio:
   ```
   git clone https://github.com/tuusuario/ecosystem-simulator-python.git
   ```
2. Ingresa al directorio del proyecto:
   ```
   cd ecosystem-simulator-python
   ```
3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

### Ejecución
```
python ecosistema.py
```

### Controles
- **ESC**: Salir de la simulación
- **ESPACIO**: Pausar/Reanudar la simulación
- **+/-**: Aumentar/Disminuir la velocidad de la simulación

### Parámetros configurables
Puedes modificar los siguientes parámetros en el archivo `ecosistema.py`:

- Cantidad inicial de cada tipo de organismo
- Tasas de reproducción
- Tasas de consumo de energía
- Velocidad de movimiento
- Comportamientos específicos de cada especie

### Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar esta simulación, puedes:
- Añadir nuevas especies o niveles tróficos
- Implementar factores ambientales (clima, estaciones)
- Mejorar la visualización o añadir estadísticas
- Corregir errores o mejorar el rendimiento
