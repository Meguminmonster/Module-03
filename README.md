El módulo sys en Python es una herramienta integrada que te permite interactuar directamente con el intérprete de Python.

A diferencia de otros módulos que manejan archivos o redes, sys se encarga de la configuración y las funciones que afectan cómo se está ejecutando tu código en ese preciso momento.

¿Para qué sirve? (Funciones clave)

sys.argv: Es una lista que contiene los argumentos de la línea de comandos que le pasas a un script al ejecutarlo. Muy útil para crear herramientas de terminal.

sys.path: Una lista de cadenas que determina dónde busca Python los módulos al usar import. Si Python no encuentra tu librería, aquí es donde debes mirar.

sys.exit(): Permite salir de un programa de forma segura, incluso lanzando un código de error si algo salió mal.

sys.version: Te dice exactamente qué versión de Python estás usando.

sys.stdin / stdout: Permiten manipular la entrada y salida de datos de forma más avanzada que un simple print() o input().

Diferencia rápida: sys vs os
Es común confundirlos, pero piénsalo así:

os: Sirve para hablar con el Sistema Operativo (carpetas, archivos, procesos del PC).

sys: Sirve para hablar con el Entorno de Python (parámetros del intérprete, rutas de librerías).

Nota: Al ser un módulo nativo, no necesitas instalar nada. Solo escribe import sys al inicio de tu archivo y listo.

---

Tu primera estructura de datos real. Las listas son el equivalente a tu mochila de inventario: son ordenadas, puedes añadir elementos y calcular analíticas básicas sobre ellas (como sumar puntuaciones o buscar la más alta).

---

 Las tuplas son como las listas, pero inmutables (una vez creadas, no se pueden modificar). Son perfectas para coordenadas 3D en juegos (x, y, z). Además, aprendes la magia del unpacking (desempaquetado), que permite asignar varias variables de golpe (x, y, z = posicion).
 
---

El tipo float en Python se utiliza para representar y almacenar números reales, es decir, números que incluyen una parte fraccionaria o decimal

---

 Los sets son colecciones que no admiten duplicados. Si intentas añadir el mismo logro de un juego dos veces, el set lo ignora. Además, aprendes a hacer magia analítica cruzando datos (uniones, intersecciones y diferencias para ver qué jugadores tienen logros en común).
 
---

Los diccionarios usan pares "llave: valor" para búsquedas instantáneas (ej. inventario["pocion"]). Aquí también aprendes a usar estructuras anidadas (diccionarios dentro de diccionarios) para crear sistemas complejos.
---

Generadores (yield)
Lo nuevo: Este es un concepto de nivel pro. En lugar de crear una lista gigante que colapse la memoria RAM de tu ordenador, los generadores "fabrican" los datos uno a uno bajo demanda usando la palabra clave yield. Es el secreto para procesar streams infinitos de datos sin que el programa se cuelgue.

---

Comprensiones (Comprehensions)
Lo nuevo: La forma más purista, elegante y "Pythonica" de transformar datos. Aprendes a filtrar y crear Listas, Diccionarios y Sets en una sola línea de código, reemplazando bloques enteros de bucles for.
