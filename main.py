import os


def inicializar_archivos():
  # Lista de archivos de texto que usa el sistema del taller
  archivos_necesarios = [
      "clientes.txt",
      "mecanicos.txt",
      "ordenes.txt",
      "repuestos.txt",
      "servicios.txt",
      "vehiculos.txt",
  ]
  # Verifica si existen; si no, los crea vacíos para blindar el programa ante cualquier ausencia
  for archivo in archivos_necesarios:
    if not os.path.exists(archivo):
      with open(archivo, "w") as f:
        pass


def mostrar_caratula():
  print("==========================================")
  print("      UNIVERSIDAD MARIANO GÁLVEZ DE GUATEMALA     ")
  print("           COATEPEQUE QUETZALTENANGO           ")
  print("PROYECTO A BASE DE UN SISTEMA DE TALLER AUTOMOTRIZ        ")
  print("==========================================")
  print(" Facultad: Ingeniería en Sistemas            ")
  print(" Materia: Algoritmo")
  print(" Ingeniero: Demshin Coutiño")
  print(
      " Integrantes: Maria Fernanda Delgado Perez, Angel Gerardo Ochoa Lopez,"
      " Diego Fernando Pascual Coronado y Junior Fernando Mejia Cheque"
  )
  print(" Semestre/Ciclo: Segundo Semestre de 2026")
  print(" Seccion: B")
  print("==========================================")
  input("Presiona Enter para entrar al sistema...")


def registrar_cliente():
  print("\n--- 1. REGISTRAR CLIENTE ---")

  while True:
    nit_cliente_ingresado = input(
        "Ingresa el NIT (9 dígitos exactos, solo números): "
    )

    if not (nit_cliente_ingresado.isdigit() and len(nit_cliente_ingresado) == 9):
      print("[!] Error: El NIT debe contener exactamente 9 dígitos numéricos.")
      continue

    bandera_nit_repetido = False
    try:
      descriptor_archivo_lectura = open("clientes.txt", "r")
      for linea_actual_archivo in descriptor_archivo_lectura:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 1
            and lista_datos_separados[0] == nit_cliente_ingresado
        ):
          bandera_nit_repetido = True
          break
      descriptor_archivo_lectura.close()
    except FileNotFoundError:
      pass

    if bandera_nit_repetido:
      print("[!] Error: Este NIT ya se encuentra registrado en el sistema.")
      continue
    break

  while True:
    nombre_completo_cliente = input(
        "Ingresa el Nombre completo (exactamente 4 palabras válidas): "
    ).strip()

    if not nombre_completo_cliente:
      print("[!] Error: El nombre no puede estar vacío.")
      continue

    palabras_nombre_usuario = nombre_completo_cliente.split()

    if len(palabras_nombre_usuario) != 4:
      print("[!] Error: Debes ingresar exactamente 4 palabras.")
      continue

    estado_nombre_valido = True
    for palabra_individual in palabras_nombre_usuario:
      if not palabra_individual.isalpha():
        estado_nombre_valido = False
        break

    if not estado_nombre_valido:
      print("[!] Error: El nombre solo debe contener letras.")
      continue

    bandera_garabato_detectado = False
    caracteres_vocales = "aeiouáéíóúAEIOU"
    for palabra_individual in palabras_nombre_usuario:
      contador_consonantes_seguidas = 0
      for letra_actual in palabra_individual:
        if letra_actual not in caracteres_vocales:
          contador_consonantes_seguidas += 1
          if contador_consonantes_seguidas >= 4:
            bandera_garabato_detectado = True
            break
        else:
          contador_consonantes_seguidas = 0
      if bandera_garabato_detectado:
        break

    if bandera_garabato_detectado:
      print(
          "[!] Error: El texto ingresado parece un garabato o no tiene"
          " estructura de nombre real."
      )
      continue

    bandera_palabra_repetida = False
    indice_recorrido = 0
    while indice_recorrido < len(palabras_nombre_usuario) - 1:
      if (
          palabras_nombre_usuario[indice_recorrido].lower()
          == palabras_nombre_usuario[indice_recorrido + 1].lower()
      ):
        bandera_palabra_repetida = True
        break
      indice_recorrido = indice_recorrido + 1

    if bandera_palabra_repetida:
      print("[!] Error: No se permite repetir la misma palabra consecutivamente.")
      continue

    estado_estructura_palabras = True
    for palabra_individual in palabras_nombre_usuario:
      palabra_en_minusculas = palabra_individual.lower()
      tiene_vocal_actual = any(
          caracter_v in caracteres_vocales for caracter_v in palabra_en_minusculas
      )
      tiene_consonante_actual = any(
          caracter_v not in caracteres_vocales
          for caracter_v in palabra_en_minusculas
      )
      if not (tiene_vocal_actual and tiene_consonante_actual):
        estado_estructura_palabras = False
        break

    if not estado_estructura_palabras:
      print(
          "[!] Error: Cada palabra debe contener al menos una vocal y"
          " consonantes."
      )
      continue

    bandera_nombre_repetido = False
    try:
      descriptor_archivo_lectura = open("clientes.txt", "r")
      for linea_actual_archivo in descriptor_archivo_lectura:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 2
            and lista_datos_separados[1].lower()
            == nombre_completo_cliente.lower()
        ):
          bandera_nombre_repetido = True
          break
      descriptor_archivo_lectura.close()
    except FileNotFoundError:
      pass

    if bandera_nombre_repetido:
      print("[!] Error: Este nombre ya se encuentra registrado en el sistema.")
      continue

    break

  descriptor_archivo_escritura = open("clientes.txt", "a")
  descriptor_archivo_escritura.write(
      nit_cliente_ingresado + "," + nombre_completo_cliente + "\n"
  )
  descriptor_archivo_escritura.close()
  print("¡Cliente registrado con éxito!")


def registrar_vehiculo():
  print("\n--- 2. REGISTRAR VEHÍCULO Y ASOCIAR ---")

  while True:
    nit_propietario_buscado = input(
        "Ingresa el NIT del cliente propietario (9 dígitos exactos): "
    )
    if nit_propietario_buscado.isdigit() and len(nit_propietario_buscado) == 9:
      break
    print("[!] Error: El NIT debe contener exactamente 9 dígitos numéricos.")

  bandera_cliente_encontrado = False
  try:
    descriptor_archivo_clientes = open("clientes.txt", "r")
    for linea_actual_archivo in descriptor_archivo_clientes:
      lista_datos_separados = linea_actual_archivo.strip().split(",")
      if (
          len(lista_datos_separados) >= 2
          and lista_datos_separados[0] == nit_propietario_buscado
      ):
        bandera_cliente_encontrado = True
        print("Propietario asignado: " + lista_datos_separados[1])
        break
    descriptor_archivo_clientes.close()
  except FileNotFoundError:
    pass

  if not bandera_cliente_encontrado:
    print("[!] Error: El NIT no existe. Primero debes registrar al cliente.")
    return

  while True:
    placa_vehiculo_ingresada = input(
        "Ingresa la placa del vehículo (Ej. D123ABC): "
    ).strip()

    if len(placa_vehiculo_ingresada) == 7:
      primer_caracter = placa_vehiculo_ingresada[0]
      digitos_centrales = placa_vehiculo_ingresada[1:4]
      letras_finales = placa_vehiculo_ingresada[4:7]

      if (
          primer_caracter.isupper()
          and primer_caracter.isalpha()
          and digitos_centrales.isdigit()
          and letras_finales.isupper()
          and letras_finales.isalpha()
      ):
        break

    print(
        "[!] Error: Formato incorrecto. Debe iniciar con 1 letra mayúscula,"
        " seguida de 3 números y terminar con 3 letras mayúsculas (Ej:"
        " D123ABC)."
    )

  lista_marcas_disponibles = [
      "Toyota",
      "Honda",
      "Nissan",
      "Mazda",
      "Hyundai",
      "Kia",
      "Ford",
      "Chevrolet",
  ]
  while True:
    print("\n--- MARCAS DISPONIBLES ---")
    indice_marca = 0
    while indice_marca < len(lista_marcas_disponibles):
      print(
          str(indice_marca + 1)
          + ". "
          + lista_marcas_disponibles[indice_marca]
      )
      indice_marca = indice_marca + 1

    opcion_marca_seleccionada = input(
        "Selecciona el número de la marca o escribe el nombre exacto: "
    ).strip()

    marca_vehiculo_resultado = ""
    if opcion_marca_seleccionada.isdigit():
      indice_convertido = int(opcion_marca_seleccionada) - 1
      if 0 <= indice_convertido < len(lista_marcas_disponibles):
        marca_vehiculo_resultado = lista_marcas_disponibles[indice_convertido]
    else:
      for marca_en_lista in lista_marcas_disponibles:
        if marca_en_lista.lower() == opcion_marca_seleccionada.lower():
          marca_vehiculo_resultado = marca_en_lista
          break

    if marca_vehiculo_resultado != "":
      break
    print("[!] Error: Marca no válida o fuera del menú. Inténtalo de nuevo.")

  lista_modelos_disponibles = [
      "Corolla",
      "Civic",
      "Sentra",
      "Mazda 3",
      "Elantra",
      "Rio",
      "Escape",
      "Cruze",
  ]
  while True:
    print("\n--- MODELOS DISPONIBLES ---")
    indice_modelo = 0
    while indice_modelo < len(lista_modelos_disponibles):
      print(
          str(indice_modelo + 1)
          + ". "
          + lista_modelos_disponibles[indice_modelo]
      )
      indice_modelo = indice_modelo + 1

    opcion_modelo_seleccionado = input(
        "Selecciona el número del modelo o escribe el nombre exacto: "
    ).strip()

    modelo_vehiculo_resultado = ""
    if opcion_modelo_seleccionado.isdigit():
      indice_convertido_m = int(opcion_modelo_seleccionado) - 1
      if 0 <= indice_convertido_m < len(lista_modelos_disponibles):
        modelo_vehiculo_resultado = lista_modelos_disponibles[
            indice_convertido_m
        ]
    else:
      for modelo_en_lista in lista_modelos_disponibles:
        if modelo_en_lista.lower() == opcion_modelo_seleccionado.lower():
          modelo_vehiculo_resultado = modelo_en_lista
          break

    if modelo_vehiculo_resultado != "":
      break
    print("[!] Error: Modelo no válido o fuera del menú. Inténtalo de nuevo.")

  descriptor_archivo_vehiculos = open("vehiculos.txt", "a")
  descriptor_archivo_vehiculos.write(
      placa_vehiculo_ingresada
      + ","
      + nit_propietario_buscado
      + ","
      + marca_vehiculo_resultado
      + ","
      + modelo_vehiculo_resultado
      + "\n"
  )
  descriptor_archivo_vehiculos.close()
  print("¡Vehículo registrado, validado y asociado con éxito!")


def registrar_mecanico():
  print("\n--- 3. REGISTRAR MECÁNICO ---")

  while True:
    codigo_mecanico_ingresado = input(
        "Ingresa el código de empleado (Ej. EMP-0001): "
    ).strip()

    if len(codigo_mecanico_ingresado) == 8:
      prefijo_codigo = codigo_mecanico_ingresado[0:3]
      guion_separador = codigo_mecanico_ingresado[3]
      digitos_empleado = codigo_mecanico_ingresado[4:8]

      if (
          prefijo_codigo.isupper()
          and all(caracter_c.isalpha() for caracter_c in prefijo_codigo)
          and guion_separador == "-"
          and digitos_empleado.isdigit()
      ):
        bandera_codigo_repetido = False
        try:
          descriptor_archivo_mecanicos = open("mecanicos.txt", "r")
          for linea_actual_archivo in descriptor_archivo_mecanicos:
            lista_datos_separados = linea_actual_archivo.strip().split(",")
            if (
                len(lista_datos_separados) >= 1
                and lista_datos_separados[0] == codigo_mecanico_ingresado
            ):
              bandera_codigo_repetido = True
              break
          descriptor_archivo_mecanicos.close()
        except FileNotFoundError:
          pass

        if bandera_codigo_repetido:
          print(
              "[!] Error: Este código de empleado ya se encuentra registrado."
          )
          continue
        break

    print(
        "[!] Error: El código debe tener el formato exacto de 8 caracteres (Ej:"
        " EMP-0001)."
    )

  while True:
    nombre_completo_mecanico = input(
        "Ingresa el Nombre del mecánico (exactamente 4 palabras válidas): "
    ).strip()

    if not nombre_completo_mecanico:
      print("[!] Error: El nombre no puede estar vacío.")
      continue

    palabras_nombre_mecanico = nombre_completo_mecanico.split()

    if len(palabras_nombre_mecanico) != 4:
      print("[!] Error: Debes ingresar exactamente 4 palabras.")
      continue

    estado_nombre_mec_valido = True
    for palabra_individual in palabras_nombre_mecanico:
      if not palabra_individual.isalpha():
        estado_nombre_mec_valido = False
        break

    if not estado_nombre_mec_valido:
      print("[!] Error: El nombre solo debe contener letras.")
      continue

    bandera_garabato_mec = False
    caracteres_vocales = "aeiouáéíóúAEIOU"
    for palabra_individual in palabras_nombre_mecanico:
      contador_consonantes_mec = 0
      for letra_actual in palabra_individual:
        if letra_actual not in caracteres_vocales:
          contador_consonantes_mec += 1
          if contador_consonantes_mec >= 4:
            bandera_garabato_mec = True
            break
        else:
          contador_consonantes_mec = 0
      if bandera_garabato_mec:
        break

    if bandera_garabato_mec:
      print(
          "[!] Error: El texto ingresado parece un garabato o no tiene"
          " estructura de nombre real."
      )
      continue

    bandera_palabra_rep_mec = False
    indice_recorrido_m = 0
    while indice_recorrido_m < len(palabras_nombre_mecanico) - 1:
      if (
          palabras_nombre_mecanico[indice_recorrido_m].lower()
          == palabras_nombre_mecanico[indice_recorrido_m + 1].lower()
      ):
        bandera_palabra_rep_mec = True
        break
      indice_recorrido_m = indice_recorrido_m + 1

    if bandera_palabra_rep_mec:
      print("[!] Error: No se permite repetir la misma palabra consecutivamente.")
      continue

    estado_estructura_mec = True
    for palabra_individual in palabras_nombre_mecanico:
      palabra_en_minusculas_m = palabra_individual.lower()
      tiene_vocal_m = any(
          caracter_v in caracteres_vocales for caracter_v in palabra_en_minusculas_m
      )
      tiene_consonante_m = any(
          caracter_v not in caracteres_vocales
          for caracter_v in palabra_en_minusculas_m
      )
      if not (tiene_vocal_m and tiene_consonante_m):
        estado_estructura_mec = False
        break

    if not estado_estructura_mec:
      print(
          "[!] Error: Cada palabra debe contener al menos una vocal y"
          " consonantes."
      )
      continue

    bandera_nombre_repetido_mec = False
    try:
      descriptor_archivo_mecanicos = open("mecanicos.txt", "r")
      for linea_actual_archivo in descriptor_archivo_mecanicos:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 2
            and lista_datos_separados[1].lower()
            == nombre_completo_mecanico.lower()
        ):
          bandera_nombre_repetido_mec = True
          break
      descriptor_archivo_mecanicos.close()
    except FileNotFoundError:
      pass

    if bandera_nombre_repetido_mec:
      print("[!] Error: Este nombre de mecánico ya se encuentra registrado.")
      continue

    bandera_nombre_repetido_cli = False
    try:
      descriptor_archivo_clientes = open("clientes.txt", "r")
      for linea_actual_archivo in descriptor_archivo_clientes:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 2
            and lista_datos_separados[1].lower()
            == nombre_completo_mecanico.lower()
        ):
          bandera_nombre_repetido_cli = True
          break
      descriptor_archivo_clientes.close()
    except FileNotFoundError:
      pass

    if bandera_nombre_repetido_cli:
      print(
          "[!] Error: Este nombre ya está registrado como cliente en el"
          " sistema."
      )
      continue

    break

  descriptor_archivo_escritura = open("mecanicos.txt", "a")
  descriptor_archivo_escritura.write(
      codigo_mecanico_ingresado + "," + nombre_completo_mecanico + "\n"
  )
  descriptor_archivo_escritura.close()
  print("¡Mecánico registrado con éxito!")


def registrar_servicio():
  print("\n--- 4. REGISTRAR SERVICIO ---")

  while True:
    codigo_servicio_ingresado = input(
        "Código del servicio (Ej. SRV-001): "
    ).strip()

    if len(codigo_servicio_ingresado) == 7:
      prefijo_servicio = codigo_servicio_ingresado[0:3]
      guion_servicio = codigo_servicio_ingresado[3]
      digitos_servicio = codigo_servicio_ingresado[4:7]

      if (
          prefijo_servicio.isupper()
          and all(caracter_c.isalpha() for caracter_c in prefijo_servicio)
          and guion_servicio == "-"
          and digitos_servicio.isdigit()
      ):
        bandera_codigo_serv_existe = False
        try:
          descriptor_archivo_servicios = open("servicios.txt", "r")
          for linea_actual_archivo in descriptor_archivo_servicios:
            lista_datos_separados = linea_actual_archivo.strip().split(",")
            if (
                len(lista_datos_separados) >= 1
                and lista_datos_separados[0] == codigo_servicio_ingresado
            ):
              bandera_codigo_serv_existe = True
              break
          descriptor_archivo_servicios.close()
        except FileNotFoundError:
          pass

        if bandera_codigo_serv_existe:
          print("[!] Error: Este código de servicio ya se encuentra registrado.")
          continue
        break

    print(
        "[!] Error: El código debe tener 3 letras mayúsculas, un guion y 3"
        " números (Ej: SRV-001)."
    )

  lista_servicios_disponibles = [
      "Cambio de Aceite (Max Q800)",
      "Servicio de Frenos (Max Q950)",
      "Alineacion y Balanceo (Max Q500)",
      "Diagnostico Electrico (Max Q650)",
      "Mantenimiento General (Max Q2750)",
      "Cambio de Faja de Tiempo (Max Q3750)",
      "Revision de Suspension (Max Q500)",
      "Limpieza de Inyectores (Max Q850)",
  ]

  lista_precios_maximos_serv = [
      800.0,
      950.0,
      500.0,
      650.0,
      2750.0,
      3750.0,
      500.0,
      850.0,
  ]

  while True:
    print("\n--- CATALOGO DE SERVICIOS DISPONIBLES ---")
    indice_servicio_catalogo = 0
    while indice_servicio_catalogo < len(lista_servicios_disponibles):
      print(
          str(indice_servicio_catalogo + 1)
          + ". "
          + lista_servicios_disponibles[indice_servicio_catalogo]
      )
      indice_servicio_catalogo = indice_servicio_catalogo + 1

    opcion_servicio_ingresada = input(
        "Selecciona el número del servicio o escribe el nombre exacto: "
    ).strip()

    nombre_servicio_seleccionado = ""
    indice_servicio_encontrado = -1

    if opcion_servicio_ingresada.isdigit():
      indice_convertido_s = int(opcion_servicio_ingresada) - 1
      if 0 <= indice_convertido_s < len(lista_servicios_disponibles):
        nombre_servicio_seleccionado = lista_servicios_disponibles[
            indice_convertido_s
        ]
        indice_servicio_encontrado = indice_convertido_s
    else:
      indice_busqueda_s = 0
      while indice_busqueda_s < len(lista_servicios_disponibles):
        if (
            lista_servicios_disponibles[indice_busqueda_s].lower()
            in opcion_servicio_ingresada.lower()
        ):
          nombre_servicio_seleccionado = lista_servicios_disponibles[
              indice_busqueda_s
          ]
          indice_servicio_encontrado = indice_busqueda_s
          break
        indice_busqueda_s = indice_busqueda_s + 1

    if nombre_servicio_seleccionado != "":
      bandera_servicio_repetido = False
      try:
        descriptor_archivo_servicios = open("servicios.txt", "r")
        for linea_actual_archivo in descriptor_archivo_servicios:
          lista_datos_separados = linea_actual_archivo.strip().split(",")
          if (
              len(lista_datos_separados) >= 2
              and lista_datos_separados[1].lower()
              == nombre_servicio_seleccionado.lower()
          ):
            bandera_servicio_repetido = True
            break
        descriptor_archivo_servicios.close()
      except FileNotFoundError:
        pass

      if bandera_servicio_repetido:
        print(
            "[!] Error: Este servicio ya se encuentra registrado en el"
            " sistema."
        )
        continue
      break

    print("[!] Error: Opción no válida o fuera del catálogo. Inténtalo de nuevo.")

  limite_maximo_servicio = lista_precios_maximos_serv[indice_servicio_encontrado]
  while True:
    precio_texto_ingresado = input(
        "Precio del servicio (Q) [Limite maximo Q"
        + str(limite_maximo_servicio)
        + "]: "
    ).strip()
    precio_texto_limpio_s = precio_texto_ingresado.replace(",", "")
    estado_precio_serv_valido = True
    try:
      precio_servicio_numerico = float(precio_texto_limpio_s)
      if (
          precio_servicio_numerico <= 0
          or precio_servicio_numerico > limite_maximo_servicio
      ):
        estado_precio_serv_valido = False
    except ValueError:
      estado_precio_serv_valido = False

    if estado_precio_serv_valido:
      break
    print(
        "[!] Error: Ingresa un precio válido mayor a 0 y que no supere el"
        " límite máximo de Q"
        + str(limite_maximo_servicio)
        + "."
    )

  descriptor_archivo_escritura = open("servicios.txt", "a")
  descriptor_archivo_escritura.write(
      codigo_servicio_ingresado
      + ","
      + nombre_servicio_seleccionado
      + ","
      + str(round(precio_servicio_numerico, 2))
      + "\n"
  )
  descriptor_archivo_escritura.close()
  print("¡Servicio registrado con éxito!")


def registrar_repuesto():
  print("\n--- 5. REGISTRAR REPUESTO ---")

  while True:
    codigo_repuesto_ingresado = input(
        "Código del repuesto (2 letras mayúsculas, dos ceros '00' y 1 número,"
        " Ej. FR002): "
    ).strip()

    if len(codigo_repuesto_ingresado) == 5:
      letras_repuesto = codigo_repuesto_ingresado[0:2]
      ceros_repuesto = codigo_repuesto_ingresado[2:4]
      numero_repuesto = codigo_repuesto_ingresado[4]

      if (
          letras_repuesto.isupper()
          and all(caracter_c.isalpha() for caracter_c in letras_repuesto)
          and ceros_repuesto == "00"
          and numero_repuesto.isdigit()
      ):
        bandera_codigo_rep_repetido = False
        try:
          descriptor_archivo_repuestos = open("repuestos.txt", "r")
          for linea_actual_archivo in descriptor_archivo_repuestos:
            lista_datos_separados = linea_actual_archivo.strip().split(",")
            if (
                len(lista_datos_separados) >= 1
                and lista_datos_separados[0] == codigo_repuesto_ingresado
            ):
              bandera_codigo_rep_repetido = True
              break
          descriptor_archivo_repuestos.close()
        except FileNotFoundError:
          pass

        if bandera_codigo_rep_repetido:
          print("[!] Error: Este código de repuesto ya se encuentra registrado.")
          continue
        break

    print(
        "[!] Error: El código debe tener 2 letras mayúsculas, dos ceros '00' y"
        " un número (Ej: FR002)."
    )

  lista_catalogo_repuestos = [
      ("Llanta Radial", 3500.0),
      ("Rin de Aleacion", 1500.0),
      ("Copa para Rin", 250.0),
      ("Valvula de Llantas", 75.0),
      ("Tuerca de Rueda", 60.0),
      ("Bateria 12V", 1300.0),
      ("Alternador", 2000.0),
      ("Motor de Arranque", 2000.0),
      ("Bujia de Encendido", 150.0),
      ("Bobina de Encendido", 800.0),
      ("Fusible Automotriz", 60.0),
      ("Foco LED / Halogeno", 150.0),
      ("Pastillas de Freno", 800.0),
      ("Disco de Freno", 1000.0),
      ("Tambor de Freno", 1200.0),
      ("Liquido de Frenos", 150.0),
      ("Aceite de Motor", 450.0),
      ("Refrigerante / Coolant", 200.0),
      ("Filtro de Aceite / Aire", 200.0),
      ("Plumilla de Limpiabrisas", 150.0),
      ("Tapon de Carter", 75.0),
      ("Arandela de Tapon", 60.0),
      ("Amortiguador Delantero/Trasero", 1500.0),
      ("Rotula de Suspension", 650.0),
      ("Buje de Parrilla", 350.0),
      ("Banda de Distribucion", 750.0),
      ("Bomba de Agua", 950.0),
      ("Termostato", 350.0),
      ("Radiador Principal", 2000.0),
      ("Sensor de Oxigeno / MAF", 1100.0),
  ]

  while True:
    print("\n--- CATALOGO DE REPUESTOS DISPONIBLES ---")
    indice_catalogo = 0
    while indice_catalogo < len(lista_catalogo_repuestos):
      tupla_repuesto_actual = lista_catalogo_repuestos[indice_catalogo]
      print(
          str(indice_catalogo + 1)
          + ". "
          + tupla_repuesto_actual[0]
          + " (Precio Maximo Permitido: Q"
          + str(tupla_repuesto_actual[1])
          + ")"
      )
      indice_catalogo = indice_catalogo + 1

    opcion_repuesto_ingresada = input(
        "Selecciona el número del repuesto o escribe el nombre exacto: "
    ).strip()

    nombre_repuesto_seleccionado = ""
    limite_maximo_repuesto = 500.0

    if opcion_repuesto_ingresada.isdigit():
      indice_convertido_r = int(opcion_repuesto_ingresada) - 1
      if 0 <= indice_convertido_r < len(lista_catalogo_repuestos):
        tupla_seleccionada = lista_catalogo_repuestos[indice_convertido_r]
        nombre_repuesto_seleccionado = tupla_seleccionada[0]
        limite_maximo_repuesto = tupla_seleccionada[1]
    else:
      for tupla_r in lista_catalogo_repuestos:
        if tupla_r[0].lower() in opcion_repuesto_ingresada.lower():
          nombre_repuesto_seleccionado = tupla_r[0]
          limite_maximo_repuesto = tupla_r[1]
          break

    if nombre_repuesto_seleccionado != "":
      bandera_repuesto_repetido = False
      try:
        descriptor_archivo_repuestos = open("repuestos.txt", "r")
        for linea_actual_archivo in descriptor_archivo_repuestos:
          lista_datos_separados = linea_actual_archivo.strip().split(",")
          if (
              len(lista_datos_separados) >= 2
              and lista_datos_separados[1].lower()
              == nombre_repuesto_seleccionado.lower()
          ):
            bandera_repuesto_repetido = True
            break
        descriptor_archivo_repuestos.close()
      except FileNotFoundError:
        pass

      if bandera_repuesto_repetido:
        print(
            "[!] Error: Este repuesto ya se encuentra registrado en el"
            " inventario."
        )
        continue
      break

    print("[!] Error: Opción no válida o fuera del catálogo. Inténtalo de nuevo.")

  while True:
    precio_repuesto_texto = input(
        "Precio unitario (Q) [Limite maximo estricto Q"
        + str(limite_maximo_repuesto)
        + "]: "
    ).strip()
    precio_repuesto_limpio = precio_repuesto_texto.replace(",", "")
    try:
      precio_unitario_repuesto = float(precio_repuesto_limpio)
      if 0 < precio_unitario_repuesto <= limite_maximo_repuesto:
        break
      else:
        print(
            f"[!] Error estricto: El precio excede el límite máximo permitido"
            f" de Q{limite_maximo_repuesto} para este repuesto en el mercado. No"
            f" se puede guardar."
        )
    except ValueError:
      print("[!] Error: Ingresa un monto numérico válido.")

  while True:
    stock_repuesto_texto = input(
        "Existencias iniciales (stock) [Rango: 0 - 500]: "
    ).strip()
    stock_repuesto_limpio = stock_repuesto_texto.replace(",", "")
    try:
      cantidad_stock_inicial = int(stock_repuesto_limpio)
      if 0 <= cantidad_stock_inicial <= 500:
        break
      else:
        print(
            "[!] Error: Las existencias no pueden ser negativas ni superar las"
            " 500 unidades iniciales."
        )
    except ValueError:
      print("[!] Error: Ingresa una cantidad entera válida.")

  descriptor_archivo_escritura = open("repuestos.txt", "a")
  descriptor_archivo_escritura.write(
      codigo_repuesto_ingresado
      + ","
      + nombre_repuesto_seleccionado
      + ","
      + str(round(precio_unitario_repuesto, 2))
      + ","
      + str(cantidad_stock_inicial)
      + "\n"
  )
  descriptor_archivo_escritura.close()
  print("¡Repuesto registrado en inventario con éxito!")


def crear_orden_trabajo():
  print("\n--- 6. CREAR ORDEN DE TRABAJO Y CÁLCULO DE COSTOS ---")

  while True:
    numero_orden_ingresado = input(
        "Número correlativo de orden (5 dígitos numéricos, ej. 00001): "
    ).strip()
    if not (
        numero_orden_ingresado.isdigit() and len(numero_orden_ingresado) == 5
    ):
      print(
          "[!] Error: Inválido. El número correlativo debe contener"
          " exactamente 5 dígitos numéricos."
      )
      continue

    bandera_orden_repetida = False
    try:
      descriptor_archivo_ordenes = open("ordenes.txt", "r")
      for linea_actual_archivo in descriptor_archivo_ordenes:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 1
            and lista_datos_separados[0] == numero_orden_ingresado
        ):
          bandera_orden_repetida = True
          break
      descriptor_archivo_ordenes.close()
    except FileNotFoundError:
      pass

    if bandera_orden_repetida:
      print("[!] Error: Este número de orden ya existe. Ingresa uno diferente.")
      continue
    break

  while True:
    placa_vehiculo_orden = input(
        "Placa del vehículo a ingresar (Ej. D123ABC): "
    ).strip()
    bandera_placa_registrada = False
    try:
      descriptor_archivo_vehiculos = open("vehiculos.txt", "r")
      for linea_actual_archivo in descriptor_archivo_vehiculos:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 1
            and lista_datos_separados[0] == placa_vehiculo_orden
        ):
          bandera_placa_registrada = True
          break
      descriptor_archivo_vehiculos.close()
    except FileNotFoundError:
      pass

    if bandera_placa_registrada:
      break
    print("[!] Error: Inválido. Esta placa não está registrada en el sistema.")

  while True:
    codigo_mecanico_orden = input(
        "Código del mecánico asignado (Ej: EMP-0001): "
    ).strip()
    bandera_mecanico_registrado = False
    try:
      descriptor_archivo_mecanicos = open("mecanicos.txt", "r")
      for linea_actual_archivo in descriptor_archivo_mecanicos:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 1
            and lista_datos_separados[0] == codigo_mecanico_orden
        ):
          bandera_mecanico_registrado = True
          break
      descriptor_archivo_mecanicos.close()
    except FileNotFoundError:
      pass

    if bandera_mecanico_registrado:
      break
    print("[!] Error: Inválido. Este código de mecánico no existe en el sistema.")

  while True:
    mano_obra_texto_ingresada = input(
        "Costo base de mano de obra (Q) [Máximo Q5000.00]: "
    ).strip()
    mano_obra_limpia = mano_obra_texto_ingresada.replace(",", "")
    try:
      costo_mano_obra_numerico = float(mano_obra_limpia)
      if 0 <= costo_mano_obra_numerico <= 5000.0:
        break
      else:
        print(
            "[!] Error: El costo de mano de obra debe estar entre Q0.00 y"
            " Q5000.00."
        )
    except ValueError:
      print("[!] Error: Ingresa un monto numérico válido.")

  acumulado_costo_servicios = 0.0
  print("\n--- AGREGAR SERVICIOS A LA ORDEN ---")

  while True:
    while True:
      respuesta_agregar_servicio = input(
          "¿Deseas agregar un servicio registrado a la orden? (S/N): "
      ).strip().lower()
      if respuesta_agregar_servicio in ["s", "si", "n", "no"]:
        break
      print(
          "[!] Opción inválida. Responde únicamente con 'S' (Sí) o 'N' (No)."
      )

    if respuesta_agregar_servicio in ["n", "no"]:
      break

    codigo_servicio_buscado = input(
        "Ingresa el código del servicio registrado (Ej: SRV-001): "
    ).strip()
    bandera_servicio_encontrado = False
    try:
      descriptor_archivo_servicios = open("servicios.txt", "r")
      for linea_actual_archivo in descriptor_archivo_servicios:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 3
            and lista_datos_separados[0] == codigo_servicio_buscado
        ):
          acumulado_costo_servicios += float(lista_datos_separados[2])
          bandera_servicio_encontrado = True
          print(
              "-> Servicio agregado: "
              + lista_datos_separados[1]
              + " (Q"
              + lista_datos_separados[2]
              + ")"
          )
          break
      descriptor_archivo_servicios.close()
    except FileNotFoundError:
      print("[!] No hay servicios registrados aún.")
      break

    if not bandera_servicio_encontrado:
      print("[!] Servicio no encontrado.")

  acumulado_costo_repuestos = 0.0
  print("\n--- AGREGAR REPUESTOS A LA ORDEN ---")

  while True:
    while True:
      respuesta_agregar_repuesto = input(
          "¿Deseas agregar un repuesto a la orden? (S/N): "
      ).strip().lower()
      if respuesta_agregar_repuesto in ["s", "si", "n", "no"]:
        break
      print(
          "[!] Opción inválida. Responde únicamente con 'S' (Sí) o 'N' (No)."
      )

    if respuesta_agregar_repuesto in ["n", "no"]:
      break

    codigo_repuesto_buscado = input(
        "Ingresa el código del repuesto (Ej: FR002): "
    ).strip()

    lista_repuestos_actualizada = []
    bandera_repuesto_encontrado = False

    try:
      descriptor_archivo_repuestos = open("repuestos.txt", "r")
      for linea_actual_archivo in descriptor_archivo_repuestos:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 4
            and lista_datos_separados[0] == codigo_repuesto_buscado
        ):
          bandera_repuesto_encontrado = True
          precio_unitario_actual = float(lista_datos_separados[2])
          stock_disponible_actual = int(lista_datos_separados[3])

          print(
              "Repuesto: "
              + lista_datos_separados[1]
              + " | Stock disponible: "
              + str(stock_disponible_actual)
              + " | Precio: Q"
              + lista_datos_separados[2]
          )

          if stock_disponible_actual <= 0:
            print("[!] Error: No hay existencias disponibles de este repuesto.")
          else:
            cantidad_texto_ingresada = input("Cantidad a utilizar: ").strip()
            cantidad_texto_limpia = cantidad_texto_ingresada.replace(",", "")
            try:
              cantidad_a_usar_entera = int(cantidad_texto_limpia)
              if (
                  cantidad_a_usar_entera > stock_disponible_actual
                  or cantidad_a_usar_entera <= 0
              ):
                print(
                    "[!] Error: Cantidad no permitida por sobrepasar el stock o"
                    " ser inválida."
                )
              else:
                nuevo_stock_calculado = (
                    stock_disponible_actual - cantidad_a_usar_entera
                )
                lista_datos_separados[3] = str(nuevo_stock_calculado)
                acumulado_costo_repuestos += (
                    precio_unitario_actual * cantidad_a_usar_entera
                )
                print(
                    "-> Repuesto agregado. Nuevo stock restante: "
                    + str(nuevo_stock_calculado)
                )
            except ValueError:
              print("[!] Error: Ingresa un número entero válido.")

        lista_repuestos_actualizada.append(
            ",".join(lista_datos_separados) + "\n"
        )
      descriptor_archivo_repuestos.close()

      if bandera_repuesto_encontrado:
        descriptor_archivo_escritura_rep = open("repuestos.txt", "w")
        descriptor_archivo_escritura_rep.writelines(
            lista_repuestos_actualizada
        )
        descriptor_archivo_escritura_rep.close()
      else:
        print("[!] Repuesto no encontrado.")

    except FileNotFoundError:
      print("[!] No hay repuestos en inventario.")
      break

  subtotal_orden = (
      costo_mano_obra_numerico
      + acumulado_costo_servicios
      + acumulado_costo_repuestos
  )
  impuesto_iva_orden = subtotal_orden * 0.12
  total_general_orden = subtotal_orden + impuesto_iva_orden
  estado_reparacion_inicial = "Recibida"
  estado_pago_inicial = "Pendiente por pagar"

  descriptor_archivo_escritura_ord = open("ordenes.txt", "a")
  descriptor_archivo_escritura_ord.write(
      numero_orden_ingresado
      + ","
      + placa_vehiculo_orden
      + ","
      + codigo_mecanico_orden
      + ","
      + str(round(total_general_orden, 2))
      + ","
      + estado_reparacion_inicial
      + ","
      + estado_pago_inicial
      + "\n"
  )
  descriptor_archivo_escritura_ord.close()

  print("\n¡Orden de trabajo generada correctamente!")
  print("Estado inicial: " + estado_reparacion_inicial)
  print("Mano de obra: Q" + str(round(costo_mano_obra_numerico, 2)))
  print("Servicios: Q" + str(round(acumulado_costo_servicios, 2)))
  print("Repuestos: Q" + str(round(acumulado_costo_repuestos, 2)))
  print("Subtotal: Q" + str(round(subtotal_orden, 2)))
  print("IVA (12%): Q" + str(round(impuesto_iva_orden, 2)))
  print("Total general a pagar: Q" + str(round(total_general_orden, 2)))


def actualizar_estado():
  print("\n--- 7. ACTUALIZAR ESTADO DE REPARACIÓN ---")

  while True:
    numero_orden_a_actualizar = input(
        "Ingresa el número de orden a actualizar: "
    ).strip()
    bandera_orden_existe = False
    try:
      descriptor_archivo_comprobar = open("ordenes.txt", "r")
      for linea_actual_archivo in descriptor_archivo_comprobar:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 1
            and lista_datos_separados[0] == numero_orden_a_actualizar
        ):
          bandera_orden_existe = True
          break
      descriptor_archivo_comprobar.close()
    except FileNotFoundError:
      pass

    if bandera_orden_existe:
      break
    print("[!] Error: No se encontró ninguna orden con ese número.")

  print("\nEstados sugeridos:")
  print("1. Recibida")
  print("2. En diagnostico")
  print("3. En reparacion")
  print("4. Finalizada")
  print("5. Entregada")

  while True:
    opcion_estado_ingresada = input(
        "Selecciona el nuevo estado (1-5): "
    ).strip()
    if opcion_estado_ingresada in ["1", "2", "3", "4", "5"]:
      break
    print("[!] Error: Opción no válida. Ingresa un número del 1 al 5.")

  diccionario_estados_reparacion = {
      "1": "Recibida",
      "2": "En diagnostico",
      "3": "En reparacion",
      "4": "Finalizada",
      "5": "Entregada",
  }
  nuevo_estado_seleccionado = diccionario_estados_reparacion.get(
      opcion_estado_ingresada, "Recibida"
  )

  lista_ordenes_actualizadas = []
  bandera_orden_encontrada = False

  try:
    descriptor_archivo_lectura_ord = open("ordenes.txt", "r")
    for linea_actual_archivo in descriptor_archivo_lectura_ord:
      lista_datos_separados = linea_actual_archivo.strip().split(",")
      if (
          len(lista_datos_separados) >= 6
          and lista_datos_separados[0] == numero_orden_a_actualizar
      ):
        lista_datos_separados[4] = nuevo_estado_seleccionado
        bandera_orden_encontrada = True

      if len(lista_datos_separados) < 6:
        while len(lista_datos_separados) < 6:
          lista_datos_separados.append("Pendiente por pagar")

      lista_ordenes_actualizadas.append(
          ",".join(lista_datos_separados[:6]) + "\n"
      )
    descriptor_archivo_lectura_ord.close()

    if bandera_orden_encontrada:
      descriptor_archivo_escritura_ord = open("ordenes.txt", "w")
      descriptor_archivo_escritura_ord.writelines(lista_ordenes_actualizadas)
      descriptor_archivo_escritura_ord.close()
      print(
          "¡Estado actualizado a '"
          + nuevo_estado_seleccionado
          + "' exitosamente!"
      )
    else:
      print("[!] No se encontró la orden indicada.")
  except FileNotFoundError:
    print("[!] No hay órdenes registradas.")


def registrar_pago():
  print("\n--- 8. REGISTRAR PAGO ---")

  while True:
    numero_orden_a_cobrar = input(
        "Ingresa el número de orden a cobrar: "
    ).strip()
    bandera_orden_existe_pago = False
    bandera_orden_ya_pagada = False
    try:
      descriptor_archivo_comprobar = open("ordenes.txt", "r")
      for linea_actual_archivo in descriptor_archivo_comprobar:
        lista_datos_separados = linea_actual_archivo.strip().split(",")
        if (
            len(lista_datos_separados) >= 6
            and lista_datos_separados[0] == numero_orden_a_cobrar
        ):
          bandera_orden_existe_pago = True
          if lista_datos_separados[5] == "Pagado":
            bandera_orden_ya_pagada = True
          break
      descriptor_archivo_comprobar.close()
    except FileNotFoundError:
      pass

    if not bandera_orden_existe_pago:
      print("[!] Error: La orden ingresada no existe en el sistema.")
      continue
    if bandera_orden_ya_pagada:
      print("[!] Error: Esta orden ya fue registrada como pagada anteriormente.")
      continue
    break

  lista_ordenes_actualizadas_pago = []
  bandera_pago_encontrado = False

  try:
    descriptor_archivo_lectura_ord = open("ordenes.txt", "r")
    for linea_actual_archivo in descriptor_archivo_lectura_ord:
      lista_datos_separados = linea_actual_archivo.strip().split(",")
      if (
          len(lista_datos_separados) >= 6
          and lista_datos_separados[0] == numero_orden_a_cobrar
      ):
        print("Monto total a pagar: Q" + lista_datos_separados[3])
        confirmacion_pago_usuario = input(
            "¿Confirmar registro de pago? (S/N): "
        ).strip().lower()
        if confirmacion_pago_usuario in ["s", "si"]:
          lista_datos_separados[5] = "Pagado"
          bandera_pago_encontrado = True

      if len(lista_datos_separados) < 6:
        while len(lista_datos_separados) < 6:
          lista_datos_separados.append("Pendiente por pagar")

      lista_ordenes_actualizadas_pago.append(
          ",".join(lista_datos_separados[:6]) + "\n"
      )
    descriptor_archivo_lectura_ord.close()

    if bandera_pago_encontrado:
      descriptor_archivo_escritura_ord = open("ordenes.txt", "w")
      descriptor_archivo_escritura_ord.writelines(
          lista_ordenes_actualizadas_pago
      )
      descriptor_archivo_escritura_ord.close()
      print("¡Pago registrado con éxito!")
    else:
      print("[!] Operación cancelada o no se pudo registrar el pago.")
  except FileNotFoundError:
    print("[!] No existen órdenes de trabajo.")


def consultar_historial():
  print("\n--- 9. CONSULTAR HISTORIAL DE VEHÍCULO ---")
  placa_vehiculo_a_consultar = input("Ingresa la placa a consultar: ")
  bandera_historial_encontrado = False

  try:
    descriptor_archivo_ordenes = open("ordenes.txt", "r")
    print("\n--- ÓRDENES DE TRABAJO REGISTRADAS ---")
    for linea_actual_archivo in descriptor_archivo_ordenes:
      lista_datos_separados = linea_actual_archivo.strip().split(",")
      if (
          len(lista_datos_separados) >= 6
          and lista_datos_separados[1] == placa_vehiculo_a_consultar
      ):
        print(
            "Orden #: "
            + lista_datos_separados[0]
            + " | Mecánico: "
            + lista_datos_separados[2]
            + " | Total: Q"
            + lista_datos_separados[3]
            + " | Estado: "
            + lista_datos_separados[4]
            + " | Pago: "
            + lista_datos_separados[5]
        )
        bandera_historial_encontrado = True
    descriptor_archivo_ordenes.close()

    if not bandera_historial_encontrado:
      print("[!] No se encontraron órdenes anteriores para esta placa.")
  except FileNotFoundError:
    print("[!] No hay historial registrado.")


def main():
  # Inicializamos los archivos automáticamente al arrancar
  inicializar_archivos()

  mostrar_caratula()
  bandera_sistema_activo = True

  while bandera_sistema_activo:
    print("\n==========================================")
    print("    MENÚ ADMINISTRACIÓN TALLER AUTOMOTRIZ ")
    print("==========================================")
    print("1. Registrar Cliente")
    print("2. Registrar Vehículo")
    print("3. Registrar Mecánico")
    print("4. Registrar Servicio")
    print("5. Registrar Repuesto")
    print("6. Crear Orden de Trabajo")
    print("7. Actualizar Estado de Reparación")
    print("8. Registrar Pago")
    print("9. Consultar Historial de Vehículo")
    print("10. Salir")

    opcion_menu_principal = input("Elige una opción (1-10): ")

    if opcion_menu_principal == "1":
      registrar_cliente()
    elif opcion_menu_principal == "2":
      registrar_vehiculo()
    elif opcion_menu_principal == "3":
      registrar_mecanico()
    elif opcion_menu_principal == "4":
      registrar_servicio()
    elif opcion_menu_principal == "5":
      registrar_repuesto()
    elif opcion_menu_principal == "6":
      crear_orden_trabajo()
    elif opcion_menu_principal == "7":
      actualizar_estado()
    elif opcion_menu_principal == "8":
      registrar_pago()
    elif opcion_menu_principal == "9":
      consultar_historial()
    elif opcion_menu_principal == "10":
      print(
          "\nSaliendo del programa... ¡Mucho éxito en la Vida! Muchas Gracias"
          " Feliz Dia."
      )
      bandera_sistema_activo = False
    else:
      print("[!] Opción incorrecta, ingresa un número del 1 al 10.")


if _name_ == "_main_":
  main()
