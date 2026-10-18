print("========================================")
print("      UNIVERSIDAD MARIANO GÁLVEZ")
print("      SISTEMA DE TALLER AUTOMOTRIZ")
print("========================================")
print(" Curso: Ingeniería en Sistemas")
print(" Integrantes: Junior y equipo")
print("========================================")
input("Presiona Enter para entrar al sistema...")

continuar = True

while continuar == True:
    print("\n================================")
    print("        MENÚ TALLER             ")
    print("================================")
    print("1. Registrar Cliente")
    print("2. Registrar Repuesto")
    print("3. Crear Orden de Trabajo")
    print("4. Salir")
    
        opcion = input("Elige una opción (1-4): ")
OPCIÓN 1: CLIENTES (Añadir dentro del while, después del input de opción)
    if opcion == "1":
        print("\n--- REGISTRAR CLIENTE ---")
        nit = input("Ingresa el NIT: ")
        nombre = input("Ingresa el Nombre: ")
        
        # Guardar en archivo de texto plano de forma sencilla
        archivo = open("clientes.txt", "a")
        archivo.write(nit + "," + nombre + "\n")
        archivo.close()
        print("¡Cliente guardado con éxito!")
