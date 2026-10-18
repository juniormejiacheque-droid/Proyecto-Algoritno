   elif opcion == "3":
        print("\n--- NUEVA ORDEN DE TRABAJO ---")
        num_orden = input("Número de orden: ")
        placa = input("Placa del carro: ")
        mano_obra = float(input("Costo de mano de obra: "))
        
       # Cálculo sencillo con el 12% de IVA
        total = mano_obra * 1.12
        estado = "Recibida"
        
        archivo = open("ordenes.txt", "a")
        archivo.write(num_orden + "," + placa + "," + str(total) + "," + estado + "\n")
        archivo.close()
        
        print("¡Orden creada correctamente!")
        print("Estado actual: " + estado)
        print("Total a pagar con IVA: Q" + str(total))
        
         elif opcion == "4":
        print("\nSaliendo del programa... ¡Mucho éxito en la defensa!")
        continuar = False
        
    else:
      print("\n[!] Opción incorrecta, ingresa un número del 1 al 4.")
      
        print("\n[!] Opción incorrecta, ingresa un número del 1 al 4.")

