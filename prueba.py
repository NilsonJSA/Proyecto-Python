import os
from tkinter import *

# Obtén la ruta del directorio actual
ruta_actual = os.getcwd()

# Añade el subdirectorio y el nombre del archivo a la ruta
ruta_imagen = os.path.join(ruta_actual, 'Fotos', 'icons8-warehouse-100.png')

# Ahora puedes usar `ruta_imagen` en tu código
imagen = PhotoImage(file=ruta_imagen)
