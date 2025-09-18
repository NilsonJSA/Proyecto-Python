"""
Proyecto final, inventario.
"""
from tkinter import *
from tkinter import ttk, messagebox
from string import punctuation
import os

#Inventario de ejemplo
producto_Inventario = [
    {"Producto": "Laptop", "Precio": 570, "Cantidad": 15},
    {"Producto": "Mouse", "Precio": 14, "Cantidad": 100},
    {"Producto": "Teclado", "Precio": 66, "Cantidad": 50},
]
#Lista de las ventas realizadas
Historial_Ventas = []

# Obtén la ruta del directorio actual
ruta_actual = os.getcwd()

#Verificador para ver si un texto contiene algún numero dentro
def input_no_numero(cadena): #Verificador para ver si el nombre no lleva numeros
    for caracter in cadena:
        if caracter.isdigit():
            return False      # Hemos encontrado un número, es Falso que no contenga
    # Hemos acabado de procesar la cadena sin encontrar números
    return True

def validador_Simbolos(cadena1):
    #if any([True if i in punctuation else False for i in cadena1])
    for char in cadena1:
        if char in punctuation:
            return False
    return True

#Clase Inventario
class InventarioApp:
    def MensajeSalida(self): #Mensaje para cuando se saldrá del programa.
        Salir = messagebox.askquestion("Salir", "¿Desea salir?")
        if Salir == 'yes':
            ventana.quit()
            #ventana.destroy()

    def MensajeInfo(self): #Mensaje del creador del programa.
        messagebox.showinfo('About', "Este proyecto fue creado por Nilson José Saballos Arana, futuro ingeniero en Sistemas.")
    
    def ventanaInventario(self): #Ventana para poder ver el inventario y los menu que contiene
        V1 = Toplevel(ventana)
        V1.title('Inventario')
        #titulo = Label(V1, text='Inventario\n')
        V1.geometry('500x200')

        #ruta_imagen = os.path.join(ruta_actual, 'Proyect_Inventario', 'Fotos', 'icons8-lista-de-portapapeles-64.png')
        #imagen = PhotoImage(file='Fotos\\icons8-lista-de-portapapeles-64.png')

        #Crear un frame para contener la lista de productos
        frame = Frame(V1)
        frame.pack(fill=BOTH, expand=True)

        # Crear una barra de desplazamiento vertical
        scrollbar = Scrollbar(frame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Crear una lista para mostrar los productos
        lista_productos = Listbox(frame, yscrollcommand=scrollbar.set)
        lista_productos.pack(fill=BOTH, expand=True)

        scrollbar.config(command=lista_productos.yview)

        #titulo.pack()
        #V1.iconphoto(False, imagen)

        for producto in producto_Inventario:
            # Agregar cada producto a la lista
            lista_productos.insert(END, f"Producto: {producto['Producto']} - Precio: ${producto['Precio']:.2f} - Cantidad disponible: {producto['Cantidad']}")

    def ventanaVenta(self):#Ventana para poder realizar las ventas y sus procesos
        venta_window = Toplevel(ventana)
        venta_window.title('Venta de productos')
        venta_window.geometry('300x220')
        
        venta = {'Cliente': '', 'Productos': [], 'Cantidad':0, 'Precio Total': 0}

        nombre_label = Label(venta_window, text="Nombre:")
        nombre_label.grid(row=0, column=0, padx=10, pady=10)
        nombre_entry_venta = Entry(venta_window)
        nombre_entry_venta.grid(row=0, column=1, padx=10, pady=10)

        producto_label = Label(venta_window, text="Producto:")
        producto_label.grid(row=1, column=0, padx=10, pady=10)
        producto_entry_venta = Entry(venta_window)
        producto_entry_venta.grid(row=1, column=1, padx=10, pady=10)

        cantidad_label = Label(venta_window, text="Cantidad:")
        cantidad_label.grid(row=2, column=0, padx=10, pady=10)
        cantidad_entry_venta = Entry(venta_window)
        cantidad_entry_venta.grid(row=2, column=1, padx=10, pady=10)

        def agregar_producto():#Para poner el producto que se esta buscando en venta.
            producto = producto_entry_venta.get().capitalize()
            cantidad = cantidad_entry_venta.get()
            nombre = nombre_entry_venta.get().capitalize()

            if not input_no_numero(nombre) or not validador_Simbolos(nombre):
                messagebox.showerror('Error', f'{nombre} contiene número o símbolos, vuélvalo a intentar')
                return

            if not nombre:
                messagebox.showerror("Error", "Por favor, ingrese el nombre del cliente.")
                return

            if not producto or not cantidad:
                messagebox.showerror("Error", "Por_venta favor, ingrese el nombre del producto y la cantidad.")
                return

            try:
                cantidad = int(cantidad)
                if cantidad <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número entero positivo.")
                return
            
            # Verificar si el producto está en el inventario
            producto_encontrado = False
            for item_inventario in producto_Inventario:
                if item_inventario['Producto'].capitalize() == producto:  # Convertir a minúsculas para comparar
                    producto_encontrado = True
                    if cantidad > item_inventario['Cantidad']:
                        messagebox.showerror("Error", f"No hay suficiente cantidad disponible de {producto} en el inventario.")
                        return
                    break

            if not producto_encontrado:
                messagebox.showerror("Error", f"No se encontró el producto {producto} en el inventario.")
                return

            venta['Productos'].append({'Producto': producto, 'Cantidad': cantidad})
            producto_entry_venta.delete(0, END)
            cantidad_entry_venta.delete(0, END)

            # Actualizar la cantidad total de productos en la venta
            venta['Cantidad'] += cantidad

        def finalizar_venta():
            nombre = nombre_entry_venta.get()

            if not venta['Productos']:  # Verificar si no se han agregado productos
                messagebox.showerror("Error", 'Debes agregar al menos un producto para finalizar la venta.')
                return

            precio_total = 0
            for producto_venta in venta['Productos']:
                for item_inventario in producto_Inventario:
                    if item_inventario['Producto'] == producto_venta['Producto']:
                        item_inventario['Cantidad'] -= producto_venta['Cantidad']
                        precio_total += item_inventario['Precio'] * producto_venta['Cantidad']

            venta['Precio Total'] = precio_total
            venta['Cliente'] = nombre
            Historial_Ventas.append(venta)

            """errores = []  # Lista para almacenar mensajes de error

            for producto_venta in venta['Productos']:
                producto_encontrado = False
                for item_inventario in producto_Inventario:
                    if item_inventario['Producto'] == producto_venta['Producto']:
                        producto_encontrado = True
                        if producto_venta['Cantidad'] > item_inventario['Cantidad']:
                            errores.append(f"No hay suficiente cantidad disponible de {producto_venta['Producto']} en el inventario.")
                        break
                if not producto_encontrado:
                    errores.append(f"No se encontró el producto {producto_venta['Producto']} en el inventario.")

            if errores:
                messagebox.showerror("Error", "\n".join(errores))
            else:"""
            messagebox.showinfo("Venta exitosa", f"Venta realizada con éxito. Precio total: ${precio_total}")
            venta_window.destroy()



        agregar_producto_button = Button(venta_window, text="Agregar Producto", command=agregar_producto)
        agregar_producto_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        finalizar_venta_button = Button(venta_window, text="Finalizar Venta", command=finalizar_venta)
        finalizar_venta_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def ventanaHistorial(self):
        historial_ventana = Toplevel(ventana)
        historial_ventana.title('Historial')

        historial_ventana.geometry('500x400')

        # Crear un frame para contener el historial de ventas
        frame = Frame(historial_ventana)
        frame.pack(fill=BOTH, expand=True)

        # Crear una barra de desplazamiento vertical
        scrollbar = Scrollbar(frame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Crear un text widget para mostrar el historial de ventas
        historial_texto = Text(frame, yscrollcommand=scrollbar.set)
        historial_texto.pack(fill=BOTH, expand=True)

        scrollbar.config(command=historial_texto.yview)

        """titulo = Label(historial_ventana, text='Historial de ventas', font=("Arial Bold", 16))
        titulo.pack()"""

        # Configurar etiquetas de estilo
        historial_texto.tag_configure("title", font=("Arial", 16, "bold"))

        if not Historial_Ventas:
            historial_texto.insert(END, "\t\tNo hay ventas registradas.", 'Title')
        else:
            for i, venta in enumerate(Historial_Ventas, start=1):
                historial_texto.insert(END, f"Venta {i}:\n", "title")
                historial_texto.insert(END, f"Nombre: {venta['Cliente']}\n")
                historial_texto.insert(END, "Productos:\n")
                for item in venta['Productos']:
                    historial_texto.insert(END, f"   - {item['Cantidad']} {item['Producto']}\n")
                historial_texto.insert(END, f"Cantidad total: {venta['Cantidad']}\n")
                historial_texto.insert(END, f"Precio Total: ${venta['Precio Total']:.2f}\n")
                historial_texto.insert(END, "\n")

    def ventanaAgregarNuevo(self):
        ventana_agregar_nuevo = Toplevel(ventana)
        ventana_agregar_nuevo.title('Agregar Nuevo Producto')
        ventana_agregar_nuevo.geometry('300x180')

        nombre_label = Label(ventana_agregar_nuevo, text="Nombre del Producto:")
        nombre_label.grid(row=0, column=0, padx=10, pady=10)
        nombre_entry = Entry(ventana_agregar_nuevo)
        nombre_entry.grid(row=0, column=1, padx=10, pady=10)

        cantidad_label = Label(ventana_agregar_nuevo, text="Cantidad:")
        cantidad_label.grid(row=1, column=0, padx=10, pady=10)
        cantidad_entry = Entry(ventana_agregar_nuevo)
        cantidad_entry.grid(row=1, column=1, padx=10, pady=10)

        precio_label = Label(ventana_agregar_nuevo, text="Precio Unitario:")
        precio_label.grid(row=2, column=0, padx=10, pady=10)
        precio_entry = Entry(ventana_agregar_nuevo)
        precio_entry.grid(row=2, column=1, padx=10, pady=10)

        def agregar_nuevo():
            nombre = nombre_entry.get().capitalize()
            cantidad = cantidad_entry.get()
            precio = precio_entry.get()

            if not input_no_numero(nombre) or not validador_Simbolos(nombre):
                messagebox.showerror('Error', f'{nombre} contiene numero, vuélvalo a intentar')
                return

            if not nombre or not cantidad or not precio:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
                return

            try:
                cantidad = int(cantidad)
                precio = float(precio)
                if cantidad <= 0 or precio <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "La cantidad y el precio deben ser números positivos.")
                return

            producto_Inventario.append({"Producto": nombre, "Precio": precio, "Cantidad": cantidad})
            messagebox.showinfo("Producto Agregado", f"Se agregó el producto {nombre} al inventario.")
            ventana_agregar_nuevo.destroy()

        agregar_button = Button(ventana_agregar_nuevo, text="Agregar", command=agregar_nuevo)
        agregar_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def ventanaAgregarExistente(self):
        ventana_agregar_existente = Toplevel(ventana)
        ventana_agregar_existente.title('Agregar Producto Existente')
        ventana_agregar_existente.geometry('300x130')

        nombre_label = Label(ventana_agregar_existente, text="Nombre del Producto:")
        nombre_label.grid(row=0, column=0, padx=10, pady=10)
        nombre_entry = Entry(ventana_agregar_existente)
        nombre_entry.grid(row=0, column=1, padx=10, pady=10)

        cantidad_label = Label(ventana_agregar_existente, text="Cantidad:")
        cantidad_label.grid(row=1, column=0, padx=10, pady=10)
        cantidad_entry = Entry(ventana_agregar_existente)
        cantidad_entry.grid(row=1, column=1, padx=10, pady=10)

        def agregar_existente():
            nombre = nombre_entry.get()
            cantidad = cantidad_entry.get()

            if not nombre or not cantidad:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
                return

            try:
                cantidad = int(cantidad)
                if cantidad <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número entero positivo.")
                return

            producto_encontrado = False
            for producto in producto_Inventario:
                if producto['Producto'] == nombre:
                    producto['Cantidad'] += cantidad
                    messagebox.showinfo("Producto Actualizado", f"Se agregaron {cantidad} unidades del producto {nombre} al inventario.")
                    producto_encontrado = True
                    break

            if not producto_encontrado:
                messagebox.showerror("Error", f"No se encontró el producto {nombre} en el inventario.")

            ventana_agregar_existente.destroy()

        agregar_button = Button(ventana_agregar_existente, text="Agregar", command=agregar_existente)
        agregar_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


        def agregar_existente():
            nombre = nombre_entry.get()
            cantidad = cantidad_entry.get()

            if not nombre or not cantidad:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
                return

            try:
                cantidad = int(cantidad)
                if cantidad <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número entero positivo.")
                return

            producto_encontrado = False
            for producto in producto_Inventario:
                if producto['Producto'] == nombre:
                    producto['Cantidad'] += cantidad
                    messagebox.showinfo("Producto Actualizado", f"Se agregaron {cantidad} unidades del producto {nombre} al inventario.")
                    producto_encontrado = True
                    break

            if not producto_encontrado:
                messagebox.showerror("Error", f"No se encontró el producto {nombre} en el inventario.")

            ventana_agregar_existente.destroy()

        agregar_button = Button(ventana_agregar_existente, text="Agregar", command=agregar_existente)
        agregar_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

Comando_Inventario = InventarioApp()

ventana = Tk()
ventana.title("Inventario")
#ruta_imagen1 = os.path.join(ruta_actual, 'Proyect_Inventario', 'Fotos', 'icons8-warehouse-100.png')
#imagen = PhotoImage(file='Fotos\\icons8-warehouse-100.png')

#ventana.iconphoto(False, imagen)

# Menu de la ventana
menuBar = Menu(ventana)
ventana.config(menu=menuBar)

# Menu secundario de menu general
SegundoMenu = Menu(menuBar, tearoff=0)

# Menu secundario (Los menus internos debe de ponerse en donde ira la prioridad)
TercerMenu = Menu(SegundoMenu, tearoff=0)  # Tercer menu dentro de Agregar.
TercerMenu.add_command(label='Nuevo', command=Comando_Inventario.ventanaAgregarNuevo)
TercerMenu.add_separator()
TercerMenu.add_command(label='Producto existente', command=Comando_Inventario.ventanaAgregarExistente)

SegundoMenu.add_cascade(label='Agregar', menu=TercerMenu)
SegundoMenu.add_separator()
SegundoMenu.add_command(label='Vender', command=Comando_Inventario.ventanaVenta)
SegundoMenu.add_separator()
SegundoMenu.add_command(label='Salir', command=Comando_Inventario.MensajeSalida)

SegundoMenu_Historial = Menu(menuBar, tearoff=0)
SegundoMenu_Historial.add_command(label='Mostrar Historial', command=Comando_Inventario.ventanaHistorial)

# Menu secundario de menu inventario
SegundoMenu_Inventario = Menu(menuBar, tearoff=0)
SegundoMenu_Inventario.add_command(label='Historial', command=Comando_Inventario.ventanaHistorial)
SegundoMenu_Inventario.add_separator()
SegundoMenu_Inventario.add_command(label='Almacenado', command=Comando_Inventario.ventanaInventario)

# Menu de Agregar
menuBar.add_cascade(label='General', menu=SegundoMenu)
menuBar.add_cascade(label='Inventario', menu=SegundoMenu_Inventario)
menuBar.add_command(label='About', command=Comando_Inventario.MensajeInfo)

"""#Pestañas
Pestaña= ttk.Notebook(ventana)
#Crear tableros
PestañaInventario = ttk.Frame(Pestaña)
PestañaHistorial = ttk.Frame(Pestaña)
#Nombres paneles
Pestaña.add(PestañaInventario, text='Inventario')
Pestaña.add(PestañaHistorial, text='Historial')
#etiquetas
lbl1 = Label(PestañaInventario, text= 'Inventario de productos')
lbl1.grid(column=0, row=0)

lbl2 = Label(PestañaHistorial, text= 'Registros de productos vendidos')
lbl2.grid(column=0, row=0)

#configuración
Pestaña.pack(expand=1, fill='both')"""

# Tamaño de ventana
ventana.geometry('1000x600')

#Imagen de fondo
#ruta_imagen_Fondo = os.path.join(ruta_actual,'Proyect_Inventario' ,'Fotos', 'IM.png')
#imagen_fondo = PhotoImage(file='Fotos\\IM.png')

# Crear un widget de Label para mostrar la imagen de fondo
#label_fondo = Label(ventana, image= imagen_fondo)
#label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
#Configuración de tamaño
#label_fondo.config(width=00, height=00)

#label_fondo.image = imagen_fondo  # Mantener referencia a la imagen para evitar que sea eliminada por el recolector de basura

# Crear un widget de Label para mostrar un mensaje de bienvenida
label_bienvenida = Label(ventana, text="¡Bienvenido a NGamer!", font=("Arial", 18))
label_bienvenida.pack(pady=20)

ventana.mainloop()