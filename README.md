🪙 Lanzador de Moneda con Interfaz Gráfica

Este proyecto es una aplicación sencilla en Python que simula el lanzamiento de una moneda. Al presionar un botón, se genera aleatoriamente "Cara" o "Sello" (cruz), 
y se muestra el resultado junto con una imagen representativa.

🎯 Objetivo

Brindar una forma visual y divertida de simular el lanzamiento de una moneda, ideal para juegos, decisiones rápidas o demostraciones educativas.

🧰 Tecnologías utilizadas

* Python 3.x
* tkinter para la interfaz gráfica
* PIL (Pillow) para mostrar imágenes

🚀 Cómo ejecutar el programa

1) Asegúrate de tener Python instalado.
2) Instala la librería Pillow si no la tienes:
   'pip install pillow'
3) Coloca las imágenes Cara_100.png y Sello_100.png en el mismo directorio que el archivo .py.
4) Ejecuta el script:
   'python nombre_del_archivo.py'
5) Haz clic en el botón Generar para lanzar la moneda.

📦 Archivos necesarios

Asegúrate de incluir los siguientes archivos en tu repositorio:

Archivo --> 	Descripción
Cara_100.png	--> Imagen que representa el lado "Cara"
Sello_100.png	--> Imagen que representa el lado "Sello"
main.py	--> Código fuente del lanzador de moneda

🧠 Lógica del programa

Se genera aleatoriamente un valor entre "Cara" y "Sello".
Se abre una nueva ventana con el resultado textual y gráfico.
Se mantiene la referencia de la imagen para evitar problemas con el recolector de basura de Python.

📄 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.
