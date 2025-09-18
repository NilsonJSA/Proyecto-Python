"""
Proyecto final consola
"""
#Importaciones
from os import system
from prettytable import PrettyTable #Imprime tablas automáticamente
#Librería que ayuda a generar cuadros automáticamente tipo como base de datos
from string import punctuation
"""
Links: https://youtu.be/kBT1g4ANQcE?si=puthNqaRTqtrXwUh
https://youtu.be/QL6nf_uZJ0w?si=Cz91KXtC0IqQ26rL
https://pypi.org/project/prettytable/
https://zetcode.com/python/prettytable/
"""

#Código de verificación no números
"""def input_no_numero(cadena):
    for caracter in cadena:
        if caracter.isdigit() or caracter.isspace(): #este ultimo ayudara a validar si hay espacios o no
            return False      # Hemos encontrado un número, es Falso que no contenga
    # Hemos acabado de procesar la cadena sin encontrar números
    return True"""

#Código de verificación no números 2.0
def input_no_numero(cadena):
    #Elimina todo lso espacios en blanco, tanto inicio como el final.
    cadena_sin_espacios = cadena.strip()
    #Verificar si la cadena esta vacía.
    if not cadena_sin_espacios:
        return False
    #Verifica si la cadena contiene algún numero
    for caracter in cadena_sin_espacios:
        if caracter.isdigit():
            return False
    return True

#Verificador para ver si el texto no contiene símbolos
def validador_Simbolos(cadena1):
    #if any([True if i in punctuation else False for i in cadena1])
    for char in cadena1:
        if char in punctuation:
            return False
    return True

#Base de datos
Historial =[]

#Ejemplo de menu básico
Inventario = [
    {"Producto": "Camisa manga larga", "Precio": 70.99, "Cantidad": 10},
    {"Producto": "Camisola de niño", "Precio": 25.90, "Cantidad": 50},
    {"Producto": "Camiseta color negro", "Precio": 50, "Cantidad": 67},
    {"Producto": "Camiseta color blanco", "Precio": 50, "Cantidad": 45},
    {"Producto": "Gorra NIKE", "Precio": 30.70, "Cantidad": 33},
]

#Menu
while True:#Ciclo secundario
    while True: #Ciclo para así evitar que se rompa el código.
        system("cls")
        print("\033[0,m" +"☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰  Menú ☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰\n")

        print("1) Compra. 🛍️\n2) Historial. 📒\n3) Inventario. 🚚\n4) Añadir producto. 📦\n5) Salir. 🔐")
        try:
            Opc = int(input("\nEscriba la opción del numero por favor: "))
            #system("cls")
            break
        except ValueError as e:
            print("\033[0;31m" + f"\n📢 Error 🚫 {e}, 🤖 vuélvalo a intentar." + "\033[0;m")
            system('pause')
            system("cls")

    if Opc == 5:
        print("\033[0;36m" + "\nGracias por utilizarnos. 😁" + "\033[0,m")
        system('pause')
        exit()
    elif Opc == 1:
        #lista y diccionario que se reiniciaran al volver a entrar
        Datos={}
        Articulo=[]
        system('cls')
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰ Compra ☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰\n")
        #Código de pago
        #https://es.stackoverflow.com/questions/514799/duda-sobre-la-funcionalidad-del-try-except
        while True:#Ciclo de anti-números texto.
            Nombre= input("\nEscriba el nombre del cliente: ").capitalize()
            if not input_no_numero(Nombre) or not validador_Simbolos(Nombre):
                print(f'\nNúmeros, espacios o símbolos encontrados "{Nombre}", vuélvalo a intentar.')
                system('pause')
            else:
                break

        while True: #Impresión de inventario
            system("cls")
            print("Inventario:")
            for producto in Inventario:
                print(f"\033[1;32m Producto:\033[0;m {producto['Producto']} \033[1;32m - Precio: $\033[0;m {producto['Precio']:.2f} \033[1;32m - Cantidad disponible: \033[0;m {producto['Cantidad']}")

            while True: 
                try:
                    cantidadItems = int(input("\nEscriba la cantidad de artículos que esta comprando: "))
                    if cantidadItems > 0:
                        break
                    else:
                        print('\033[0;31m' + '\n📢 Error 🚫 "no puede poner 0 cantidad o negativos", 🤖 vuélvalo a intentar.\n' + '\033[0;m')
                        system('pause')
                except ValueError as e:
                    print("\033[0;31m" + f"\n📢 Error 🚫 {e}, 🤖 vuélvalo a intentar.\n" + "\033[0;m")
                    system("pause")

            for i in range(cantidadItems): # Registro de cada producto a comprar
                while True:
                    Producto = input(f"\nNombre de Articulo {i + 1} = ").lower()
                    # Verificar que el producto esté en el inventario
                    if any(item["Producto"].lower() == Producto for item in Inventario):
                        while True:
                            try:
                                Cantidad = int(input(f"\nEscriba la cantidad de {Producto} que está comprando: "))
                                # Verificar que hay suficiente cantidad en el inventario
                                if Cantidad > 0:
                                    if any(item["Producto"].lower() == Producto and item["Cantidad"] >= Cantidad for item in Inventario):
                                        break
                                    else:
                                        print("\033[0;31m" + f"\n📢 Error 🚫 No hay suficiente cantidad disponible, 🤖 vuélvalo a intentar.\n" + "\033[0;m")
                                else:
                                    print('\033[0;31m' + '\n📢 Error 🚫 "no puede poner 0 cantidad o negativos", 🤖 vuélvalo a intentar.\n' + '\033[0;m')
                            except ValueError as e:
                                print("\033[0;31m" + f"\n📢 Error 🚫 {e}, 🤖 vuélvalo a intentar.\n" + "\033[0;m")
                                system("Pause")

                        # Obtener el precio del producto
                        Precio = next(item['Precio'] for item in Inventario if item['Producto'].lower() == Producto)
                        
                        for item in Inventario:
                            if item["Producto"].lower() == Producto:
                                Precio = item['Precio']
                                break
                        # Actualizar la cantidad disponible en el inventario
                        for item in Inventario:
                            if item['Producto'].lower() == Producto:
                                item["Cantidad"] -= Cantidad
                        Articulo.append({"Producto": Producto, "Precio": Precio, "Cantidad": Cantidad})
                        break
                    else:
                        print("\033[0;31m" + f"\n📢 Error 🚫 Producto no encontrado en el inventario, 🤖 vuélvalo a intentar.\n" + "\033[0;m")
                        system("pause")
            break

        print("<--------------------------------------------------->")
        print("<--------------- Calculo de total --------------->")
        print("<--------------------------------------------------->\n")

#Suma de todos los productos
        Total = 0
        for k in Articulo:
            Total += k['Precio'] * k['Cantidad']
        
        print("\033[0;33m" + "El total de las compra sera de" + "\033[0;m", Total)

        Datos = {"Cliente": Nombre, "Compras": Articulo, "CompraFinal": Total}
        print("=====================================================\n")
        Historial.append(Datos)
        system('pause')
        system("cls")

    elif Opc == 2:
        system('cls')
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰ Historial ☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        #Código de historial.
        if not Historial:
            print("\n☹️  Historial vacío ☹️\n")
            system("pause")
        else:
            Historial_tabla = PrettyTable() #Activar librería
            Historial_tabla.field_names = ["\033[1;36m" +"cliente" +'\033[0;m ', '\033[1;36m '+ "Compras" + '\033[0;m ', '\033[1;26m '+"Total" + '\033[0;m ']
            #Títulos de cada columna
            for compra in Historial:# Generación de filas con la lista Historial
                compras = ', '.join([f'{item["Producto"]} x {item["Cantidad"]}' for item in compra['Compras']])
                #descuentos = ', '.join([f"{item['Producto']} - ${item['Descuento']:.2f}" for item in compra['DescuentoCompra']])
                
                Historial_tabla.add_row([compra['Cliente'], compras, f"${compra['CompraFinal']:.2f}"])
            print(Historial_tabla)#Impresión de filas y columnas.
            system('pause')
            system("cls")
    elif Opc == 3:
        system('cls')
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰ Inventario ☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰\n")
        for producto in Inventario:
            print(f"\033[1;32m Producto:\033[0;m {producto['Producto']} \033[1;32m - Precio: \033[0;m ${producto['Precio']:.2f} \033[1;32m - Cantidad disponible: \033[0;m {producto['Cantidad']}\n")
        system("pause")

    elif Opc == 4:
        system('cls')
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰ Añadir Producto ☰☰☰☰☰☰☰☰☰☰☰☰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰\n")

        for producto in Inventario:
            print(f"\033[1;32m Producto:\033[0;m {producto['Producto']} \033[1;32m - Precio: \033[0;m ${producto['Precio']:.2f} \033[1;32m - Cantidad disponible: \033[0;m {producto['Cantidad']}\n")

        nombre_producto = input("\nIngrese el nombre del nuevo producto: ").strip().capitalize()  # Eliminar espacios en blanco al inicio y al final

        # Verificar si el producto ya existe en el inventario
        producto_existente = next((item for item in Inventario if item["Producto"].lower() == nombre_producto.lower()), None)

        if producto_existente:
            print(f"\nEl producto '{nombre_producto}' ya existe en el inventario. La cantidad se actualizará.\n")
            while True:
                try:
                    cantidad_producto = int(input("\nIngrese la cantidad del nuevo producto: "))
                    if cantidad_producto <= 0:
                        print('\033[0;31m' + '\n📢 Error 🚫 "no puede poner 0 cantidad o negativos", 🤖 vuélvalo a intentar.\n' + '\033[0;m')
                        system('pause')
                    else:
                        break
                except ValueError as e:
                    print("\033[0;31m" + f"\n📢 Error 🚫 {e}, 🤖 vuélvalo a intentar.\n" + "\033[0;m")
                    system("Pause")
            producto_existente["Cantidad"] += cantidad_producto
        else:
            # Agregar el nuevo producto al inventario
            while True:
                try:
                    cantidad_producto = int(input("\nIngrese la cantidad del nuevo producto: "))
                    if cantidad_producto <= 0:
                        print('\033[0;31m' + '\n📢 Error 🚫 "no puede poner 0 cantidad o negativos", 🤖 vuélvalo a intentar.\n' + '\033[0;m')
                        system('pause')
                    else:
                        break
                except ValueError as e:
                    print("\033[0;31m" + f"\n📢 Error 🚫 {e}, 🤖 vuélvalo a intentar.\n" + "\033[0;m")
                    system("Pause")
            
            while True:
                try:
                    precio_producto = float(input("\nIngrese el precio unitario del nuevo producto: "))
                    if precio_producto <= 0:
                        print('\033[0;31m' + '\n📢 Error 🚫 "no puede poner 0 cantidad o negativos", 🤖 vuélvalo a intentar.\n' + '\033[0;m')
                        system('pause')
                    else:
                        break
                except ValueError as e:
                    print("\033[0;31m" + f"\n📢 Error 🚫 {e}, 🤖 vuélvalo a intentar.\n" + "\033[0;m")
                    system("Pause")
            
            Inventario.append({"Producto": nombre_producto, "Precio": precio_producto, "Cantidad": cantidad_producto})
            print(f"\nEl producto '{nombre_producto}' ha sido añadido al inventario.")
        system('pause')


    else:
        print("\033[0;31m]" + "\n🔎 Ponga la opción correcta. 📎 Vuélvalo a intentar." + "\033[0;m]")
        system('pause')