
# Definir las matrices para almacenar usuarios, notas y roles
usuarios = []
notas = []
roles = []
promedio_notas = []

# Función de registro de nuevos usuarios
def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    rol = input("Rol (Estudiante/Profesor): ").lower()
    
    if rol not in ['estudiante', 'profesor']:
        print("Rol no válido. Debe ser 'Estudiante' o 'Profesor'.")
        return
    
    # Agregar usuario, rol y password a las matrices
    usuarios.append(username)
    roles.append(rol)
    notas.append([])  # Inicializar una lista vacía para las notas de este usuario
    promedio_notas.append(0)  # Inicializar promedio de notas
    
    print("Usuario registrado con éxito.")

# Función de login
def login():
    print("\n--- Iniciar Sesión ---")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    
    if username in usuarios:
        index = usuarios.index(username)
        print(f"Bienvenido {username}!")
        return index
    else:
        print("Usuario no encontrado.")
        return None

# Función para consultar las notas (solo estudiantes)
def consultar_notas(index):
    if roles[index] == "estudiante":
        print("\n--- Consultar Notas ---")
        if len(notas[index]) > 0:
            print("Tus notas son:", notas[index])
            print("Promedio de notas:", promedio_notas[index])
        else:
            print("No tienes notas registradas.")
    else:
        print("Acción no permitida. Solo los estudiantes pueden consultar notas.")

# Función para agregar notas (solo profesores)
def agregar_notas(index):
    if roles[index] == "profesor":
        print("\n--- Agregar Notas ---")
        estudiante = input("Ingresa el nombre del estudiante: ")
        if estudiante in usuarios:
            estudiante_index = usuarios.index(estudiante)
            nueva_nota = float(input("Ingresa la nueva nota: "))
            notas[estudiante_index].append(nueva_nota)
            promedio_notas[estudiante_index] = sum(notas[estudiante_index]) / len(notas[estudiante_index])
            print(f"Nota registrada para {estudiante}. Nuevo promedio: {promedio_notas[estudiante_index]}")
        else:
            print("Estudiante no encontrado.")
    else:
        print("Acción no permitida. Solo los profesores pueden agregar notas.")

# Función para mostrar el menú principal
def menu_principal(index):
    while True:
        if roles[index] == "estudiante":
            print("\n--- Menú Estudiante ---")
            print("1. Consultar notas")
            print("2. Salir")
            opcion = input("Elige una opción: ")
            
            if opcion == "1":
                consultar_notas(index)
            elif opcion == "2":
                break
            else:
                print("Opción no válida.")
        
        elif roles[index] == "profesor":
            print("\n--- Menú Profesor ---")
            print("1. Agregar notas")
           
            print("3. Salir")
            opcion = input("Elige una opción: ")
            
            if opcion == "1":
                agregar_notas(index)
            elif opcion == "3":
                break
            else:
                print("Opción no válida.")

# Función principal para ejecutar el sistema
def gestor_de_notas():
    while True:
        print("\n--- Gestor de Notas ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            index = login()
            if index is not None:
                menu_principal(index)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# Ejecutar el gestor de notas
gestor_de_notas()