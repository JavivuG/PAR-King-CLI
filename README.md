# PAR-King (versión de consola)

Puzle de aparcamiento al estilo *Rush Hour* en Python: mueve los coches por el tablero hasta llevar un coche a la casilla de salida.

> Trabajo de la asignatura **Paradigmas de Programación** · Grado en Ingeniería Informática · Universidad de Valladolid · Curso 2021-2022

## Qué hace

- Carga los niveles desde `niveles.txt` y dibuja el tablero en la terminal con caracteres Unicode de recuadro.
- Cada coche se identifica con una letra: la **mayúscula** lo mueve hacia la izquierda o hacia arriba, y la **minúscula** hacia la derecha o hacia abajo.
- Acepta varias jugadas seguidas en una sola línea (por ejemplo `aBc`) y solo ejecuta las que no chocan con otro coche o con el borde.
- Cuenta los movimientos válidos y da el nivel por completado cuando un coche ocupa la casilla de salida.
- Guarda el récord de cada nivel en `records.txt` y solo permite jugar hasta el primer nivel sin récord.
- Al completar un nivel, pregunta si se quiere pasar al siguiente (`S`/`N`).

## Tecnologías

- Python 3 (solo biblioteca estándar).

## Aspectos técnicos destacados

- **Tablero como matriz de caracteres**: cada casilla del tablero (6x6 más el borde) ocupa un bloque de 3 filas por 5 columnas en una matriz de 24x40, lo que permite dibujar los coches con esquinas y líneas (`┌ ─ ┐ │ └ ┘`).
- **Formato de nivel propio**: cada coche se describe con un código de cuatro caracteres, orientación (`H`/`V`), columna, fila y longitud (por ejemplo `V322`), y cada nivel indica las coordenadas de su salida.
- **Detección de colisiones sobre la propia representación**: antes de mover un coche se comprueba que la casilla destino de la matriz contiene un espacio en blanco.
- **Persistencia en ficheros de texto** para niveles y récords.

## Estructura del repositorio

```text
PAR-King-CLI/
├── PAR-King.py       # Programa completo
├── niveles.txt       # Niveles que carga el programa
├── records.txt       # Récord de movimientos por nivel
├── niveles1.txt      # Ficheros de niveles adicionales (no los carga el código)
├── niveles2.txt
├── niveles3.txt
└── jugadas.txt       # Fichero de datos auxiliar (no lo usa el código)
```

## Requisitos

- Python 3.
- Una terminal con soporte Unicode para ver el tablero correctamente.

## Cómo ejecutar

Desde la carpeta del repositorio, porque el programa abre `niveles.txt` y `records.txt` con rutas relativas:

```bash
python3 PAR-King.py
```

El juego modifica `records.txt` al conseguir un nuevo récord. Para jugar con otro conjunto de niveles, sustituye el contenido de `niveles.txt` por el de otro fichero con el mismo formato.

## Autoría

Trabajo individual de Javier García González.

Existe una versión con interfaz gráfica en [PAR-King-GUI](https://github.com/JavivuG/PAR-King-GUI).

---

Forma parte de [UVa-Projects](https://github.com/JavivuG/UVa-Projects).
