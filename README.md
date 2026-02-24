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
